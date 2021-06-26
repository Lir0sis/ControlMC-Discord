# bot.py
import os
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TRUSTED = re.compile("").split(os.getenv('TRUSTED_LIST'))

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    #if message.author == self.user:
    print(message.author)

client.run(TOKEN)