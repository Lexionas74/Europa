from nextcord.ext import commands
import aiosqlite


async def Economy(bot):
    await bot.wait_until_ready()
    bot.economy_db = await aiosqlite.connect("economy.db")
    await bot.economy_db.execute(
        "CREATE TABLE IF NOT EXISTS economy(guild_id int, author_id int, wallet int, bank int, PRIMARY KEY (author_id))"
    )
    await bot.economy_db.commit()


async def Prefix(bot):
    await bot.wait_until_ready()
    bot.db = await aiosqlite.connect("prefix.db")
    await bot.db.execute(
        "CREATE TABLE IF NOT EXISTS prefix(guild_id int, prefix text)")
    await bot.db.commit()