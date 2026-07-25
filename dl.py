"""Backward-compatible entry point for downloading one video."""

import sys

from youtube_downloader import main


if __name__ == "__main__":
    raise SystemExit(main(["video", *sys.argv[1:]]))
