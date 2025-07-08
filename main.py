import os
import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import yt_dlp

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL({
    'format': 'bestaudio/best',
    'noplaylist': False,
    'quiet': True,
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
})


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

queues = {}

@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user}')
    await tree.sync()

async def play_next(interaction: discord.Interaction, guild_id):
    print(f"[DEBUG] play_next для guild_id: {guild_id}")
    
    voice_client = interaction.guild.voice_client
    if not voice_client:
        return

    if queues.get(guild_id) and len(queues[guild_id]) > 0:
        query = queues[guild_id].pop(0)
        print(f"[DEBUG] Запрос: {query}")
        try:
            loop = bot.loop
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(query, download=False))
            
            if 'entries' in data:
                data = data['entries'][0]
            
            title = data.get('title', 'Неизвестно')
            url = data.get('url')
            
            if not url:
                raise Exception("Не удалось получить URL аудио")
            
            source = discord.FFmpegPCMAudio(url, **ffmpeg_options)
            source = discord.PCMVolumeTransformer(source)

            def after_playing(error):
                if error:
                    print(f"Ошибка: {error}")
                asyncio.run_coroutine_threadsafe(play_next(interaction, guild_id), bot.loop)

            voice_client.play(source, after=after_playing)
            await interaction.followup.send(f"🎶 Сейчас играет: {title}")
        except Exception as e:
            print(f"[ERROR] {e}")
            await interaction.followup.send(f"Ошибка: {e}")
            await play_next(interaction, guild_id)
    else:
        await voice_client.disconnect()
        await interaction.followup.send("Очередь пуста. Отключаюсь.")

@tree.command(name="play", description="Воспроизвести музыку")
@app_commands.describe(query="Ссылка или название")
async def play(interaction: discord.Interaction, query: str):
    await interaction.response.defer()
    guild_id = interaction.guild.id

    if not interaction.user.voice:
        await interaction.followup.send("Зайдите в голосовой канал!")
        return

    voice_channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client

    if not voice_client:
        await voice_channel.connect()
        voice_client = interaction.guild.voice_client

    if guild_id not in queues:
        queues[guild_id] = []

    queues[guild_id].append(query)

    if not voice_client.is_playing():
        await play_next(interaction, guild_id)
    else:
        await interaction.followup.send("Трек добавлен в очередь.")

@tree.command(name="skip", description="Пропустить трек")
async def skip(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await interaction.response.send_message("⏭ Пропущено.")
    else:
        await interaction.response.send_message("Не играет музыка.")

@tree.command(name="queue", description="Показать очередь")
async def queue(interaction: discord.Interaction):
    guild_id = interaction.guild.id
    q = queues.get(guild_id, [])
    if q:
        msg = "\n".join(f"{i+1}. {url}" for i, url in enumerate(q))
        await interaction.response.send_message(f"Очередь:\n{msg}")
    else:
        await interaction.response.send_message("Очередь пуста.")

bot.run(TOKEN)