import os

import yt_dlp

url = "https://www.youtube.com/watch?v=fgrXAeNj9tM"

os.makedirs("downloads", exist_ok=True)

ydl_opts = {
    # "cookiesfrombrowser": ("chrome",),

    "outtmpl": "downloads/%(title)s.%(ext)s",
    "format": "bestvideo[height>=720]+bestaudio/bestvideo+bestaudio/best",
    "format_sort": ["res", "fps", "vcodec:h264", "acodec"],
    "merge_output_format": "mp4",

    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["en", "en-orig"],
    "subtitlesformat": "srt/best",
    "postprocessors": [
        {"key": "FFmpegSubtitlesConvertor", "format": "srt"},
        {"key": "FFmpegEmbedSubtitle"},
    ],

    "noplaylist": True,

    "extractor_args": {
        "youtube": {
            "player_client": ["web_safari", "mweb"]
        }
    },

    "retries": 5,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        print("Title:", info["title"])
        print("Formats:", len(info.get("formats", [])))
        subs = list(info.get("subtitles", {}).keys())
        auto = list(info.get("automatic_captions", {}).keys())
        print("Manual subs:", subs[:10])
        print("Auto subs available:", "yes" if auto else "no")

        ydl.download([url])

except Exception as e:
    print("❌", e)
