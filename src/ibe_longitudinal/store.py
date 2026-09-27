"""Append operations use a lock, optimistic digest, validation and atomic replace."""
from copy import deepcopy
import json
import os
from pathlib import Path
import tempfile

from .validation import ZERO_HASH, ValidationError, digest, event_hash, require, validate


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def loads(text):
    def invalid(value):
        raise ValidationError(f"invalid JSON constant: {value}")
    return json.loads(text, object_pairs_hook=_pairs, parse_constant=invalid)


def read(path):
    return loads(Path(path).read_text(encoding='utf-8'))


def encoded(data):
    return (json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')


def extend(data, batch, root=None):
    """Return a validated copy; caller supplies events without chain fields."""
    require(isinstance(batch, dict) and set(batch) == {'artifacts', 'events'}, 'batch requires exactly artifacts and events')
    require(isinstance(batch['artifacts'], list) and isinstance(batch['events'], list), 'batch entries must be arrays')
    require(batch['events'] or batch['artifacts'], 'empty append batch')
    validate(data, root)
    result = deepcopy(data)
    result['artifacts'].extend(deepcopy(batch['artifacts']))
    prev = data['events'][-1]['hash'] if data['events'] else ZERO_HASH
    for event in deepcopy(batch['events']):
        require(isinstance(event, dict) and 'hash' not in event and 'previous_hash' not in event, 'append input must omit chain fields')
        event['previous_hash'] = prev
        event['hash'] = event_hash(event)
        result['events'].append(event)
        prev = event['hash']
    validate(result, root, previous=data)
    return result


def append(path, batch, expected_sha256):
    path = Path(path).resolve()
    lock = path.with_name(path.name + '.lock')
    try:
        lock.mkdir()
    except FileExistsError as exc:
        raise ValidationError(f'journal is locked: {lock}; inspect owner before removing a stale lock') from exc
    temporary = None
    try:
        raw = path.read_bytes()
        require(digest(raw) == expected_sha256, 'journal changed since review; reload before appending')
        result = extend(loads(raw.decode('utf-8')), batch, path.parent)
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.journal-', delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(encoded(result))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        return result
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.rmdir()
