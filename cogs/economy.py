import nextcord
from nextcord.ext import commands
from datetime import datetime
import asyncio
import random

class Economy(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    async def open_account(self, member):
        cursor = await self.bot.economy_db.execute("SELECT * FROM economy WHERE author_id = ?", (member.id,))
        data = await cursor.fetchone()
        if not data:
            await self.bot.economy_db.execute("INSERT OR IGNORE INTO economy (author_id, wallet, bank) VALUES (?,?,?)", (member.id, 0, 0))
            await self.bot.economy_db.commit()

    async def update_economy(self, member, change=0, mode='wallet'):
        await self.open_account(member)
        await self.bot.economy_db.execute(f"UPDATE economy SET {mode} = {mode} + ? WHERE author_id = ?", (change, member.id))
        await self.bot.economy_db.commit()
        cursor = await self.bot.economy_db.execute("SELECT wallet, bank FROM economy WHERE author_id = ?", (member.id,))
        data = await cursor.fetchone()
        return {'wallet':data[0], 'bank':data[1]}

    async def ConvertToInt(self, ctx, amount, mode='wallet'):
        cursor = await self.bot.economy_db.execute(f"SELECT {mode} FROM economy WHERE author_id = ?", (ctx.author.id,))
        data = await cursor.fetchone()
        mode = data[0]
        amount = amount.replace("max", f"{mode}")
        amount = amount.replace("all", f"{mode}")
        amount = amount.replace("half", f"{int(mode/2) if not int(mode/2) else int(mode/2+1)}")
        amount = re.sub(r"[^0-9ekEK.]", r"", amount)
        amount = amount.replace(".0", "")
        amount = amount.replace("k", "*1000")
        amount = amount.replace("e", "*10**")
        try:
            am = int(eval(amount))
        except Exception:
            raise commands.BadArgument("That's an invalid way to type the amount")
        if am > mode:
            raise commands.BadArgument(f"You don't have that much money in your bank, you only have {mode}")
        elif am < 0:
            raise commands.BadArgument("Amount can't be negative")
        elif am == 0:
            raise commands.BadArgument("Amount can't be 0")
        return am        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def beg(self, ctx):
        money = random.randint(10, 100)
        await self.update_economy(ctx.author, money)
        await ctx.send("You got {0} money".format(money))    
def setup(bot):
    bot.add_cog(Economy(bot))            