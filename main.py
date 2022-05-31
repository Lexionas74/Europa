import os
import nextcord
from nextcord.ext import commands
from nextcord import Guild, Interaction, Message

bot = commands.Bot(command_prefix="as!")
my_secret = os.environ['TOKEN']

@bot.slash_command()
async def test(interaction: Interaction):
	await interaction.response.send_message("haha balls")

bot.run(my_secret)