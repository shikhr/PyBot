from discord.ext import commands
import discord


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", description="Get a list of all commands")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help", description="List of available commands:", color=0x9C84EF
        )
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i)
            commands = cog.get_commands()
            data = []
            for command in commands:
                description = command.description.partition("\n")[0]
                data.append(f".{command.name} - {description}")
            help_text = "\n".join(data)
            embed.add_field(
                name=i.capitalize(), value=f"```{help_text}```", inline=False
            )
        await ctx.send(embed=embed)

    @commands.command(name="ping", description="Test the bot")
    async def ping(self, ctx):
        await ctx.send(f"pong")


async def setup(bot):
    await bot.add_cog(General(bot))
