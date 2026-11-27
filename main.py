#!/usr/bin/env python3
"""news-image-20261127-v6: copy the pre-rendered entry.png to the output dir.

Standard library only. The entry image is rendered ahead of time and shipped
in this repository as entry.png; this program only places a byte-exact copy
at <output-dir>/entry.png. The output directory is taken from argv[1], then
from $MAKEFUN_OUTPUT_DIR, then from /output. The copy is verified by comparing
SHA-256 digests of the source and the destination.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def _digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _output_dir(argv):
    if len(argv) > 1 and argv[1]:
        return Path(argv[1])
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    return Path("/output")


def main(argv):
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1

    dest_dir = _output_dir(argv)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"

    with open(source, "rb") as f:
        signature = f.read(8)
    if signature != b"\x89PNG\r\n\x1a\n":
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    with open(source, "rb") as f:
        header = f.read(24)
    if len(header) < 24 or header[12:16] != b"IHDR":
        print("error: entry.png has no IHDR chunk", file=sys.stderr)
        return 1
    if int.from_bytes(header[16:20], "big") != 1024 or int.from_bytes(header[20:24], "big") != 1024:
        print("error: entry.png is not 1024x1024", file=sys.stderr)
        return 1

    if source.stat().st_size > 1048576:
        print("error: entry.png exceeds the 1048576-byte size cap", file=sys.stderr)
        return 1

    shutil.copyfile(source, dest)

    if dest.stat().st_size != source.stat().st_size:
        print("error: copied file size differs from source", file=sys.stderr)
        return 1
    if _digest(source) != _digest(dest):
        print("error: copied file digest differs from source", file=sys.stderr)
        return 1
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
