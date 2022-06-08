import nextcord
from nextcord.ext import commands
from datetime import datetime
import asyncio
import random

class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: nextcord.Member, reason):
        await member.kick(reason=reason)
        embed = nextcord.embed(name="Kicked Member", description=f"kicked {member} from the server for `{reason}`", colour = nextcord.Colour.green())
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))         