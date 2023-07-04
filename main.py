import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asyncio
import requests
from datetime import timezone
import datetime
import base64

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
counterA = 0
counterB = 0
counterC = 0
counterD = 0
numberr = 0

@bot.command()
async def trivia(ctx):
    global number
    global counterA
    global counterB
    global counterC
    global counterD
    counterA = 0
    counterB = 0
    counterC = 0
    counterD = 0
    print("in trivia")
    member = ctx.message.author
    resp = requests.get('https://opentdb.com/api.php?amount=1&type=multiple&encode=base64')
    parsed = resp.json()

    for result in parsed["results"]:
        questionn = result["question"]
        base64_message = questionn
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        question = message_bytes.decode('ascii')
        print(question)
    for result in parsed["results"]:
        choiceeA = result["correct_answer"]
        base64_message = choiceeA
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        choiceA = message_bytes.decode('ascii')
    for result in parsed["results"]:
        wronganswerss = result["incorrect_answers"]
        base64_message = wronganswerss
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        wronganswers = message_bytes.decode('ascii')
    for result in parsed["results"]:
        answerr = result["correct_answer"]
        base64_message = answerr
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        answer = message_bytes.decode('ascii')
    numberr = random.randint(1,4)
    choiceB, choiceC, choiceD = wronganswers
    await ctx.send(answer)
    if numberr == 1:
        print("1")
        embed_message = discord.Embed(title="Trivia",
                                      description="Trivia question answer by doing .......",
                                      color=0x109319)
        embed_message.add_field(name=question,
                                value="A = " + choiceA + "\nB = " + choiceB + "\nC = " + choiceC + "\nD = " + choiceD + "",
                                inline=False)

        embed_message.set_footer(text="this bot has been made by <@698854159117582439>")
        await ctx.send(embed=embed_message)
    elif numberr == 2:
        print("2")
        embed_message = discord.Embed(title="Trivia",
                                      description="Trivia question answer by doing .......",
                                      color=0x109319)
        embed_message.add_field(name=question,
                                value="A = " + choiceB + "\nB = " + choiceA + "\nC = " + choiceC + "\nD = " + choiceD + "",
                                inline=False)

        embed_message.set_footer(text="this bot has been made by <@698854159117582439>")
        await ctx.send(embed=embed_message)
    elif numberr == 3:
        print("3")
        embed_message = discord.Embed(title="Trivia",
                                      description="Trivia question answer by doing .......",
                                      color=0x109319)
        embed_message.add_field(name=question,
                                value="A = " + choiceC + "\nB = " + choiceB + "\nC = " + choiceA + "\nD = " + choiceD + "",
                                inline=False)

        embed_message.set_footer(text="this bot has been made by <@698854159117582439>")
        await ctx.send(embed=embed_message)
    elif numberr == 4:
        print("4")
        embed_message = discord.Embed(title="Trivia",
                                      description="Trivia question answer by doing .......",
                                      color=0x109319)
        embed_message.add_field(name=question,
                                value="A = " + choiceD + "\nB = " + choiceB + "\nC = " + choiceC + "\nD = " + choiceA + "",
                                inline=False)

        embed_message.set_footer(text="this bot has been made by <@698854159117582439>")
        await ctx.send(embed=embed_message)
    await asyncio.sleep(6)
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    before = utc_timestamp * 1000




@bot.command()
async def vote(ctx, arg):
    print("voted")
    global numberr
    global counterA
    global counterB
    global counterC
    global counterD
    if arg == "A":
        await ctx.send("chose A")
        counterA = counterA + 1
        dt = datetime.datetime.now(timezone.utc)
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        after = utc_timestamp * 1000
        if numberr == 1:
            await ctx.send("yup")
        else:
            await ctx.send("nope")
    elif arg == "B":
        await ctx.send("chose B")
        counterB += 1
        dt = datetime.datetime.now(timezone.utc)
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        after = utc_timestamp * 1000
        if numberr == 2:
            await ctx.send("yup")
        else:
            await ctx.send("nope")
    elif arg == "C":
        await ctx.send("chose C")
        counterC += 1
        dt = datetime.datetime.now(timezone.utc)
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        after = utc_timestamp * 1000
        if numberr == 3:
            await ctx.send("yup")
        else:
            await ctx.send("nope")
    elif arg == "D":
        await ctx.send("chose D")
        counterD += 1
        dt = datetime.datetime.now(timezone.utc)
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        after = utc_timestamp * 1000
        if numberr == 4:
            await ctx.send("yup")
        else:
            await ctx.send("nope")
    PointsGain = after


bot.run("token")
