# 🎬 YouTube Downloader

<p align="center">
  اسکریپت‌های سادهٔ Python برای دانلود ویدیو و پلی‌لیست YouTube با کیفیت بالا و زیرنویس انگلیسی.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/yt--dlp-powered-FF0000?logo=youtube&logoColor=white" alt="Powered by yt-dlp">
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-555555" alt="Cross-platform">
</p>

> ⚠️ فقط محتوایی را دانلود کنید که مجاز به دانلود آن هستید و قوانین YouTube را رعایت کنید.

## ✨ امکانات

- 🎥 دانلود یک ویدیو یا پلی‌لیست کامل
- 🎞️ اولویت با بهترین کیفیت MP4 (۷۲۰p برای ویدیو، ۱۰۸۰p برای پلی‌لیست)
- 💬 دانلود و embed کردن زیرنویس انگلیسی
- 🔁 تلاش مجدد خودکار هنگام خطا
- 🗂️ جلوگیری از دانلود تکراری پلی‌لیست با archive

## 🚀 شروع سریع

```bash
python3 -m pip install -U yt-dlp
python3 dl.py
```

قبل از اجرا، مقدار `url` را در فایل اسکریپت به لینک ویدیو یا پلی‌لیست خودتان تغییر دهید.

## 📦 پیش‌نیازها

| ابزار                                      | کاربرد                     |
| ------------------------------------------ | -------------------------- |
| Python 3.9+                                | اجرای اسکریپت‌ها           |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | دانلود محتوا               |
| FFmpeg                                     | ادغام ویدیو، صدا و زیرنویس |

### macOS

```bash
# Python: https://www.python.org/downloads/
python3 -m pip install -U yt-dlp
brew install ffmpeg
```

### Ubuntu / Debian

```bash
python3 -m pip install -U yt-dlp
sudo apt install ffmpeg
```

### 🪟 Windows

Python را از [python.org/downloads](https://www.python.org/downloads/) نصب کنید و گزینهٔ **Add Python to PATH** را فعال کنید. سپس در PowerShell و از پوشهٔ پروژه اجرا کنید:

```powershell
py -m pip install -U yt-dlp
winget install Gyan.FFmpeg
```

## ▶️ اجرا

| دستور              | کاربرد          | تنظیمات اصلی                                     |
| ------------------ | --------------- | ------------------------------------------------ |
| `python3 dl.py`    | دانلود یک ویدیو | کیفیت حداقل ۷۲۰p، زیرنویس `en` و `en-orig`       |
| `python3 dl-pl.py` | دانلود پلی‌لیست | کیفیت حداقل ۱۰۸۰p، زیرنویس انگلیسی و کوکی Chrome |

در ویندوز به‌جای `python3` از `py` استفاده کنید:

```powershell
py dl.py      # یک ویدیو
py dl-pl.py   # پلی‌لیست
```

خروجی‌ها در `downloads/` ذخیره می‌شوند. پلی‌لیست‌ها در پوشه‌ای با نام همان پلی‌لیست قرار می‌گیرند.

## 🧩 POT provider (اختیاری)

برای اجرای provider با Docker:

```bash
docker run -d --name bgutil-pot --restart unless-stopped -p 4416:4416 brainicism/bgutil-ytdlp-pot-provider
```

یا برای نصب آن با Python:

```bash
python3 -m pip install -U bgutil-ytdlp-pot-provider
```

در ویندوز ابتدا [Docker Desktop](https://www.docker.com/products/docker-desktop/) را نصب و اجرا کنید، سپس دستور Docker بالا را در PowerShell بزنید.

> ℹ️ نصب provider به‌تنهایی تنظیمات `yt-dlp` را تغییر نمی‌دهد؛ در صورت نیاز باید آن را در تنظیمات اسکریپت متصل کنید.

## 📁 ساختار پروژه

```text
.
├── dl.py       # دانلود یک ویدیو
├── dl-pl.py    # دانلود پلی‌لیست
└── downloads/  # فایل‌هایی که دانلود میشن داخل این پوشه ذخیره میشن
```

## 🤝 مشارکت

ایده یا باگی دارید؟ یک Issue باز کنید یا Pull Request بفرستید.
