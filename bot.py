# Bot.py
import discord
import os
import asyncio
from dotenv import load_dotenv
import time

#GLOBALS
load_dotenv()
DISCORD_TOKEN  = os.getenv("DISCORD_TOKEN")
DISCORD_CLIENT = discord.Client()

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
    file = 'snd_01.mp3'
    if "🐒" in message.content.lower():
        voiceChannel = message.author.voice
        if voiceChannel is not None:
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