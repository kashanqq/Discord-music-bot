# Lite Discord-music-bot
Music-bot which support youtube for discord.

This Bot support next command: 

/play - for active bot and start your music

/skip - skip plaing track and go next one (if it has, another way bot will disconnect)

/queue - show queue of track that will play later


# You have to have yt-dlp and ffmpeg on your PC. If you don't have it, keep reading.

# How install yt-dlp for Win 11:

1. Click this https://github.com/yt-dlp/yt-dlp/releases/tag/2025.06.30 and download yt-dlp.exe in any folder on your PC (primary, in comfortable folder)
2. Open the Search write "variables" and open "Edit the system environment variables"
3. Go over in Advanced tab and click on "Environment variables"
4. Here, double click on "Path" (System Variables) - New.. - select your "yt-dlp.exe" file.
5. Open Command Prompt (Win + R → type cmd) and test:
   yt-dlp --version

# How install ffmpeg for Win 11:

1. Go to: https://www.gyan.dev/ffmpeg/builds/

2. In the "Release builds" section, download this ZIP file: ffmpeg-release-essentials.zip

3. Extract it somewhere

4. Inside the extracted folder, find bin\ffmpeg.exe

5. Add the C:\ffmpeg\bin\ folder to your system PATH:
Just like you did for yt-dlp

6. Open a new Command Prompt and test:
ffmpeg -version

From now, you shouldn't use other bots for music

# (Pls, create .env file and paste your API-key, expl: DISCORD_TOKEN=YOUR_TOKEN)
Get it, you can here: https://discord.com/developers/applications, by clicking "New application"
