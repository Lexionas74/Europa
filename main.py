import os
import nextcord
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message

bot = commands.Bot(command_prefix="as!")
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
	print("uwu")

@bot.slash_command(name="Example", description="Slash command description here!")
async def example(interaction: Interaction):
	await interaction.response.send_message("Message you want to send here")

bot.run(my_secret)