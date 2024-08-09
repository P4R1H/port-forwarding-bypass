import discord
from discord.ext import commands
from discord.commands import Option
import os
from discord import option
from dotenv import load_dotenv
import subprocess
load_dotenv()

banned_commands = []

vibe = """
Linux pi 6.6.28+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.6.28-1+rpt1 (2024-04-22) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Jun  2 02:51:58 2024 from 192.168.1.9
"""
intents = discord.Intents.all()
client = commands.Bot(command_prefix=",", intents=intents)

# favorite save
# aliases

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="π"))
    client.terminal = 0
    print("{0.user}".format(client))

@client.event
async def on_message(msg):
    if(msg.author.id!=617021192011776000): return
    await client.process_commands(msg)
    if(msg.channel.id != 1247276658998771723): return
    if(not client.terminal):
        if msg.content == "ssh pi@192.168.1.1": 
            client.terminal = 1
            em = discord.Embed(description=f"```\n{vibe}\n```", color = discord.Color.blue())
            await msg.channel.send(embed = em)
    elif msg.content == "exit": 
        client.terminal = 0
        await msg.add_reaction("🍃")
    elif client.terminal:
        if msg.content.startswith("cd "):
            directory = msg.content.split(" ", 1)[1]
            os.chdir(directory)
            result = subprocess.run("ls", shell=True, capture_output=True, text=True)
            em = discord.Embed(description=f"Changed directory to `{os.getcwd()}`\n\n```\n{result.stdout}\n```", color=discord.Color.blue())
        else:
            result = subprocess.run(msg.content, shell=True, capture_output=True, text=True)
            if(result.returncode==0):
                em = discord.Embed(description=f"```\n{result.stdout}\n```", color=discord.Color.green())
            else:
                em = discord.Embed(description=f"```\n{result.stderr}\n```", color=discord.Color.red())
        await msg.channel.send(embed=em)


@client.command()
async def pi(ctx, *, sentence):
    result = subprocess.run(sentence, shell=True, capture_output=True, text=True)
    if(result.returncode==0):
        em = discord.Embed(description = f"**Argument**```\n{result.args}\n```\n**Output**\n```\n{result.stdout}\n```", color = discord.Color.green())
    else:
        em = discord.Embed(description = f"**Argument**```\n{result.args}\n```**Error**\n```\n{result.stderr}\n```", color = discord.Color.red())

    await ctx.reply(embed = em)


@client.slash_command(guild_ids=[877275069309657089], description = "Connect to ssh client")
async def ssh(ctx):
    if(ctx.author.id!=617021192011776000): 
        await ctx.respond("No", ephemeral = True)
        return
    if(client.terminal == 1):
        client.terminal = 0
        await ctx.respond("Terminal deactivated.")
    else:
        client.terminal = 1
        await ctx.respond("Terminal activated.")


@client.slash_command(guild_ids=[877275069309657089], description = "Upload file to send to remote server.")
async def upload_file(ctx, file: discord.Option(discord.Attachment, description="File"), relative_path=None):
    if(ctx.author.id!=617021192011776000): 
        await ctx.respond("No", ephemeral = True)
        return
    if relative_path is None:
        relative_path = file.filename
    saved_file = await file.save(relative_path)
    await ctx.respond(f"File saved to `{os.getcwd()}/{relative_path}`", ephemeral = True)


@client.slash_command(guild_ids=[877275069309657089], description = "Retrieve file from remote server.")
async def get_file(ctx, relative_path):
    if(ctx.author.id!=617021192011776000): 
        await ctx.respond("No", ephemeral = True)
        return
    try:
        with open(relative_path, 'rb') as file:
            discord_file = discord.File(file, filename=relative_path)
            await ctx.respond(file=discord_file)
    except Exception as a:
        await ctx.respond(f"Couldn't upload file\nError: `{a}`")
    


client.run(os.getenv("TOKEN"))

