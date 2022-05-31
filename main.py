import os
import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="as!")
my_secret = os.environ['TOKEN']


bot.run(my_secret)