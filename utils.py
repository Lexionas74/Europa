from nextcord.ext import commands
import aiosqlite


async def Economy(client):
    await client.wait_until_ready()
    client.economy_db = await aiosqlite.connect("economy.db")
    await client.economy_db.execute(
        "CREATE TABLE IF NOT EXISTS economy(guild_id int, author_id int, wallet int, bank int, PRIMARY KEY (author_id))"
    )
    await client.economy_db.commit()


async def Prefix(client):
    await client.wait_until_ready()
    client.db = await aiosqlite.connect("prefix.db")
    await client.db.execute(
        "CREATE TABLE IF NOT EXISTS prefix(guild_id int, prefix text)")
    await client.db.commit()