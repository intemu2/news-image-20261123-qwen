"""news-image-20261123 hybrid: copy the pre-rendered entry image.

Stdlib only. No network. Deterministic: the output bytes are exactly
the bytes of entry.png in this repository.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Self-check: read the file back and confirm it holds exactly the image.
    with open(dst, "rb") as f:
        written = f.read()
    with open(src, "rb") as f:
        expected = f.read()
    if written != expected:
        raise SystemExit("entry.png does not match the repository image")


if __name__ == "__main__":
    main()
