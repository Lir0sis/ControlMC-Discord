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
process = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# @bot.command()
# async def help(ctx):
#     ctx.send('go PM me with theese commands')

@bot.command()
async def start(ctx):
    if (str(ctx.author) == OWNER or ctx.author in TRUSTED):
        #FNAME = 'myfifo'
        #os.mkfifo(FNAME, mode=0o777)

        # Open read end of pipe. Open this in non-blocking mode since otherwise it
        # may block until another process/threads opens the pipe for writing.
        #stdin = os.open(FNAME, os.O_RDONLY | os.O_NONBLOCK)

        # Open the write end of pipe.
        #tochild = os.open(FNAME, os.O_WRONLY)
        #print('Pipe open (%d, %d)' % (stdin, tochild))
        global process
        process = subprocess.Popen(
            [r'C:\Users\Valentine\Desktop\gtserver-thermos\run.bat'],
            cwd=r'C:\Users\Valentine\Desktop\gtserver-thermos',
            shell=False,
            stdout=None,
            stdin=None,
            stderr=None,
            universal_newlines=True,
        )
        #print('child started: %s (%s)' % (str(process), str(process.stdin)))

        # Close read end of pipe since it is not used in the parent process.

        # Write to child then close the write end to indicate to the child that
        # the input is complete.
        #os.write(tochild, bytes('Line 1\n', 'utf-8'))
        #os.write(tochild, bytes('Line 2\n', 'utf-8'))
        #print('data written')
        #os.close(tochild)

        # Wait for child to complete.
        #process.wait()
        #os.unlink(FNAME)
        await ctx.send('Starting server...')

@bot.command()
async def stop(ctx):
    if (str(ctx.author) == OWNER or ctx.author in TRUSTED):
        await process.terminate()
        outs, errs = process.communicate()
        await ctx.send('{}\n{}'.format(outs,errs))

@bot.command()
async def status(ctx):
    if (str(ctx.author) == OWNER or ctx.author in TRUSTED):
        try:
            if (process != None and process.communicate(timeout=120) != None):
                await ctx.send('Server is up')
            else:
                await ctx.send('Sever is down')
        except subprocess.TimeoutExpired:
            process.kill()
            outs, errs = process.communicate()
            await ctx.send('{}\n{}'.format(outs,errs))

@bot.command()
async def exec(ctx, *args):
    if (str(ctx.author) == OWNER or ctx.author in TRUSTED):
        outs, errs = process.communicate(''.join(args))
        await ctx.send('{}\n{}'.format(outs,errs))
            
bot.run(TOKEN)