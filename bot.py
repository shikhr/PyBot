import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

from greeting import get_greeting

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def meme(ctx):
    await ctx.send("meem")


@bot.command()
async def slap(ctx, member: discord.Member):
    slapped_whom = "themselves" if ctx.author == member else member.mention
    await ctx.send(f"{ctx.message.author.mention} slapped {slapped_whom}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    messageContent = message.content.strip().lower()
    # print(message.author, message.content, message.channel.id)
    if messageContent == "hello there":
        await message.channel.send("General Kenobi")
    elif bool(re.search(r"\b(hel+o+|hey+|hi+)\b", messageContent)):
        await message.channel.send(get_greeting(message.author.mention))
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing a required argument.¯\_(ツ)_/¯")
        return
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That's not a valid command!")
        return
    await ctx.send("Couldn't run the command. (> <)")


bot.run(TOKEN)
