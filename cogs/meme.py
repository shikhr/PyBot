from discord.ext import commands
import discord
from create_meme import gen_meme_url


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cmeme", description="Create a meme using memegen api")
    async def cmeme(self, ctx, *args):
        gen_url = gen_meme_url(args)
        await ctx.send(gen_url)


async def setup(bot):
    await bot.add_cog(Meme(bot))
