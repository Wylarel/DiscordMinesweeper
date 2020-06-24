import discord
from discord.ext import commands

import minesweeper as ms

TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"

client = commands.Bot(command_prefix='!', case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def ping(ctx):
    await ctx.send("pong")


@client.command(name='minesweeper', aliases=['ms'], help='Minesweeper Bot')
async def minesweeper(ctx, size=10, difficulty=4):
    text = (
        "**MINESWEEPER**"
        "\nBy Wylarel\n"
        "\n*Size:* `%size%x%size%` | *Mines:* `%mines%`\n"
        "\n**Grid:**\n%grid%\n"
        "\n**Solution:**\n||%solution%||"
    )
    await ctx.send(ms.main(text=text, size=size, difficulty=difficulty))

client.run(TOKEN)
