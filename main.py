import discord
from discord.ext import commands, tasks
import openpyxl
import random
from itertools import cycle
import os
from openpyxl import load_workbook
import asyncio

wb = load_workbook(r'C:\Users\pablo\PycharmProjects\trivia_bot\trivia.xlsx')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
sheet = wb.active
counterA = 0
counterB = 0
counterC = 0
counterD = 0
def question(choice):
    question = sheet[f"A{choice}"].value
    return question
def choiceA(choice):
    choiceA = sheet[f"B{choice}"].value
    return choiceA
def choiceB(choice):
    choiceB = sheet[f"C{choice}"].value
    return choiceB
def choiceC(choice):
    choiceC = sheet[f"D{choice}"].value
    return choiceC
def choiceD(choice):
    choiceD = sheet[f"E{choice}"].value
    return choiceD
def answer(choice):
    answer = sheet[f"F{choice}"].value
    return answer

@bot.command()
async def trivia(ctx):
    global number
    print("in trivia")
    member = ctx.message.author
    numberrr = random.randint(1, 150)
    questionN = question(numberrr)
    choiceeA = choiceA(numberrr)
    choiceeB = choiceB(numberrr)
    choiceeC = choiceC(numberrr)
    choiceeD = choiceD(numberrr)
    answerR = answer(numberrr)
    embed_message = discord.Embed(title="Trivia",
                            description="Trivia question answer by doing .......",
                            color=0x109319)
    embed_message.add_field(name=questionN, value="A = " + choiceeA + "\nB = " + choiceeB + "\nC = " + choiceeC + "\nD = " + choiceeD + "",
                    inline=False)

    embed_message.set_footer(text="this bot has been made by <@698854159117582439>")
    await ctx.send(embed=embed_message)
    print("before count")
    await asyncio.sleep(6)
    print("after count")
    print(counterA)
    print(counterB)
    print(counterC)
    print(counterD)
    if counterA > counterB and counterA > counterC and counterA  > counterD:
        await ctx.send("you guys chose A")
    elif counterB > counterA and counterB > counterB and counterC > counterD:
        await ctx.send("you guys chose B")
    elif counterC > counterA and counterC > counterB and counterC > counterD:
        await ctx.send("you guys chose C")
    elif counterD > counterA and counterD > counterB and counterD > counterC:
        await ctx.send("you guys chose D")
    elif counterA == 0:
        await ctx.send("error contant exir180")


@bot.command()
async def vote(ctx, arg):
    print("voted")
    global counterA
    global counterB
    global counterC
    global counterD
    if arg == "A":
        await ctx.send("voted A")
        counterA = counterA + 1
    elif arg == "B":
        await ctx.send("voted B")
        counterB += 1
    elif arg == "C":
        await ctx.send("voted C")
        counterC += 1
    elif arg == "D":
        await ctx.send("voted D")
        counterD += 1


bot.run("MTExNzUzODAyNjA3NjI0MjA4NQ.GOx9nL.VsN6kiGP8Xw7b0CGt2MfOG_hdeh6TslpmggDps")
