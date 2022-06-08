import os
import nextcord
import random
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message
import asyncio
import difflib
import aiosqlite


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
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the perms for that")
    elif isinstance(error,commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if int(h) == 0 and int(m) == 0:
            em = nextcord.Embed(title="**Command on cooldown**", description=f'You must wait {int(s)} seconds to use the {ctx.command} command!', colour=nextcord.Colour.red())
            await ctx.send(embed=em, delete_after=float(error.retry_after))
        elif int(h) == 0 and int(m) != 0:
            em = nextcord.Embed(title="**Command on cooldown**", description=f' You must wait {int(m)} minutes and {int(s)} seconds to use the {ctx.command} command!', colour=nextcord.Colour.red())
            await ctx.send(embed=em, delete_after=float(error.retry_after))
        else:
            em = nextcord.Embed(title="**Command on cooldown**", description=f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use the {ctx.command} command!', colour=nextcord.Colour.red())
            await ctx.send(embed=em, delete_after=float(error.retry_after))
    elif isinstance(error, commands.MissingRequiredArgument):
        ctx.command.reset_cooldown(ctx)
        em = nextcord.Embed(
            title="Missing Required Argument",
            color = nextcord.Color.red(),
            description=f"```\n{ctx.prefix}{ctx.command.name} {ctx.command.usage if ctx.command.usage else ctx.command.signature}\n```\n\n**{error.args[0]}**")
        await ctx.send(embed=em)
    elif isinstance(error, commands.CommandNotFound):
        matches = difflib.get_close_matches((ctx.message.content.split(' ')[0]).strip(ctx.prefix), [cmd.name for cmd in self.commands]) # this needs to be improved but i can't be bothered to do that rn
        if matches:
            em = nextcord.Embed(title='Command not found', description="Did you mean: \n"+' | '.join(f'`{match}`' for match in matches), color=nextcord.Color.red())
            return await ctx.send(embed=em)
        return await ctx.send(embed=nextcord.Embed(title='Command not found', description="That's not a command", color=nextcord.Color.red()))
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("You dont own the bot, you cant do that")
    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send("That cog does not exist or is not loaded")
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("That command is disabled!")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Member is not found")
    else:        
        await ctx.send(error)
        raise error


bot.run(my_secret)
