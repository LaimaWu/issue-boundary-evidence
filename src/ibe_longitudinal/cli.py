"""A separate CLI. Never invokes or imports the IBE extraction engine."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys
import zipfile

from .freeze import initialize
from .report import render
from .store import append, read, encoded, extend
from .docx_source import extract
from .study import prepare
from .validation import ValidationError, digest, timestamp, validate


def main(argv=None):
    parser = argparse.ArgumentParser(description='Independent IBE longitudinal research journal')
    commands = parser.add_subparsers(dest='command', required=True)
    init = commands.add_parser('init-freeze', help='Verify original freeze ZIP and create a new journal')
    init.add_argument('archive', type=Path)
    init.add_argument('directory', type=Path)
    init.add_argument('--dataset-id', required=True)
    init.add_argument('--release', required=True)
    docx = commands.add_parser('extract-docx', help='Recover study JSON and research Markdown from transfer documents')
    docx.add_argument('adjudication', type=Path)
    docx.add_argument('research', type=Path)
    docx.add_argument('directory', type=Path)
    study = commands.add_parser('prepare-study', help='Build and validate a lossless source-study append batch')
    study.add_argument('journal', type=Path)
    study.add_argument('source', type=Path)
    study.add_argument('--source-id', required=True)
    study.add_argument('--batch-id', required=True)
    study.add_argument('--artifacts', required=True, type=Path, help='JSON array of new pinned source artifacts')
    study.add_argument('--recorded-at', default=None, help='Actual import time; defaults to current UTC')
    study.add_argument('--output', required=True, type=Path)
    check = commands.add_parser('validate', help='Check schema, history, provenance, times and artifact bytes')
    check.add_argument('journal', type=Path)
    check.add_argument('--previous', type=Path, help='Prior journal to enforce immutable historical prefixes')
    add = commands.add_parser('append', help='Append a reviewed batch atomically')
    add.add_argument('journal', type=Path)
    add.add_argument('batch', type=Path)
    add.add_argument('--expected-sha256', required=True, help='Journal digest returned by validate')
    report = commands.add_parser('report', help='Render validated research history without inference')
    report.add_argument('journal', type=Path)
    report.add_argument('--output', required=True, type=Path, help='New output file; will not overwrite an existing file')
    report.add_argument('--as-of', help='UTC timestamp ending in Z; filter by recorded_at')
    args = parser.parse_args(argv)
    try:
        if args.command == 'extract-docx':
            extract(args.adjudication, args.research, args.directory)
            print(f'Sources extracted: {args.directory}')
        elif args.command == 'prepare-study':
            current = read(args.journal)
            batch = prepare(current, read(args.source), args.source_id, args.batch_id,
                            args.recorded_at or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), read(args.artifacts))
            extend(current, batch, args.journal.parent)
            with args.output.open('xb') as handle:
                handle.write(encoded(batch))
            print(f"Prepared {len(batch['events'])} events; journal unchanged.")
        elif args.command == 'init-freeze':
            data, count = initialize(args.archive, args.directory, args.dataset_id, args.release)
            print(f"Verified {count} frozen checksums; initialized {len(data['cases'])} cases; no adjudications inferred.")
        elif args.command == 'append':
            result = append(args.journal, read(args.batch), args.expected_sha256)
            print(f"Appended successfully; {len(result['events'])} total events.")
        else:
            data = read(args.journal)
            previous = read(args.previous) if args.command == 'validate' and args.previous else None
            validate(data, args.journal.parent, previous)
            if args.command == 'validate':
                print(f"Valid: {len(data['cases'])} cases, {len(data['events'])} events, {len(data['artifacts'])} verified artifacts")
                print(f"sha256: {digest(args.journal.read_bytes())}")
            else:
                if args.as_of:
                    if not args.as_of.endswith('Z'):
                        raise ValidationError('--as-of must be an explicit UTC timestamp ending in Z')
                    timestamp(args.as_of)
                content = render(data, args.as_of)
                # Exclusive creation prevents overwriting a source, journal or frozen report.
                with args.output.open('x', encoding='utf-8') as handle:
                    handle.write(content)
                print(f"Report written: {args.output}")
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as exc:
        print(f'longitudinal: {exc}', file=sys.stderr)
        return 2
    return 0
