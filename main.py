import os
import nextcord
import random
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message

bot = commands.bot(command_prefix="as!")
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
	print("uwu")

@bot.slash_command(name="Example", description="Slash command description here!")
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


@bot.command()
async def simprate(ctx):
	choices = [1, 100]
	await ctx.send(random.choice(choices))
bot.run(my_secret)