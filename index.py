import discord
from discord.ext import commands
from datetime import datetime
from asyncio import sleep

from secrets import bot_token
from roll_utils import roll_stats
from ascii_bar import create_bar
from schedules_utils import *


client = commands.Bot(command_prefix="!")
last_session = ""
next_session = ""


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def rollcharacter(ctx):
    await ctx.send("You got: {}".format(roll_stats()))


@client.command()
async def createbar(ctx, arg):
    await ctx.send("--<>--Loading Next Session:--<>--\n{}".format(create_bar(int(arg))))


@client.command()
async def ns(ctx, arg, arg2=None):
    global last_session
    global next_session

    try:
        ns_datetime = datetime.strptime(str(arg), "%d-%m-%Y-%H:%M")

        if str(arg2) == "auto-ls":
            if next_session == "":
                last_session = datetime.now().strftime("%d-%m-%Y-%H:%M")
            else:
                last_session = next_session

        next_session = ns_datetime
        percentage = calculate_percent_to_next_session(last_session, next_session)
        message = await ctx.send(
            "Next Session: \n```\n{} BTC\n```{}--<>--Loading Next Session:--<>--\n{}".format(
                str(next_session),
                calculate_time_difference(next_session),
                create_bar(percentage),
            )
        )

        while sixty_seconds_left(next_session) != True:
            await sleep(60)
            percentage = calculate_percent_to_next_session(last_session, next_session)
            contents = "Next Session: \n```\n{} BTC\n```{}--<>--Loading Next Session:--<>--\n{}".format(
                str(next_session),
                calculate_time_difference(next_session),
                create_bar(percentage),
            )
            await message.edit(content=contents)

        contents = "Next Session: \n```\n{} BTC\n```{}--<>--Loading Next Session:--<>--\n{}".format(
            str(next_session),
            "Time Till Next Game: ```\n0 Days, 0 Hours, 0 Minutes\n```",
            create_bar(100),
        )
        await message.edit(content=contents)
    except:
        await ctx.send(
            "Wrong time format please enter a format matching day-month-year-hour:minutes for example '01-01-2021-00:00'"
        )


@client.command()
async def setls(ctx, arg):
    global last_session
    try:
        last_session = datetime.strptime(str(arg), "%d-%m-%Y-%H:%M")
        await ctx.send("Setting Last Session Time To: {}".format(str(last_session)))
    except:
        await ctx.send(
            "Wrong time format please enter a format matching day-month-year-hour:minutes for example '01-01-2021-00:00'"
        )


client.run(bot_token)
