import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='ph!')

@bot.event
async def on_ready():
    print ("Ready")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def eight_ball():
 responses = [
    'No, just no.',
    'YES YES YES.',
    'Maybe.',
    'Probably.',
    'I will keep it as a mystery.',
 ]
 await bot.say(random.choice(responses))
@bot.command(pass_context=True)
async def sing():
 response = [
     "I don't like singing, noob.",
     "Happy birthday to you, Happy birthday to you.",
     "Sorry, I prefer to see you doing that.",
 ]
 await bot.say(random.choice(response))
@bot.command(pass_context=True)
async def info():
 response = ("```Hey there, thanks for using Phoenix Bot, I'm currently getting configured, so this command will be done soon.```")
 await bot.say(response)
bot.run("NDYyMjQxMzk1NzY0MjMyMTkz.DhgQ8Q.EmqyftS4CPF8BYlEl5Vf2pv8pHg")
