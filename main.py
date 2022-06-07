import os
import nextcord
import random
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message
import asyncio
bot = commands.Bot(command_prefix="e!", intents=nextcord.Intents.all())
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
    await ch_pr()
    print("uwu")

@bot.slash_command(name="example", description="Slash command description here!")
async def example(interaction: Interaction):
	await interaction.response.send_message("Message you want to send here")

@bot.command()
@commands.is_owner()
async def reload(ctx: commands.Context, extension: str):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    print(f"Unloaded and Reloaded {extension}")
    await ctx.reply("Reloaded Cog succesfully!")  
        
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.reply("Loaded extension!")
    
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.reply("Unloaded extension!")

async def ch_pr():
    await bot.wait_until_ready()
    statuses = ["as!help", "you through your window" "Lexionas74#1535", "Angad07#0337"]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=nextcord.Activity(
            type=nextcord.ActivityType.watching, name=status))
        await asyncio.sleep(300)

bot.run(my_secret)