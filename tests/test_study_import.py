"""Source-ingestion fidelity tests; none of these change or exercise heuristics."""
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from ibe_longitudinal.docx_source import blocks, extract, loads as source_loads
from ibe_longitudinal.report import render
from ibe_longitudinal.store import extend, read
from ibe_longitudinal.study import prepare
from ibe_longitudinal.validation import DIMENSIONS, ValidationError, digest, validate

ROOT = Path(__file__).resolve().parents[1] / 'research/longitudinal/v0.1.0'
SOURCES = ROOT / 'sources/study-2026-09-27'
SOURCE_ID = 'study-20260927-adjudication-recovered-json'


class StudyImportTests(unittest.TestCase):
    def setUp(self):
        self.study = read(SOURCES / 'adjudication-recovered.json')
        self.before = read(ROOT / 'history/journal-before-source-import.json')
        self.journal = read(ROOT / 'journal.json')
        self.batch = read(ROOT / 'history/import-batch-2026-09-27.json')
        self.artifacts = read(ROOT / 'history/source-artifacts-2026-09-27.json')
        self.recorded = self.batch['events'][0]['recorded_at']

    def prepare(self, study=None):
        return prepare(self.before, study or self.study, SOURCE_ID, 'study-20260927', self.recorded, self.artifacts)

    def test_reproducible_import_matches_reviewed_batch_and_journal(self):
        self.assertEqual(self.prepare(), self.batch)
        self.assertEqual(extend(self.before, self.batch, ROOT), self.journal)
        validate(self.journal, ROOT, self.before)

    def test_source_case_timestamps_and_hashes_match_all_frozen_inputs(self):
        cases = {c['issue_url']:c for c in self.before['cases']}
        artifacts = {a['id']:a for a in self.before['artifacts']}
        for c in self.study['cases']:
            frozen = cases[c['issue_url']]
            self.assertEqual(c['frozen_artifact']['snapshot_completed_utc'], frozen['frozen_at'])
            self.assertEqual(c['frozen_artifact']['report_sha256'], artifacts[frozen['report_artifact_id']]['sha256'])

    def test_every_source_dimension_and_alignment_preserved_exactly(self):
        events = [e for e in self.journal['events'] if e['kind']=='adjudication']
        self.assertEqual(len(events), len(self.study['cases'])*len(DIMENSIONS))
        for e in events:
            p=e['payload']; index=int(p['source_pointer']['pointer'].split('/')[-1]); source=self.study['cases'][index]
            self.assertEqual(p['source_assessment'], source['dimensions'][p['dimension']])
            self.assertEqual(p['frozen_alignment'], source['frozen_report_adjudication']['dimension_alignment'][p['dimension']])
            self.assertEqual(p['verdict'], 'source_recorded')
        self.assertEqual(sum(e['payload']['frozen_alignment']=='not_claimed' for e in events), 11)

    def test_timeline_edits_deletions_reviews_are_lossless(self):
        events=[e for e in self.journal['events'] if e['kind']=='evidence' and '/evidence_timeline/' in e['payload']['source']['locator']]
        self.assertEqual(len(events), sum(len(c['evidence_timeline']) for c in self.study['cases']))
        kinds=set()
        for e in events:
            p=e['payload']; parts=p['source']['locator'].split('/'); source=self.study['cases'][int(parts[2])]['evidence_timeline'][int(parts[4])]
            self.assertEqual(p['source_record'],source)
            self.assertEqual(p['occurred_at'],source['at_utc'])
            self.assertEqual(p['epistemic_status'],source['evidence_type'])
            self.assertEqual(p['source']['origin'],'research_summary')
            kinds.add(p['source_kind'])
        self.assertTrue({'comment_edit','deleted_comments','pr_review','pr_closed'}.issubset(kinds))

    def test_closed_is_not_final_and_disposition_and_questions_survive(self):
        outcomes=[e['payload'] for e in self.journal['events'] if e['kind']=='outcome']
        self.assertEqual(sum(p['issue_state']=='closed' for p in outcomes),3)
        self.assertTrue(all(p['status']=='unresolved' for p in outcomes))
        for p,case in zip(outcomes,self.study['cases']):
            self.assertEqual(p['source_disposition'],case['dimensions']['fix_trajectory']['status'])
            self.assertEqual(p['unresolved_questions'],case['unresolved'])
        self.assertIn('closed_no_fix',[p['source_disposition'] for p in outcomes])
        self.assertIn('main_merged_backport_unresolved',[p['source_disposition'] for p in outcomes])

    def test_snapshots_are_not_counted_as_post_freeze_upstream_events(self):
        snapshots=[e['payload'] for e in self.journal['events'] if e['kind']=='evidence' and e['payload']['kind']=='research_snapshot']
        self.assertEqual(len(snapshots),10)
        for p in snapshots:
            self.assertEqual(p['temporal_scope'],'research_snapshot')
            self.assertEqual(p['occurred_at'],self.study['as_of_utc'])
            self.assertEqual(p['observed_at'],self.study['as_of_utc'])

    def test_old_pr_and_release_transitions_remain_pre_freeze(self):
        transitions=[e['payload'] for e in self.journal['events'] if e['kind']=='evidence' and e['payload'].get('source_kind') in ('opened_utc','merged_utc','closed_utc','published_utc')]
        for p in transitions:
            self.assertEqual(p['occurred_at'],p['source_record'][p['source_kind']])
        old=[p for p in transitions if p['occurred_at'].startswith('2021-')]
        self.assertEqual(len(old),1)
        self.assertEqual(old[0]['temporal_scope'],'pre_freeze_context')
        release=next(p for p in transitions if p['source_kind']=='published_utc')
        self.assertEqual(release['temporal_scope'],'pre_freeze_context')

    def test_mismatched_source_identity_and_missing_dimensions_rejected(self):
        for field in ('freeze_hash','report_hash','timestamp','cases','dimensions','no_questions'):
            with self.subTest(field=field):
                source=deepcopy(self.study)
                if field=='freeze_hash': source['freeze']['archive_sha256']='0'*64
                if field=='report_hash': source['cases'][0]['frozen_artifact']['report_sha256']='0'*64
                if field=='timestamp': source['cases'][0]['frozen_artifact']['snapshot_completed_utc']='2026-01-01T00:00:00Z'
                if field=='cases': source['cases'].pop()
                if field=='dimensions': del source['cases'][0]['dimensions']['cause']
                if field=='no_questions': source['cases'][0]['unresolved']=[]
                with self.assertRaises(ValidationError): self.prepare(source)

    def test_duplicate_batch_and_backdated_import_rejected(self):
        with self.assertRaisesRegex(ValidationError,'already imported'):
            prepare(self.journal,self.study,SOURCE_ID,'study-20260927',self.recorded)
        with self.assertRaisesRegex(ValidationError,'backdate'):
            prepare(self.before,self.study,SOURCE_ID,'other','2026-09-01T00:00:00Z',self.artifacts)

    def test_tampered_source_record_pointer_and_cutoff_rejected(self):
        for field in ('record','pointer','cutoff','timeline','adjudication','outcome'):
            with self.subTest(field=field):
                candidate=deepcopy(self.batch)
                snapshot=candidate['events'][0]['payload']
                if field=='record': snapshot['source_record']['title']='Changed'
                if field=='pointer': snapshot['source']['json_pointer']='/cases/999'
                if field=='cutoff': snapshot['observed_at']=snapshot['occurred_at']='2026-09-26T23:41:38Z'
                if field=='timeline': candidate['events'][1]['payload']['statement']='Altered source statement'
                if field=='adjudication': next(e for e in candidate['events'] if e['kind']=='adjudication')['payload']['frozen_alignment']='supported'
                if field=='outcome': next(e for e in candidate['events'] if e['kind']=='outcome')['payload']['issue_state']='open'
                with self.assertRaises(ValidationError): extend(self.before,candidate,ROOT)

    def test_report_shows_qualifiers_and_separates_two_status_axes(self):
        report=render(self.journal)
        for text in ('Source status','Source evidence basis','research\\_snapshot','not\\_claimed','partial\\_pre\\_freeze','closed\\_no\\_fix','main\\_merged\\_backport\\_unresolved','Snapshot diff','Literal report signals','Misses / noise'):
            self.assertIn(text,report)
        self.assertNotIn('Pending source import.',report)
        self.assertNotIn('Pending source import.',render(self.journal,self.recorded))
        self.assertIn('Pending source import.',render(self.journal,self.study['as_of_utc']))

    def test_docx_recovery_is_reproducible_and_preserves_original_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'recovered'
            recovered=extract(SOURCES/'adjudication-original.docx',SOURCES/'research-original.docx',out)
            self.assertEqual(recovered,self.study)
            for name in ('adjudication-original.docx','research-original.docx','adjudication-recovered.json','research-recovered.md'):
                self.assertEqual((out/name).read_bytes(),(SOURCES/name).read_bytes())
            with self.assertRaises(ValueError): extract(SOURCES/'adjudication-original.docx',SOURCES/'research-original.docx',out)
        audit=read(SOURCES/'extraction-audit.json')
        for document in audit['documents']:
            self.assertEqual(digest((SOURCES/document['file']).read_bytes()),document['sha256'])
            self.assertEqual(blocks(SOURCES/document['file']),document['blocks'])
        self.assertEqual(sum(b['kind']=='table' for b in audit['documents'][1]['blocks']),12)

    def test_research_report_and_source_json_cover_the_same_five_dimensions(self):
        research=(SOURCES/'research-recovered.md').read_text()
        for case in self.study['cases']:
            self.assertIn(case['issue_url'],research)
            for dimension in DIMENSIONS:
                self.assertIn(case['dimensions'][dimension]['assessment'],research)

    def test_source_json_duplicate_keys_and_nonfinite_rejected(self):
        for content in ('{"a":1,"a":2}','{"a":NaN}'):
            with self.assertRaises(ValueError): source_loads(content)


if __name__=='__main__': unittest.main()
