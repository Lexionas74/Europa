import os
import nextcord
import random
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message
import asyncio
import difflib
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
    statuses = ["e!help", "you through your window" "Lexionas74#1535", "Angad07#0337"]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=nextcord.Activity(
            type=nextcord.ActivityType.watching, name=status))
        await asyncio.sleep(300)
@bot.event        
async def on_command_error(ctx: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            matches = difflib.get_close_matches((ctx.message.content.split(' ')[0]).strip(ctx.prefix), [cmd.name for cmd in bot.commands]) # this needs to be improved but i can't be bothered to do that rn
            if matches:
                em = nextcord.Embed(title='Command not found', description="Did you mean: \n"+' | '.join(f'`{match}`' for match in matches), color=nextcord.Color.red())
                return await ctx.send(embed=em)
            return await ctx.send(embed=nextcord.Embed(title='Command not found', description="That's not a command", color=nextcord.Color.red()))       
        elif isinstance(error, commands.MissingRequiredArgument):
            ctx.command.reset_cooldown(ctx)
            em = nextcord.Embed(
                title="Missing Required Argument",
                color = nextcord.Color.red(),
                description=f"```\n{ctx.prefix}{ctx.command.name} {ctx.command.usage if ctx.command.usage else ctx.command.signature}\n```\n\n**{error.args[0]}**")
            await ctx.send(embed=em)            
        await ctx.send(error)


bot.run(my_secret)