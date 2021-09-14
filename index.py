import discord
from discord.ext import commands
from secrets import bot_token
from roll_utils import roll_stats

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def rollcharacter(ctx):
    await ctx.send("You got: {}".format(roll_stats()))


client.run(bot_token)
