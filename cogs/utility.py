import nextcord
from nextcord.ext import commands
from datetime import datetime
import asyncio
import random

class Utility(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.launch_time = datetime.utcnow()
    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.reply(f"I have been online for {days}d, {hours}h, {minutes}m, {seconds}s")
        print(f"I have been online for {days}d, {hours}h, {minutes}m, {seconds}s")
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! My lantency is {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Utility(bot)) 