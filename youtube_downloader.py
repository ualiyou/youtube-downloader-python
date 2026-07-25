"""A small, local command-line interface around yt-dlp."""

import argparse
import sys
from pathlib import Path

import yt_dlp


def positive_int(value):
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be a positive number")
    return value


def add_download_options(parser):
    parser.add_argument("url", help="YouTube video or playlist URL")
    parser.add_argument(
        "--min-height",
        "--quality",
        dest="min_height",
        type=positive_int,
        default=720,
        help="minimum preferred video height (default: 720)",
    )
    parser.add_argument(
        "--sub-langs",
        "--sub-lang",
        dest="sub_langs",
        default="en,en-orig",
        help="comma-separated subtitle languages (default: en,en-orig)",
    )
    parser.add_argument("--output", default="downloads", help="output directory (default: downloads)")
    parser.add_argument("--audio-only", action="store_true", help="download audio as MP3")
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="opt in to cookies from a browser, for example: chrome",
    )


def make_parser():
    parser = argparse.ArgumentParser(
        prog="yt-archive",
        description="Download YouTube videos and playlists locally with yt-dlp.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    add_download_options(subparsers.add_parser("video", help="download one video"))
    add_download_options(subparsers.add_parser("playlist", help="download a playlist"))
    return parser


def build_options(args):
    output = Path(args.output)
    subtitles = [language.strip() for language in args.sub_langs.split(",") if language.strip()]
    playlist = args.command == "playlist"
    options = {
        "outtmpl": str(output / ("%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s" if playlist else "%(title)s.%(ext)s")),
        "format": "bestaudio/best" if args.audio_only else f"bestvideo[height>={args.min_height}]+bestaudio/bestvideo+bestaudio/best",
        "format_sort": ["res", "fps", "vcodec:h264", "acodec"],
        "merge_output_format": "mp4",
        "writesubtitles": not args.audio_only,
        "writeautomaticsub": not args.audio_only,
        "subtitleslangs": subtitles,
        "subtitlesformat": "srt/best",
        "postprocessors": ([{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}] if args.audio_only else [{"key": "FFmpegSubtitlesConvertor", "format": "srt"}, {"key": "FFmpegEmbedSubtitle"}]),
        "noplaylist": not playlist,
        "retries": 5,
        "extractor_args": {"youtube": {"player_client": ["mweb"] if playlist else ["web_safari", "mweb"]}},
    }
    if playlist:
        options.update(ignoreerrors=True, download_archive=str(output / "archive.txt"))
    if args.cookies_from_browser:
        options["cookiesfrombrowser"] = (args.cookies_from_browser,)
    return options


def main(argv=None):
    parser = make_parser()
    args = parser.parse_args(argv)
    Path(args.output).mkdir(parents=True, exist_ok=True)
    try:
        with yt_dlp.YoutubeDL(build_options(args)) as downloader:
            downloader.download([args.url])
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
