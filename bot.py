# Bot.py
import discord
import os
import asyncio
from dotenv import load_dotenv
import time
import random

#GLOBALS
load_dotenv()
DISCORD_TOKEN  = os.getenv("DISCORD_TOKEN")
DISCORD_CLIENT = discord.Client()
AUDIO_FILES    = os.listdir(path=".\\audio")

def __in_voice_channel(voice):
    global DISCORD_CLIENT
    ids = [vc.id for vc in [vc.channel for vc in DISCORD_CLIENT.voice_clients]]
    return voice.channel.id in ids

@DISCORD_CLIENT.event
async def on_ready():
    global DISCORD_CLIENT
    print("Bot is Now Running")
    for guild in DISCORD_CLIENT.guilds:
        print(
            f'{DISCORD_CLIENT.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

@DISCORD_CLIENT.event
async def on_message(message):
    global DISCORD_CLIENT
    global AUDIO_FILES
    path = "audio\\"
    file = os.path.join(path,random.choice(AUDIO_FILES))
    if "🐒" in message.content.lower():
        voiceChannel = message.author.voice
        if voiceChannel is not None and not __in_voice_channel(voiceChannel):
            vc = await voiceChannel.channel.connect()
            vc.play(discord.FFmpegPCMAudio(file), after=lambda e: print('done', e))
            while vc.is_playing():
                await asyncio.sleep(1)
            vc.stop()
            await vc.disconnect()

def Run():
    global DISCORD_TOKEN
    global DISCORD_CLIENT
    
    print("Running Bot...")
    DISCORD_CLIENT.run(DISCORD_TOKEN)

def main():
    Run()

if __name__ == "__main__":
    main()