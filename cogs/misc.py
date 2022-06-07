import nextcord
import random
from nextcord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot



def setup(bot):
    bot.add_cog(Misc(bot))  