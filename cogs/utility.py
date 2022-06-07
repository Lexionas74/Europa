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
    
    @commands.command()
    async def info(self, ctx):
        em = nextcord.Embed(title="Information", description="Europa", color=nextcord.Colour.green())
        em.add_field(name="Server count", value=f"{self.bot.user.name} is in {len(self.bot.guilds)} Servers!")
        await ctx.send(embed=em)
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(981077362978476042)
        join = nextcord.Embed(title=f"Joined {guild}", colour = nextcord.Colour.green())
        join.add_field(name="Server Count", value=f"{self.bot.user.name} is in {len(self.bot.guilds)} Guilds now!")
        join.add_field(name="Member Count", value=f"{len(guild.members)}  members")
        await channel.send(embed=join)
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(981077362978476042)
        leave = nextcord.Embed(title=f"Left {guild}", colour = nextcord.Colour.red())
        leave.add_field(name="Server Count", value=f"{self.bot.user.name} is in {len(self.bot.guilds)} Guilds now")
        leave.add_field(name="Member Count", value=f"{len(guild.members)} members")
        await channel.send(embed=leave)        
def setup(bot):
    bot.add_cog(Utility(bot)) 