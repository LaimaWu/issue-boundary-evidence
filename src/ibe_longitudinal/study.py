"""Lossless import of source study schema 1.0; no keyword judgment or scoring."""
from copy import deepcopy

from .validation import DIMENSIONS, require, timestamp


def prepare(data, study, source_id, batch_id, recorded_at, artifacts=()):
    """Build a reviewable append batch; actual source labels remain separate.

    All supplied source cases have explicit open research questions. Sources
    without those questions need a separately authored outcome, never auto-final.
    """
    require(study.get('schema_version') == '1.0', 'unsupported source schema')
    require(study['evaluation_release']['tag'] == data['frozen_release'], 'source release differs from freeze')
    registry = {a['id']:a for a in [*data['artifacts'], *artifacts]}
    require(source_id in registry and registry[source_id]['kind'] == 'research_dataset', 'source dataset artifact required')
    require(any(a['kind'] == 'freeze_archive' and a['sha256'] == study['freeze']['archive_sha256'] for a in registry.values()), 'source freeze archive hash mismatch')
    require(timestamp(recorded_at) >= timestamp(study['as_of_utc']), 'cannot backdate import before source observation')
    cases = {c['issue_url']:c for c in data['cases']}
    require(len(study['cases']) == len(cases) and {c['issue_url'] for c in study['cases']} == set(cases), 'source case set differs from frozen journal')
    require(not any(e['id'].startswith(batch_id+':') for e in data['events']), 'batch already imported')
    latest = {}
    for e in data['events']:
        if e['kind'] != 'evidence': latest[(e['case_id'], e['payload'].get('dimension', 'outcome'))] = e['id']
    result = {'artifacts':deepcopy(list(artifacts)), 'events':[]}
    observed = study['as_of_utc']
    for index, original in enumerate(study['cases']):
        case = cases[original['issue_url']]
        frozen = original['frozen_artifact']
        require(frozen['snapshot_completed_utc'] == case['frozen_at'], 'source freeze timestamp mismatch')
        require(frozen['report_sha256'] == registry[case['report_artifact_id']]['sha256'], 'source frozen report hash mismatch')
        require(frozen['report_path_in_archive'] == registry[case['report_artifact_id']]['path'].replace('frozen/', 'cases/', 1), 'source frozen report path mismatch')
        require(set(original['dimensions']) == set(DIMENSIONS) == set(original['frozen_report_adjudication']['dimension_alignment']), 'source must contain all five dimensions')
        require(original['unresolved'], 'source without open questions needs explicit outcome review')
        prefix = batch_id+':'+case['id']
        pointer = '/cases/'+str(index)
        def add(suffix, kind, payload):
            event = {'id':prefix+':'+suffix,'case_id':case['id'],'recorded_at':recorded_at,'actor':'source-study import (no new adjudication)','kind':kind,'payload':payload}
            result['events'].append(event)
            return event['id']
        def evidence(suffix, record, at, scope, statement, basis, url, locator, kind, original_kind):
            return add(suffix,'evidence',{'kind':kind,'source_kind':original_kind,'occurred_at':at,'observed_at':observed,'temporal_scope':scope,'epistemic_status':basis,'statement':statement,'source_record':deepcopy(record),'source':{'url':url,'locator':locator,'json_pointer':locator,'excerpt':statement,'author':'Not named in supplied research; attribution retained from source','author_role':'maintainer' if basis=='maintainer_confirmed_fact' else 'researcher','artifact_id':source_id,'origin':'research_summary'}})
        snapshot = evidence('snapshot',original,observed,'research_snapshot',original['freeze_context'],'observed_fact',case['issue_url'],pointer,'research_snapshot','case_state_as_of')
        refs = [snapshot]
        for number, item in enumerate(original['evidence_timeline']):
            refs.append(evidence('timeline-'+str(number+1),item,item['at_utc'],'post_freeze' if timestamp(item['at_utc']) > timestamp(case['frozen_at']) else 'pre_freeze_context',item['statement'],item['evidence_type'],item['url'],pointer+'/evidence_timeline/'+str(number),'observation',item['kind']))
        # Date-bearing PR/release transitions are separate from their state at cutoff.
        for field, kind in (('linked_prs','pull_request'),('release_and_backport','release')):
            for number,item in enumerate(original[field]):
                for time_field in ('opened_utc','merged_utc','closed_utc','published_utc'):
                    if time_field in item:
                        at=item[time_field]
                        refs.append(evidence(field+'-'+str(number+1)+'-'+time_field,item,at,'post_freeze' if timestamp(at)>timestamp(case['frozen_at']) else 'pre_freeze_context',f"Source records {time_field}={at}. Other fields describe state at study cutoff.",'observed_fact',item['url'],pointer+'/'+field+'/'+str(number),kind,time_field))
        alignment = original['frozen_report_adjudication']
        dims = {}
        for dimension in DIMENSIONS:
            assessment = original['dimensions'][dimension]
            dims[dimension] = add('dimension-'+dimension,'adjudication',{'dimension':dimension,'verdict':'source_recorded','epistemic_status':alignment['researcher_assessment_type'],'frozen_claim':alignment['summary'],'rationale':assessment['assessment'],'evidence_ids':refs,'unresolved_questions':[],'supersedes':latest.get((case['id'],dimension)),'source_assessment':deepcopy(assessment),'frozen_alignment':alignment['dimension_alignment'][dimension],'source_pointer':{'artifact_id':source_id,'pointer':pointer}})
        add('outcome','outcome',{'status':'unresolved','issue_state':original['issue_state_as_of'],'resolution':'unknown','source_disposition':original['dimensions']['fix_trajectory']['status'],'rationale':original['dimensions']['fix_trajectory']['assessment'],'evidence_ids':refs,'dimension_ids':dims,'unresolved_questions':deepcopy(original['unresolved']),'supersedes':latest.get((case['id'],'outcome'))})
    return result
