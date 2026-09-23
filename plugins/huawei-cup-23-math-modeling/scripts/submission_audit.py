#!/usr/bin/env python3
"""Local, non-uploading audit for a Huawei Cup 23 PDF submission package."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf', type=Path)
    ap.add_argument('--question', choices=list('ABCDEF'), required=True)
    ap.add_argument('--team', required=True)
    ap.add_argument('--attachment', type=Path)
    ap.add_argument('--out', type=Path)
    args = ap.parse_args()
    pdf = args.pdf
    checks = []
    def check(name, ok, detail): checks.append({'name': name, 'ok': bool(ok), 'detail': detail})
    check('exists', pdf.is_file(), str(pdf))
    check('pdf_extension', pdf.suffix.lower() == '.pdf', pdf.suffix)
    expected = f'{args.question}{args.team}.pdf'
    check('filename', pdf.name == expected, f'expected {expected}, got {pdf.name}')
    if pdf.is_file():
        check('nonempty', pdf.stat().st_size > 0, f'{pdf.stat().st_size} bytes')
        check('pdf_signature', pdf.read_bytes()[:5] == b'%PDF-', 'first five bytes')
        digest_md5, digest_sha = md5(pdf), sha256(pdf)
    else:
        digest_md5 = digest_sha = None
    if args.attachment:
        check('attachment_exists', args.attachment.is_file(), str(args.attachment))
        if args.attachment.is_file():
            check('attachment_size', args.attachment.stat().st_size <= 50 * 1024 * 1024, f'{args.attachment.stat().st_size} bytes')
            check('attachment_stem', args.attachment.stem == pdf.stem, f'expected {pdf.stem}')
    result = {'pdf': str(pdf.resolve()), 'expected_filename': expected, 'md5': digest_md5, 'sha256': digest_sha, 'checks': checks, 'passed': all(c['ok'] for c in checks)}
    out = args.out or pdf.with_suffix('.submission-audit.json')
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 2

if __name__ == '__main__':
    raise SystemExit(main())

