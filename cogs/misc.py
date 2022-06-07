import nextcord
import random
from nextcord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    @commands.command()
    async def test(self, ctx):
        await ctx.send("balls")
    @commands.command()
    async def test_(self, ctx):
        await ctx.send("balls")


def setup(bot):
    bot.add_cog(Misc(bot))  