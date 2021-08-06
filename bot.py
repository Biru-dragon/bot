import discord
import json
import datetime

from urllib import parse, request
import re

default_intents = discord.Intents.default()
default_intents.members = True

bot = commands.Bot(command_prefix='!', description="", intents=default_intents)

@bot.event
async def on_ready():
    print(f"{bot.user.display_name} is ready !")

#Partie du code concernant juste une commande (qui marche)
    
@bot.event
async def on_member_join(member: discord.Member):
    memberid = "{member.id}"

bot.run("token")     
