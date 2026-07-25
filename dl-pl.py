"""Backward-compatible entry point for downloading one playlist."""

import sys

from youtube_downloader import main


if __name__ == "__main__":
    raise SystemExit(main(["playlist", *sys.argv[1:]]))
