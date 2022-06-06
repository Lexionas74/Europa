import nextcord
import random
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        choices = ("Heads", "Tails")
        rancoin = random.choice(choices)
        await ctx.reply(rancoin)

    @commands.command(aliases=["8ball"], description="Ask the magic 8ball a question!")
    async def eightball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        await ctx.send(f":8ball: Question: {question}\n:8ball: Answer {random.choice(responses)}")        
    @commands.command(description="Play a rock paper scissors game against the bot!")
    async def rps(self, ctx, message):
        answer = message.lower()
        choices = ["rock", "paper", "scissors"]
        if answer not in choices:
            await ctx.reply(
                "That is not an option! Please user either: rock, paper or scissors"
            )
            return
        else:
            computers_answer = random.choice(choices)
            if computers_answer == answer:
                return await ctx.reply(f"Tie! We both picked {answer}")
            conversion = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
            if conversion[answer] == computers_answer:
                return await ctx.reply(
                    f"You win! I picked {computers_answer} and you picked {answer}!"
                )
            await ctx.reply(f"I win! I picked {computers_answer} and you picked {answer}!")
def setup(bot):
    bot.add_cog(Fun(bot))        