import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

from greeting import get_greeting
import responses
from create_meme import gen_meme_url

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def cmeme(ctx, *args):
    gen_url = gen_meme_url(args)
    await ctx.send(gen_url)


@bot.command()
async def slap(ctx, member: discord.Member):
    if member == bot.user:
        await ctx.send(
            responses.u1_throws_u2(u1=bot.user.mention, u2=ctx.message.author.mention)
        )
        return
    slapped_whom = "themselves" if ctx.message.author == member else member.mention
    await ctx.send(f"{ctx.message.author.mention} slapped {slapped_whom}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    messageContent = message.content.strip().lower()

    if messageContent == "hello there":
        await message.channel.send("General Kenobi")

    elif bool(re.search(r"\b(hel+o+|hey+|hi+)\b", messageContent)):
        await message.channel.send(get_greeting(message.author.mention))

    elif bool(re.search(r"\b(good *night|gn)\b", messageContent)):
        await message.channel.send(f"✨Sweet dreams✨, {message.author.mention}")

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
