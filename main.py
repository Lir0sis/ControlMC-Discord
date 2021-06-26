# bot.py
import os
import re
import subprocess
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER = os.getenv('ADMIN')
TRUSTED = list(json.loads(os.getenv('TRUSTED_LIST')))

service_name = 'MCServerIIA'

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# @bot.command()
# async def help(ctx):
#     ctx.send('go PM me with theese commands')

@bot.command()
async def start(ctx):
    if (ctx.author == OWNER or ctx.author in TRUSTED):
        res = subprocess.run(['sc','start',service_name])
        ctx.send(res)

@bot.command()
async def stop(ctx):
    if (ctx.author == OWNER or ctx.author in TRUSTED):
        res = subprocess.run(['sc','stop',service_name])
        ctx.send(res)

bot.run(TOKEN)