"""Read the original freeze ZIP without executing its contents or editing it."""
import json
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import zipfile

from .store import encoded
from .validation import digest, require, validate


def initialize(archive, destination, dataset_id, release):
    """Verify the freeze manifest and copy exact bytes to a new data directory."""
    archive, destination = Path(archive), Path(destination)
    require(not destination.exists(), 'destination already exists; initialize never overwrites')
    raw = archive.read_bytes()
    with zipfile.ZipFile(archive) as zipped:
        names = zipped.namelist()
        require(len(names) == len(set(names)), 'duplicate ZIP member')
        require(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in names), 'unsafe ZIP member')
        manifests = [n for n in names if n.endswith('/SHA256SUMS.txt')]
        require(len(manifests) == 1, 'expected one freeze SHA256SUMS.txt')
        manifest = manifests[0]
        prefix = manifest[:-len('SHA256SUMS.txt')]
        checked = set()
        for line in zipped.read(manifest).decode('utf-8').splitlines():
            expected, relative = line.split(maxsplit=1)
            relative = relative.removeprefix('./')
            require(not PurePosixPath(relative).is_absolute() and '..' not in PurePosixPath(relative).parts, 'unsafe manifest path')
            name = prefix + relative
            require(name not in checked, 'duplicate checksum entry')
            require(digest(zipped.read(name)) == expected, f'freeze checksum mismatch: {relative}')
            checked.add(name)
        require(checked == {n for n in names if not n.endswith('/') and n != manifest}, 'manifest does not cover all frozen files')
        data = {'schema_version':'1.0.0', 'dataset_id':dataset_id, 'frozen_release':release, 'artifacts':[], 'cases':[], 'events':[]}
        destination.parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix='.freeze-', dir=destination.parent))
        try:
            def save(aid, path, content, kind):
                target = stage / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
                data['artifacts'].append({'id':aid, 'path':path, 'sha256':digest(content), 'kind':kind})
            save('freeze-archive', 'sources/freeze.zip', raw, 'freeze_archive')
            save('freeze-checksums', 'sources/SHA256SUMS.txt', zipped.read(manifest), 'freeze_manifest')
            for name in sorted(checked):
                if '/cases/' not in name or not name.endswith('/metadata.json'):
                    continue
                meta = json.loads(zipped.read(name))
                case_id = PurePosixPath(name).parent.name
                report_name = str(PurePosixPath(name).with_name('report.md'))
                require(report_name in checked, f'missing frozen report: {case_id}')
                save(case_id+'-report', f'frozen/{case_id}/report.md', zipped.read(report_name), 'frozen_report')
                save(case_id+'-metadata', f'frozen/{case_id}/metadata.json', zipped.read(name), 'frozen_metadata')
                data['cases'].append({'id':case_id, 'issue_url':meta['issue_url'], 'frozen_at':meta['snapshot_completed_utc'], 'report_artifact_id':case_id+'-report', 'metadata_artifact_id':case_id+'-metadata'})
            validate(data, stage)
            (stage / 'journal.json').write_bytes(encoded(data))
            stage.rename(destination)
        finally:
            if stage.exists():
                shutil.rmtree(stage)
    return data, len(checked)
