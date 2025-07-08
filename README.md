# 🎵 Lite Discord Music Bot

A lightweight music bot for Discord that supports YouTube playback using `yt-dlp` and `ffmpeg`.

## 🛠 Features

- `/play` – Play music from YouTube  
- `/skip` – Skip current track and play the next one (disconnects if queue is empty)  
- `/queue` – Show the current queue

## ⚙️ Requirements

- Python 3.10+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases)
- [ffmpeg](https://www.gyan.dev/ffmpeg/builds/)
- Discord bot token
- Anything libraries from "requirements.txt"

## 📦 Installation

1. **Download "main.py" and "requirements.txt" from this repo:**

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install yt-dlp (Windows 11):**

Download yt-dlp.exe: [yt-dlp latest](https://github.com/yt-dlp/yt-dlp/releases)

Save it in a convenient folder (e.g., C:\yt-dlp)

Add the folder to your system PATH:

Search for "Environment Variables"

Go to Advanced > Environment Variables

Under System Variables, edit Path, add new, and paste the path to your yt-dlp.exe

4. **Install ffmpeg:**

Go to [FFmpeg downloads](https://www.gyan.dev/ffmpeg/builds/#release-builds)

Download ffmpeg-release-essentials.zip

Extract it and locate the bin\ffmpeg.exe file

Add the bin folder (e.g., C:\ffmpeg\bin) to your system PATH

Test it in CMD:
```bash
yt-dlp --version
ffmpeg -version
```
5. **Set up environment variables:**
Create a .env file in the project folder:
```bash
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```
Get your token from: [Discord Developer Portal](https://discord.com/developers/applications)

## 🧪Usage

Launch the bot:
```bash
python main.py
```
Use the following commands in your Discord server:
/play <url> — Plays a YouTube track

/skip — Skips to the next song in queue

/queue — Displays the current music queue

## 💡Notes

**This bot is designed to be simple and fast to set up.**

You can always improve it by adding:

Loop/repeat

Pause/resume

Volume control

Web dashboard

*Created by @kashanqq
Don’t forget to ⭐ this repo if it helped you!*
