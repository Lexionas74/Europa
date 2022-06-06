import nextcord
import random
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        choices = ("Heads", "Tails")
        rancoin = random.choice(choices)
        await ctx.reply(rancoin)
def setup(bot):
    bot.add_cog(Fun(bot))        