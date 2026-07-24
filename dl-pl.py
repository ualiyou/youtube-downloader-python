import argparse
import os

import yt_dlp


DEFAULT_URL = "https://www.youtube.com/playlist?list=PL1PqvM2UQiMoGNTaxFMSK2cih633lpFKP"


def positive_int(value):
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be a positive number")
    return value


parser = argparse.ArgumentParser(description="Download a YouTube playlist.")
parser.add_argument("url", nargs="?", default=DEFAULT_URL, help="playlist URL")
parser.add_argument("--quality", type=positive_int, default=720, help="preferred minimum height (default: 720)")
parser.add_argument("--sub-lang", default="en.*", help="comma-separated subtitle languages")
parser.add_argument("--output", default="downloads", help="output directory (default: downloads)")
parser.add_argument("--audio-only", action="store_true", help="download audio as MP3 instead of video")
parser.add_argument("--cookies-from-browser", default="chrome", help="browser for cookies; use 'none' to disable (default: chrome)")
args = parser.parse_args()

os.makedirs(args.output, exist_ok=True)
subtitles = [language.strip() for language in args.sub_lang.split(",") if language.strip()]
postprocessors = (
    [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}]
    if args.audio_only
    else [
        {"key": "FFmpegSubtitlesConvertor", "format": "srt"},
        {"key": "FFmpegEmbedSubtitle"},
    ]
)

ydl_opts = {
    "outtmpl": f"{args.output}/%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s",
    "format": "bestaudio/best" if args.audio_only else f"bestvideo[height>={args.quality}]+bestaudio/bestvideo+bestaudio/best",
    "format_sort": ["res", "fps", "vcodec:h264", "acodec"],
    "merge_output_format": "mp4",
    "writesubtitles": not args.audio_only,
    "writeautomaticsub": not args.audio_only,
    "subtitleslangs": subtitles,
    "subtitlesformat": "srt/best",
    "postprocessors": postprocessors,
    "noplaylist": False,
    "playlist_items": None,
    "ignoreerrors": True,
    "download_archive": os.path.join(args.output, "archive.txt"),
    "extractor_args": {"youtube": {"player_client": ["web_safari", "mweb"]}},
    "retries": 5,
}

if args.cookies_from_browser.lower() != "none":
    ydl_opts["cookiesfrombrowser"] = (args.cookies_from_browser,)

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])
except Exception as error:
    print("❌", error)
