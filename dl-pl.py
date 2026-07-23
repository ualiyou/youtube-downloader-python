import os

import yt_dlp

url = "https://www.youtube.com/playlist?list=PL1PqvM2UQiMoGNTaxFMSK2cih633lpFKP"

os.makedirs("downloads", exist_ok=True)

ydl_opts = {
    "cookiesfrombrowser": ("chrome",),
    "outtmpl": "downloads/%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s",
    "format": "bestvideo[height>=1080]+bestaudio/bestvideo+bestaudio/best",
    "format_sort": ["res", "fps", "vcodec:h264", "acodec"],
    "merge_output_format": "mp4",
    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["en.*"],
    "subtitlesformat": "srt/best",
    "postprocessors": [
        {"key": "FFmpegSubtitlesConvertor", "format": "srt"},
        {"key": "FFmpegEmbedSubtitle"},
    ],

    "noplaylist": False,
    "playlist_items": None,
    "ignoreerrors": True,
    "download_archive": "downloads/archive.txt",

    "extractor_args": {
        "youtube": {
            "player_client": ["web_safari", "mweb"]
        }
    },

    "retries": 5,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
