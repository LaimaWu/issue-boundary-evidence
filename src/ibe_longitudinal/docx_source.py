"""Recover source text from transfer DOCX files; never modify the originals."""
import json
from pathlib import Path
import shutil
import tempfile
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from hashlib import sha256


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def loads(text):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f'duplicate source JSON key: {key}')
            result[key] = value
        return result
    def invalid(value):
        raise ValueError(f'invalid source JSON constant: {value}')
    return json.loads(text, object_pairs_hook=pairs, parse_constant=invalid)

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def paragraph_text(node):
    return ''.join((el.text or '') if el.tag == W+'t' else '\t' if el.tag == W+'tab' else '\n' if el.tag in (W+'br', W+'cr') else '' for el in node.iter())


def blocks(path):
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read('word/document.xml'))
        require(not any(root.iter(W+'ins')) and not any(root.iter(W+'del')), 'review tracked changes before importing')
        require(not any(root.iter(W+'drawing')) and not any(root.iter(W+'object')), 'embedded objects require manual source review')
        result = []
        for index, node in enumerate(root.find(W+'body')):
            if node.tag == W+'p':
                style = node.find(W+'pPr/'+W+'pStyle')
                result.append({'block':index, 'kind':'paragraph', 'style':style.get(W+'val') if style is not None else None, 'text':paragraph_text(node)})
            elif node.tag == W+'tbl':
                result.append({'block':index, 'kind':'table', 'rows':[[ '\n'.join(paragraph_text(p) for p in cell.iter(W+'p')) for cell in row.findall(W+'tc')] for row in node.findall(W+'tr')]})
            else:
                require(node.tag == W+'sectPr', 'unsupported body content requires review')
        return result


def markdown(body):
    lines = []
    for block in body:
        if block['kind'] == 'paragraph':
            style = block['style'] or ''
            prefix = '#' * int(style[-1]) + ' ' if style.startswith('Heading') and style[-1].isdigit() else '- ' if style == 'ListBullet' else ''
            lines += [prefix + block['text'], '']
        else:
            for index, row in enumerate(block['rows']):
                lines.append('| ' + ' | '.join(cell.replace('|', '\\|').replace('\n', '<br>') for cell in row) + ' |')
                if index == 0:
                    lines.append('| ' + ' | '.join('---' for _ in row) + ' |')
            lines.append('')
    return '\n'.join(lines)


def extract(adjudication, research, output):
    """Write unchanged DOCX copies, recovered JSON/Markdown and an extraction audit."""
    output = Path(output)
    require(not output.exists(), 'extraction destination exists')
    original = [Path(adjudication), Path(research)]
    document_blocks = [blocks(path) for path in original]
    require(all(b['kind'] == 'paragraph' for b in document_blocks[0]), 'JSON transfer unexpectedly contains tables')
    paragraphs = [b['text'] for b in document_blocks[0]]
    start = next((i for i,p in enumerate(paragraphs) if p.strip().startswith('{')), None)
    require(start is not None, 'no JSON object found in transfer document')
    recovered = '\n'.join(paragraphs[start:]).rstrip() + '\n'
    study = loads(recovered)
    require(study.get('schema_version') == '1.0' and isinstance(study.get('cases'), list), 'unsupported source study schema')
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.docx-source-', dir=output.parent))
    try:
        names = ['adjudication-original.docx', 'research-original.docx']
        for path, name in zip(original, names):
            (stage/name).write_bytes(path.read_bytes())
        (stage/'adjudication-recovered.json').write_text(recovered, encoding='utf-8')
        (stage/'research-recovered.md').write_text(markdown(document_blocks[1]), encoding='utf-8')
        audit = {'method':'OOXML body paragraphs/runs and tables in document order; br/cr and tab preserved. JSON wrapper excluded. Markdown presentation reconstructed; original JSON/Markdown byte identity cannot be established without those original files.', 'json_wrapper':paragraphs[:start], 'documents':[{'file':name,'original_filename':path.name,'sha256':digest(path.read_bytes()),'blocks':body} for name,path,body in zip(names,original,document_blocks)], 'derived':[{'file':name,'sha256':digest((stage/name).read_bytes())} for name in ['adjudication-recovered.json','research-recovered.md']]}
        (stage/'extraction-audit.json').write_bytes(encoded(audit))
        stage.rename(output)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    return study
