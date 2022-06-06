import nextcord
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

def setup(bot):
    bot.add_cog(Fun(bot))        