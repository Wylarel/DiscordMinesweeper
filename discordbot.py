from discord.ext import commands

import minesweeper as ms

TOKEN = open("TOKEN", "r").read()

client = commands.Bot(command_prefix='!', case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def ping(ctx):
    await ctx.send("pong")


@client.command(name='minesweeper', aliases=['ms'], help='Minesweeper Bot')
async def minesweeper(ctx, size=10, difficulty=2):
    text = (
        "**MINESWEEPER**"
        "\nBy Wylarel\n"
        "\n*Size:* `{size}x{size}` | *Difficulty:* `{difficulty}` | *Mines:* `{mines}`\n"
        "\n**Grid:**\n{grid}\n"
        "\n**Solution:**\n||{solution}||"
    )
    output = ms.main(text=text, size=size, difficulty=difficulty)
    if len(output) > 2000:
        await ctx.send(":x: The grid is too big for Discord (" + str(len(output)) + " characters)")
        return

    await ctx.send(output)


client.run(TOKEN)
