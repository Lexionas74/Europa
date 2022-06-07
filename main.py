import os
import nextcord
import random
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message
import asyncio
import difflib
import aiosqlite
from bot import Europa

async def get_prefix(bot: commands.Bot, message: Message):
    if not message.guild:
        return commands.when_mentioned_or("e!")(bot, message)
    try:
        return commands.when_mentioned_or(
            *bot.prefix_cache[message.guild.id])(bot, message)
    except KeyError:
        cur = await bot.db.execute(
            "SELECT prefix FROM prefix WHERE guild_id = ?",
            (message.guild.id, ))
        data = await cur.fetchall()
        if data is None or data == []:
            await bot.db.execute(
                "INSERT OR IGNORE INTO prefix(guild_id, prefix) VALUES (?,?)",
                (message.guild.id, "e!"),
            )
            await bot.db.commit()
            bot.prefix_cache[message.guild.id] = []
            bot.prefix_cache[message.guild.id].append("e!")
            data = [("e!", )]
        prefixes = [prefix for i in data for prefix in i]
        prefixes = sorted(prefixes, key=lambda m: len(m), reverse=True)
        return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, intents=nextcord.Intents.all())
bot.prefix_cache = {}
loop = asyncio.get_event_loop()
my_secret = os.environ['TOKEN']

async def Prefix(bot):
    await bot.wait_until_ready()
    bot.db = await aiosqlite.connect("prefix.db")
    await bot.db.execute(
        "CREATE TABLE IF NOT EXISTS prefix(guild_id int, prefix text)")
    await bot.db.commit()

async def Economy(bot):
    await bot.wait_until_ready()
    bot.economy_db = await aiosqlite.connect("economy.db")
    await bot.economy_db.execute(
        "CREATE TABLE IF NOT EXISTS economy(author_id int, wallet int, bank int, PRIMARY KEY (author_id))"
    )
    await bot.economy_db.commit()

@bot.event
async def on_ready():
    await ch_pr()
    print("uwu")

@bot.event
async def on_guild_join(guild: Guild):
    bot.prefix_cache[guild.id].append("e!")
    await bot.db.execute(
        "INSERT OR IGNORE INTO prefix(guild_id, pref) VALUES (?,?)",
        (guild.id, "p!"))
    await bot.db.commit()

@bot.event
async def on_guild_remove(guild: Guild):
    del bot.prefix_cache[guild.id]
    await bot.db.execute("DELETE FROM prefix WHERE guild_id =pre ?",
                            (guild.id, ))
    await bot.db.commit()

@bot.group(description="changes the prefix [admin only]", invoke_without_command=True)
@commands.check_any(commands.has_permissions(administrator=True), commands.is_owner())
async def prefix(ctx: commands.Context, prefix: str = None):
    prefixes = await get_prefix(bot, ctx)
    prefixes.remove('<@981074794986504253> ')
    if prefix is None:
        return await ctx.send(embed=nextcord.Embed(
            title="Server prefixes",
            description="\n".join([
                f"{num}. {prefix}"
                for num, prefix in enumerate(prefixes, start=1)
            ]),
        ))
    if len(
            prefixes
    ) == 7:  # do not change the message or the 7, this is done on purpose
        return await ctx.send("Can have a maximum of 5 prefixes per server")
    elif prefix in prefixes:
        return await ctx.send("That's already a prefix")
    try:
        bot.prefix_cache[ctx.guild.id].append(prefix)
    except KeyError:  # this error should never be raised but just in case
        print(bot.prefix_cache)
    await bot.db.execute(
        "INSERT OR IGNORE INTO prefix(guild_id, prefix) VALUES (?,?)",
        (ctx.guild.id, prefix),
    )
    await bot.db.commit()
    await ctx.send(f"Added ``{prefix}`` to server prefixes")

@prefix.command()
async def delete(ctx, prefix):
    prefixes = await get_prefix(bot, ctx)
    if prefix in prefixes:
        await bot.db.execute(
            "DELETE FROM prefix WHERe guild_id = ? AND prefix = ?",
            (ctx.guild.id, prefix))
        try:
            bot.prefix_cache[ctx.guild.id].remove(prefix)
        except ValueError:
            pass
        await ctx.send(f"Done! removed {prefix} from server prefixes")
    else:
        return await ctx.send(f"{prefix} isn't a server prefix")

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

bot.run(my_secret)
