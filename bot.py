import discord
from discord.ext import commands
import random

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send('Я демонстративный бот!')

@bot.command('weather')
async def command_weather(ctx:commands.Context):
    await ctx.send('Погода сегодня класс!')

@bot.command('plus')
async def command_plus(ctx:commands.Context, a, b):
    a = int(a)
    b = int(b)
    result = a + b
    await ctx.send(result)

@bot.command('minus')
async def command_minus(ctx:commands.Context, a, b):
    a = int(a)
    b = int(b)
    result = a - b
    await ctx.send(result)

@bot.command('password')
async def command_password(ctx:commands.Context):
    sogl = 'qwrtpsdghjklxcvbnm'
    glas = 'eyuioa'
    numbers = '01234567890'
    symbol = '@#%?!'
    password = ""
    for i in range(4):
        password += random.choice(sogl)
        password += random.choice(glas)
    for i in range(2):
        password += random.choice(numbers)
    password += random.choice(symbol)
    print(password)

bot.run("")
