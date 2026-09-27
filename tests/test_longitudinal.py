"""Synthetic contract tests; no tuning against the ten research cases."""
from copy import deepcopy
from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

from jsonschema import Draft202012Validator
from ibe_longitudinal.cli import main
from ibe_longitudinal.freeze import initialize
from ibe_longitudinal.report import render
from ibe_longitudinal.store import append, encoded, extend, loads, read
from ibe_longitudinal.validation import DIMENSIONS, ValidationError, digest, validate

REPO = Path(__file__).resolve().parents[1]
T = '2026-01-02T00:00:00Z'


def seed(root):
    (root / 'report.md').write_text('Frozen synthetic claim: component A fails.\n')
    (root / 'metadata.json').write_text(json.dumps({'issue_url':'https://github.com/example/synthetic/issues/1', 'snapshot_completed_utc':'2026-01-01T00:00:00Z'}))
    return {'schema_version':'1.0.0', 'dataset_id':'synthetic', 'frozen_release':'test-only',
            'artifacts':[{'id':i, 'path':p, 'sha256':digest((root/p).read_bytes()), 'kind':k} for i,p,k in [('report','report.md','frozen_report'), ('metadata','metadata.json','frozen_metadata')]],
            'cases':[{'id':'case-a','issue_url':'https://github.com/example/synthetic/issues/1', 'frozen_at':'2026-01-01T00:00:00Z','report_artifact_id':'report','metadata_artifact_id':'metadata'}], 'events':[]}


def event(eid, kind, payload):
    return {'id':eid,'case_id':'case-a','recorded_at':T,'actor':'synthetic-researcher','kind':kind,'payload':payload}


def evidence(eid='ev-1'):
    return event(eid,'evidence',{'kind':'maintainer_comment','occurred_at':T,'observed_at':T,'temporal_scope':'post_freeze','epistemic_status':'maintainer_confirmed_fact','statement':'Synthetic confirmation.', 'source':{'url':'https://github.com/example/synthetic/issues/1#issuecomment-1','locator':'comment 1','excerpt':'Component A fails.','author':'synthetic-maintainer','author_role':'maintainer','artifact_id':None}})


def adjudication(dimension):
    return event('dim-'+dimension,'adjudication',{'dimension':dimension,'verdict':'supported','epistemic_status':'researcher_inference','frozen_claim':'Frozen synthetic claim.','rationale':'Synthetic reasoning based on ev-1.','evidence_ids':['ev-1'],'unresolved_questions':[],'supersedes':None})


def outcome():
    return event('out-1','outcome',{'status':'final','issue_state':'closed','resolution':'fixed','rationale':'Explicit synthetic research decision.','evidence_ids':['ev-1'],'dimension_ids':{d:'dim-'+d for d in DIMENSIONS},'unresolved_questions':[],'supersedes':None})


def batch(events):
    return {'artifacts':[],'events':events}


class LongitudinalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = seed(self.root)

    def complete(self):
        return extend(self.data, batch([evidence(), *map(adjudication,DIMENSIONS), outcome()]), self.root)

    def test_schema_is_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(read(REPO/'src/ibe_longitudinal/schema.json'))

    def test_valid_history_preserves_input_and_all_five_dimensions(self):
        original = deepcopy(self.data)
        result = self.complete()
        self.assertEqual(self.data, original)
        self.assertEqual(len(result['events']), 7)
        validate(result, self.root, self.data)

    def test_schema_rejects_unknown_keys_enum_and_missing_dimension(self):
        for mutation in ('extra','enum','missing','timestamp'):
            with self.subTest(mutation=mutation):
                events = [evidence(), *map(adjudication,DIMENSIONS), outcome()]
                if mutation == 'extra': events[0]['payload']['score'] = 42
                if mutation == 'enum': events[0]['payload']['epistemic_status'] = 'fact-ish'
                if mutation == 'missing': del events[-1]['payload']['dimension_ids']['cause']
                if mutation == 'timestamp': events[0]['recorded_at'] = '2026-02-30T00:00:00Z'
                with self.assertRaises(ValidationError): extend(self.data,batch(events))

    def test_unknown_case_duplicate_ids_and_forward_refs_rejected(self):
        for mutation in ('unknown','duplicate','forward'):
            with self.subTest(mutation=mutation):
                events = [evidence()]
                if mutation == 'unknown': events[0]['case_id'] = 'missing'
                if mutation == 'duplicate': events.append(evidence())
                if mutation == 'forward': events.insert(0,adjudication('cause'))
                with self.assertRaises(ValidationError): extend(self.data,batch(events))

    def test_cross_case_evidence_reference_rejected(self):
        other = deepcopy(self.data['cases'][0]); other.update(id='case-b',issue_url='https://github.com/example/synthetic/issues/2')
        self.data['cases'].append(other)
        ev = evidence(); ev['case_id'] = 'case-b'
        with self.assertRaisesRegex(ValidationError,'invalid evidence reference'):
            extend(self.data,batch([ev,adjudication('cause')]))

    def test_pre_freeze_context_is_allowed_but_cannot_masquerade_as_new_evidence(self):
        ev = evidence(); ev['payload']['occurred_at'] = '2025-12-31T00:00:00Z'
        with self.assertRaisesRegex(ValidationError,'pre/post-freeze'):
            extend(self.data,batch([ev]))
        ev['payload']['temporal_scope'] = 'pre_freeze_context'
        validate(extend(self.data,batch([ev])))

    def test_freeze_boundary_is_context_not_post_freeze(self):
        ev = evidence(); ev['payload']['occurred_at'] = self.data['cases'][0]['frozen_at']
        with self.assertRaises(ValidationError): extend(self.data,batch([ev]))
        ev['payload']['temporal_scope'] = 'pre_freeze_context'
        extend(self.data,batch([ev]))

    def test_observation_and_recording_chronology(self):
        for mutation in ('future_event','future_observation','early_record','backwards_record'):
            with self.subTest(mutation=mutation):
                events = [evidence()]
                if mutation == 'future_event': events[0]['payload']['occurred_at'] = '2026-01-03T00:00:00Z'
                if mutation == 'future_observation': events[0]['payload']['observed_at'] = '2026-01-03T00:00:00Z'
                if mutation == 'early_record': events[0]['recorded_at'] = '2025-12-31T00:00:00Z'
                if mutation == 'backwards_record':
                    ev = evidence('ev-2'); ev['recorded_at'] = '2026-01-01T01:00:00Z'; events.append(ev)
                with self.assertRaises(ValidationError): extend(self.data,batch(events))

    def test_no_false_maintainer_confirmation(self):
        ev=evidence(); ev['payload']['source']['author_role']='reporter'
        with self.assertRaisesRegex(ValidationError,'maintainer provenance'): extend(self.data,batch([ev]))
        ev['payload']['epistemic_status']='observed_fact'
        adj=adjudication('cause'); adj['payload']['epistemic_status']='maintainer_confirmed_fact'
        with self.assertRaisesRegex(ValidationError,'lacks maintainer'): extend(self.data,batch([ev,adj]))

    def test_inference_only_evidence_cannot_be_promoted_to_observed_fact(self):
        ev=evidence(); ev['payload']['epistemic_status']='researcher_inference'
        adj=adjudication('cause'); adj['payload']['epistemic_status']='observed_fact'
        with self.assertRaisesRegex(ValidationError,'inference only'):
            extend(self.data,batch([ev,adj]))

    def test_adjudication_requires_evidence_except_unresolved_or_not_assessed(self):
        adj=adjudication('cause'); adj['payload']['evidence_ids']=[]
        with self.assertRaisesRegex(ValidationError,'needs evidence'): extend(self.data,batch([adj]))
        adj['payload'].update(verdict='unresolved',unresolved_questions=['What caused this?'])
        extend(self.data,batch([adj]))

    def test_closed_issue_can_remain_unresolved(self):
        events=[evidence(),*map(adjudication,DIMENSIONS),outcome()]
        events[-1]['payload'].update(status='unresolved',resolution='unknown',unresolved_questions=['Was the fix released?'])
        result=extend(self.data,batch(events))
        self.assertIn('unresolved',render(result))
        self.assertEqual(result['events'][-1]['payload']['issue_state'],'closed')

    def test_final_requires_resolution_evidence_and_resolved_dimensions(self):
        for mutation in ('unknown','no_evidence','questions','dimension','dimension_questions'):
            with self.subTest(mutation=mutation):
                events=[evidence(),*map(adjudication,DIMENSIONS),outcome()]
                if mutation=='unknown': events[-1]['payload']['resolution']='unknown'
                if mutation=='no_evidence': events[-1]['payload']['evidence_ids']=[]
                if mutation=='questions': events[-1]['payload']['unresolved_questions']=['Still unknown']
                if mutation=='dimension': events[1]['payload'].update(verdict='unresolved',unresolved_questions=['Still unknown'])
                if mutation=='dimension_questions': events[1]['payload']['unresolved_questions']=['Still unknown']
                with self.assertRaises(ValidationError): extend(self.data,batch(events))

    def test_revision_must_supersede_latest_same_dimension(self):
        result=self.complete()
        revised=adjudication('cause'); revised['id']='cause-revised'
        with self.assertRaisesRegex(ValidationError,'supersedes'): extend(result,batch([revised]))
        revised['payload']['supersedes']='dim-cause'
        updated=extend(result,batch([revised]))
        self.assertEqual(updated['events'][:7],result['events'])
        self.assertIn('Review required',render(updated))
        old_out=outcome(); old_out['id']='out-2'; old_out['payload']['supersedes']='out-1'
        with self.assertRaisesRegex(ValidationError,'latest cause'): extend(updated,batch([old_out]))

    def test_explicit_not_claimed_dimension_does_not_force_a_claim_for_finality(self):
        events=[evidence(),*map(adjudication,DIMENSIONS),outcome()]
        severity=next(e for e in events if e['kind']=='adjudication' and e['payload']['dimension']=='severity')
        severity['payload']['verdict']='not_claimed'
        severity['payload']['frozen_claim']='The frozen report makes no severity claim.'
        result=extend(self.data,batch(events))
        self.assertEqual(result['events'][-1]['payload']['status'],'final')

    def test_reopen_preserves_old_final_and_allows_new_unresolved_outcome(self):
        result=self.complete(); ev=evidence('reopen'); ev['payload']['kind']='reopen'
        out=outcome(); out['id']='out-2'; out['payload'].update(status='unresolved',issue_state='open',resolution='unknown',evidence_ids=['reopen'],unresolved_questions=['Why did the fix fail?'],supersedes='out-1')
        updated=extend(result,batch([ev,out]))
        self.assertEqual(updated['events'][6]['payload']['status'],'final')
        self.assertEqual(updated['events'][-1]['payload']['status'],'unresolved')

    def test_history_deletion_and_rewritten_chain_rejected_against_baseline(self):
        previous=self.complete()
        with self.assertRaisesRegex(ValidationError,'historical events'):
            validate(self.data,previous=previous)
        events=deepcopy(previous['events'])
        for ev in events:
            del ev['hash']; del ev['previous_hash']
        events[0]['payload']['statement']='Rewritten history'
        rewritten=extend(self.data,batch(events))
        with self.assertRaisesRegex(ValidationError,'historical events'):
            validate(rewritten,previous=previous)

    def test_header_and_artifact_history_are_immutable(self):
        for key in ('cases','artifacts','frozen_release'):
            changed=deepcopy(self.data)
            if key=='cases': changed[key][0]['frozen_at']='2025-01-01T00:00:00Z'
            if key=='artifacts': changed[key][0]['sha256']='0'*64
            if key=='frozen_release': changed[key]='other'
            with self.assertRaises(ValidationError): validate(changed,previous=self.data)

    def test_hash_chain_detects_modified_event(self):
        result=self.complete(); result['events'][0]['actor']='someone-else'
        with self.assertRaisesRegex(ValidationError,'hash chain'): validate(result)

    def test_artifact_modification_missing_and_traversal_rejected(self):
        (self.root/'report.md').write_text('Modified')
        with self.assertRaisesRegex(ValidationError,'hash mismatch'): validate(self.data,self.root)
        (self.root/'report.md').unlink()
        with self.assertRaisesRegex(ValidationError,'missing artifact'): validate(self.data,self.root)
        for path in ('../escape','/tmp/escape'):
            bad=deepcopy(self.data); bad['artifacts'][0]['path']=path
            with self.assertRaisesRegex(ValidationError,'unsafe artifact'): validate(bad)

    def test_symlink_escape_rejected(self):
        (self.root/'report.md').unlink(); (self.root/'report.md').symlink_to(self.root.parent/'outside')
        with self.assertRaisesRegex(ValidationError,'escapes root'): validate(self.data,self.root)

    def test_metadata_mismatch_rejected_even_with_updated_file_digest(self):
        p=self.root/'metadata.json'; meta=read(p); meta['issue_url']='https://github.com/example/other/issues/1'; p.write_text(json.dumps(meta))
        self.data['artifacts'][1]['sha256']=digest(p.read_bytes())
        with self.assertRaisesRegex(ValidationError,'metadata issue'): validate(self.data,self.root)

    def test_atomic_append_stale_writer_lock_and_validation_failure(self):
        path=self.root/'journal.json'; path.write_bytes(encoded(self.data)); original=path.read_bytes()
        with self.assertRaisesRegex(ValidationError,'changed since review'): append(path,batch([evidence()]),'0'*64)
        lock=self.root/'journal.json.lock'; lock.mkdir()
        with self.assertRaisesRegex(ValidationError,'locked'): append(path,batch([evidence()]),digest(original))
        lock.rmdir()
        invalid=evidence(); invalid['case_id']='missing'
        with self.assertRaises(ValidationError): append(path,batch([invalid]),digest(original))
        self.assertEqual(path.read_bytes(),original)
        self.assertFalse(lock.exists())
        append(path,batch([evidence()]),digest(original))
        self.assertEqual(len(read(path)['events']),1)
        self.assertEqual(list(self.root.glob('.journal-*')),[])

    def test_strict_json_rejects_duplicate_keys_and_nonfinite_numbers(self):
        for text in ('{"a":1,"a":2}','{"a":NaN}','{"a":Infinity}'):
            with self.assertRaises(ValidationError): loads(text)

    def test_render_is_deterministic_and_has_historical_cutoff(self):
        result=self.complete()
        self.assertEqual(render(result),render(result))
        before=render(result,'2026-01-01T12:00:00Z')
        self.assertIn('Pending source import',before)
        self.assertNotIn('Synthetic confirmation',before)

    def test_report_escapes_untrusted_markup(self):
        ev=evidence(); ev['payload']['statement']='<script>bad</script> ![image](https://evil.test) @all\n# injected'
        output=render(extend(self.data,batch([ev])))
        self.assertNotIn('<script>',output)
        self.assertNotIn('![image]',output)
        self.assertNotIn('@all',output)
        self.assertNotIn('\n# injected',output)

    def test_cli_end_to_end_and_frozen_overwrite_protection(self):
        journal=self.root/'journal.json'; journal.write_bytes(encoded(self.data))
        additions=self.root/'batch.json'; additions.write_bytes(encoded(batch([evidence()])))
        with redirect_stdout(io.StringIO()),redirect_stderr(io.StringIO()):
            self.assertEqual(main(['validate',str(journal)]),0)
            self.assertEqual(main(['append',str(journal),str(additions),'--expected-sha256',digest(journal.read_bytes())]),0)
            out=self.root/'report-output.md'
            self.assertEqual(main(['report',str(journal),'--output',str(out)]),0)
            self.assertEqual(main(['report',str(journal),'--output',str(self.root/'report.md')]),2)
            self.assertEqual(main(['report',str(journal),'--output',str(self.root/'other.md'),'--as-of','2026-01-01']),2)
        validate(read(journal),self.root)
        self.assertTrue(out.exists())

    def make_archive(self, corrupt=False, unsafe=False):
        meta={'issue_url':'https://github.com/example/synthetic/issues/1','snapshot_completed_utc':'2026-01-01T00:00:00Z'}
        items={'cases/case-a/metadata.json':encoded(meta),'cases/case-a/report.md':b'Frozen report\n','MANIFEST.md':b'test'}
        checks=''.join(f'{digest(v)}  ./{k}\n' for k,v in items.items())
        archive=self.root/'freeze.zip'
        with zipfile.ZipFile(archive,'w') as z:
            for k,v in items.items(): z.writestr('freeze/'+k,v if not corrupt else v+b'changed')
            z.writestr('freeze/SHA256SUMS.txt',checks)
            if unsafe: z.writestr('../escape',b'bad')
        return archive

    def test_freeze_import_checks_every_member_and_preserves_bytes(self):
        archive=self.make_archive(); raw=archive.read_bytes(); dest=self.root/'dataset'
        data,count=initialize(archive,dest,'synthetic','test-only')
        self.assertEqual(count,3)
        self.assertEqual((dest/'sources/freeze.zip').read_bytes(),raw)
        self.assertEqual((dest/'frozen/case-a/report.md').read_bytes(),b'Frozen report\n')
        self.assertEqual(archive.read_bytes(),raw)
        self.assertEqual(data['events'],[])
        with self.assertRaises(ValidationError): initialize(archive,dest,'synthetic','test-only')

    def test_bad_freeze_fails_without_partial_dataset(self):
        for corrupt,unsafe in ((True,False),(False,True)):
            with self.subTest(corrupt=corrupt,unsafe=unsafe):
                archive=self.make_archive(corrupt,unsafe)
                with self.assertRaises(ValidationError): initialize(archive,self.root/'dataset','synthetic','test-only')
                self.assertFalse((self.root/'dataset').exists())

    def test_real_frozen_snapshot_integrity_without_using_cases_for_tuning(self):
        folder=REPO/'research/longitudinal/v0.1.0'
        journal=read(folder/'journal.json'); validate(journal,folder)
        archive=folder/'sources/freeze.zip'
        with zipfile.ZipFile(archive) as z:
            manifest=next(n for n in z.namelist() if n.endswith('/SHA256SUMS.txt'))
            prefix=manifest[:-len('SHA256SUMS.txt')]
            lines=z.read(manifest).decode().splitlines()
            self.assertEqual(len(lines),98)
            for line in lines:
                expected,path=line.split(maxsplit=1)
                self.assertEqual(digest(z.read(prefix+path.removeprefix('./'))),expected)
            for a in journal['artifacts']:
                if a['kind'] in ('frozen_report','frozen_metadata'):
                    original=prefix+a['path'].replace('frozen/','cases/',1)
                    self.assertEqual((folder/a['path']).read_bytes(),z.read(original))

    def test_engine_has_no_import_dependency_on_new_layer(self):
        for source in (REPO/'src/issue_boundary_evidence').glob('*.py'):
            self.assertNotIn('ibe_longitudinal',source.read_text())
        result=subprocess.run([sys.executable,'-c','import issue_boundary_evidence.cli; import sys; assert "ibe_longitudinal" not in sys.modules; assert "jsonschema" not in sys.modules'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)


if __name__=='__main__':
    unittest.main()
