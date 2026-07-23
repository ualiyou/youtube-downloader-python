# 🎬 YouTube Downloader

<p align="center">
  Simple Python scripts for downloading YouTube videos and playlists in high quality with English subtitles.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/yt--dlp-powered-FF0000?logo=youtube&logoColor=white" alt="Powered by yt-dlp">
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-555555" alt="Cross-platform">
</p>

> ⚠️ Download only content you are allowed to download, and follow YouTube's Terms of Service.

## ✨ Features

- 🎥 Download a single video or a complete playlist
- 🎞️ Prefer the best available MP4 quality (minimum 720p by default)
- 💬 Download and embed English subtitles
- 🔁 Retry failed downloads automatically
- 🗂️ Skip previously downloaded playlist items with an archive

## 🚀 Quick Start

```bash
python3 -m pip install -r requirements.txt
python3 dl.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

The scripts keep their previous built-in URLs when no URL is provided.

## 📦 Requirements

| Tool | Purpose |
| --- | --- |
| Python 3 | Runs the scripts |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Downloads content |
| FFmpeg | Merges video, audio, and subtitles |

### macOS

```bash
# Install Python from https://www.python.org/downloads/ if needed
python3 -m pip install -U yt-dlp
brew install ffmpeg
```

### Ubuntu / Debian

```bash
python3 -m pip install -U yt-dlp
sudo apt install ffmpeg
```

### 🪟 Windows

Install Python from [python.org/downloads](https://www.python.org/downloads/) and enable **Add Python to PATH**. Then run this from the project folder in PowerShell:

```powershell
py -m pip install -U yt-dlp
winget install Gyan.FFmpeg
```

## ▶️ Usage

| Command | Use case | Main settings |
| --- | --- | --- |
| `python3 dl.py URL` | Download one video | Minimum 720p; `en` and `en-orig` subtitles |
| `python3 dl-pl.py URL` | Download a playlist | Minimum 720p; English subtitles; Chrome cookies |

On Windows, use `py` instead of `python3`:

```powershell
py dl.py      # One video
py dl-pl.py   # Playlist
```

Downloads are saved in `downloads/`. Playlist downloads are grouped in a folder named after the playlist.

### Copy-paste Examples

```bash
# Download one video
python3 dl.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download one video at 1080p with English subtitles
python3 dl.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --quality 1080 --sub-lang en

# Download audio only as MP3
python3 dl.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --audio-only

# Download a playlist
python3 dl-pl.py "https://www.youtube.com/playlist?list=PL1PqvM2UQiMoGNTaxFMSK2cih633lpFKP"
```

### Options

```bash
python3 dl.py URL --quality 1080 --sub-lang en --output videos
python3 dl.py URL --audio-only
python3 dl-pl.py URL --cookies-from-browser none
```

`--quality`, `--sub-lang`, and `--output` are available in both scripts. `--audio-only` saves MP3 files and skips subtitle embedding. Playlist downloads use Chrome cookies by default; pass `--cookies-from-browser none` to disable them.

## 🧩 Optional POT Provider

Run the provider with Docker:

```bash
docker run -d --name bgutil-pot --restart unless-stopped -p 4416:4416 brainicism/bgutil-ytdlp-pot-provider
```

Or install it with Python:

```bash
python3 -m pip install -U bgutil-ytdlp-pot-provider
```

On Windows, install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/) before running the Docker command in PowerShell.

> ℹ️ Installing the provider does not configure `yt-dlp` automatically. Connect it in the script configuration if you need to use it.

## 📁 Project Structure

```text
.
├── dl.py       # Download one video
├── dl-pl.py    # Download a playlist
├── requirements.txt
├── LICENSE
└── downloads/  # Output files (ignored by Git)
```

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a pull request.
