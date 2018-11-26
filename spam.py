import discord
from discord.ext.commands import Bot

from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("you did it!")

@client.event
async def on_message(message):
    if message.content.upper().startswith ("!spam"):
        await client.send_message(message.channel, "!spam :money_mouth:")


client.login("NTA5MTA3NDgyMDkwNzk5MTI0.Dt3tbw.lpGzU0s4PqT133UbwzB0iJA9l3I")
 
