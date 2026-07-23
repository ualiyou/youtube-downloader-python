# yt-dl

دانلود ویدیوهای YouTube با `yt-dlp`، به‌همراه زیرنویس انگلیسی. `dl.py` برای یک ویدیو و `dl-pl.py` برای پلی‌لیست است.

## نصب Python

Python 3 را از [python.org/downloads](https://www.python.org/downloads/) نصب کنید و سپس از ریشهٔ پروژه این دستورها را اجرا کنید:

```bash
python3 -m pip install -U yt-dlp
```

برای ادغام ویدیو، صدا و زیرنویس، FFmpeg نیز لازم است:

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### ویندوز

هنگام نصب Python گزینهٔ **Add Python to PATH** را فعال کنید. سپس در PowerShell، از ریشهٔ پروژه اجرا کنید:

```powershell
py -m pip install -U yt-dlp
winget install Gyan.FFmpeg
```

برای اجرای POT provider با Docker در ویندوز، ابتدا [Docker Desktop](https://www.docker.com/products/docker-desktop/) را نصب و اجرا کنید؛ سپس همان دستور Docker بخش بعدی را در PowerShell اجرا کنید.

## POT provider (اختیاری)

برای راه‌اندازی با Docker:

```bash
docker run -d --name bgutil-pot --restart unless-stopped -p 4416:4416 brainicism/bgutil-ytdlp-pot-provider
```

یا برای نصب با Python:

```bash
python3 -m pip install -U bgutil-ytdlp-pot-provider
```

## اجرا

ابتدا مقدار `url` را در اسکریپت موردنظر تغییر دهید، سپس اجرا کنید:

```bash
# یک ویدیو
python3 dl.py

# یک پلی‌لیست
python3 dl-pl.py
```

در ویندوز از این دستورها استفاده کنید:

```powershell
# یک ویدیو
py dl.py

# یک پلی‌لیست
py dl-pl.py
```

فایل‌های خروجی در پوشهٔ `downloads/` ذخیره می‌شوند.
