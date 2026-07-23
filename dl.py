import argparse
import os

import yt_dlp


DEFAULT_URL = "https://www.youtube.com/watch?v=y_bsjZThP0o&pp=ygUYdHJhZGluZyB3aXRoIGNsYXVkZSBjb2Rl"


def positive_int(value):
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be a positive number")
    return value


parser = argparse.ArgumentParser(description="Download one YouTube video.")
parser.add_argument("url", nargs="?", default=DEFAULT_URL, help="video URL")
parser.add_argument("--quality", type=positive_int, default=720, help="preferred minimum height (default: 720)")
parser.add_argument("--sub-lang", default="en,en-orig", help="comma-separated subtitle languages")
parser.add_argument("--output", default="downloads", help="output directory (default: downloads)")
parser.add_argument("--audio-only", action="store_true", help="download audio as MP3 instead of video")
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
    "outtmpl": f"{args.output}/%(title)s.%(ext)s",
    "format": "bestaudio/best" if args.audio_only else f"bestvideo[height>={args.quality}]+bestaudio/bestvideo+bestaudio/best",
    "format_sort": ["res", "fps", "vcodec:h264", "acodec"],
    "merge_output_format": "mp4",
    "writesubtitles": not args.audio_only,
    "writeautomaticsub": not args.audio_only,
    "subtitleslangs": subtitles,
    "subtitlesformat": "srt/best",
    "postprocessors": postprocessors,
    "noplaylist": True,
    "extractor_args": {"youtube": {"player_client": ["web_safari", "mweb"]}},
    "retries": 5,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(args.url, download=False)
        print("Title:", info["title"])
        print("Formats:", len(info.get("formats", [])))
        print("Manual subs:", list(info.get("subtitles", {}).keys())[:10])
        print("Auto subs available:", "yes" if info.get("automatic_captions") else "no")
        ydl.download([args.url])
except Exception as error:
    print("❌", error)
