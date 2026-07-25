# YouTube Playlist Archiver

<p align="center">
  Local, resumable MP4/MP3 downloads for YouTube videos and playlists, with subtitle support. Powered by <a href="https://github.com/yt-dlp/yt-dlp">yt-dlp</a>.
</p>

<p align="center">
  <a href="https://github.com/ualiyou/youtube-downloader-python/actions/workflows/ci.yml"><img src="https://github.com/ualiyou/youtube-downloader-python/actions/workflows/ci.yml/badge.svg" alt="CI status"></a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python 3.9+">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT license"></a>
</p>

> Download only content you are allowed to download and follow the platform's Terms of Service.

## Why use this?

- Download a single video or resume a playlist without redownloading completed items.
- Save MP4 video, MP3 audio, and English subtitles locally.
- Keep control of credentials: browser cookies are **off by default** and must be explicitly requested.

This is a small local CLI, not a replacement for yt-dlp. It focuses on repeatable video and playlist archives.

## Install

You need Python 3.9+ and [FFmpeg](https://ffmpeg.org/) (for merging media, MP3, and subtitles).

```bash
git clone https://github.com/ualiyou/youtube-downloader-python.git
cd youtube-downloader-python
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install .
```

Install FFmpeg with `brew install ffmpeg` (macOS), `sudo apt install ffmpeg` (Ubuntu/Debian), or `winget install Gyan.FFmpeg` (Windows).

## Quick start

```bash
# Download one video, preferring 720p or better, with English subtitles
yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID"

# Download a playlist; completed items are tracked in downloads/archive.txt
yt-archive playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Save audio only as MP3
yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only
```

## Usage examples

Replace `VIDEO_ID` and `PLAYLIST_ID` with your own public YouTube URLs. Keep URLs in quotes, especially when they contain `&`.

| Goal | Command |
| --- | --- |
| Download a video with the defaults | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID"` |
| Prefer 1080p or higher | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --min-height 1080` |
| Download to a specific folder | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --output videos` |
| Download MP3 audio only | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only` |
| Download an MP3 to a specific folder | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only --output music` |
| Download Persian and English subtitles | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --sub-langs fa,en` |
| Download a playlist and resume later | `yt-archive playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID"` |
| Prefer 720p for every playlist item | `yt-archive playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" --min-height 720` |
| Use local Chrome cookies only when login is required | `yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" --cookies-from-browser chrome` |

### Copy-paste commands

```bash
# 1. A normal video download. Files go to downloads/.
yt-archive video "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 2. A higher-resolution video with Persian and English subtitles.
yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --min-height 1080 \
  --sub-langs fa,en \
  --output downloads/tutorials

# 3. Extract audio as MP3; subtitle processing is skipped for audio-only mode.
yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --audio-only \
  --output music

# 4. Archive a course playlist. Re-running this command skips finished items.
yt-archive playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --min-height 720 \
  --sub-langs en,en-orig \
  --output archives

# 5. Use cookies only for a video that requires your signed-in browser session.
yt-archive video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --cookies-from-browser chrome
```

On Windows PowerShell, the same `yt-archive` commands work after activating `.venv`. If you prefer the original scripts, these remain supported:

```powershell
py dl.py "https://www.youtube.com/watch?v=VIDEO_ID"
py dl-pl.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --output archives
```

### Output layout

```text
downloads/
├── Video title.mp4
├── Video title.en.srt
├── archive.txt
└── Playlist title/
    ├── 01 - First lesson.mp4
    └── 01 - First lesson.en.srt
```

## Options

| Option | Meaning |
| --- | --- |
| `video URL` | Download exactly one video. |
| `playlist URL` | Download every available item in a playlist and record completed items. |
| `--min-height HEIGHT` | Prefer the best available format at least this tall; `--quality` remains an alias. This is a minimum, not a maximum or exact resolution. |
| `--sub-langs LANGS` | Comma-separated subtitle languages to download and embed, such as `en,en-orig` or `fa,en`. |
| `--output DIRECTORY` | Output directory; defaults to `downloads`. |
| `--audio-only` | Extract MP3 instead of downloading video. |
| `--cookies-from-browser BROWSER` | Explicitly opt in to local browser cookies when a video requires login, for example `chrome`, `firefox`, or `edge`. Omit this option for public videos. |

Playlist files are stored under a playlist-named folder and use `downloads/archive.txt` to skip completed entries.

## Privacy and troubleshooting

- The CLI never reads browser cookies unless `--cookies-from-browser` is supplied.
- Some videos require login, may be unavailable in your region, or may not have subtitles.
- If merging or subtitles fail, confirm `ffmpeg -version` works in the same terminal.
- Keep yt-dlp current by reinstalling this project when upstream YouTube changes affect downloads.

## Development

```bash
python -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance and [CHANGELOG.md](CHANGELOG.md) for releases.

## Roadmap

- [ ] Write a download manifest with source metadata and completion status.
- [ ] Add a dry-run mode and clearer per-item failure summary.
- [ ] Publish the stable CLI to PyPI.
