import nextcord
from nextcord.ext import commands
import random

bot = commands.Bot(command_prefix='hl!', Intents = nextcord.Intents.all(), _CaseInsensitiveDict = True)

@bot.command()
async def roll(ctx):
    await ctx.send(random.choice(['Yes', 'No']))

bot.run('MTAxOTc0NTc2MTI3MDk1NjA4Mg.G4LM-s.e7T9nslpTRb8yLodb1f84jCiK_ZijWFbHyhwcQ')