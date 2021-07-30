# bot.py
import discord

import os
from dotenv import load_dotenv

import random

client = discord.Client()

fortunes = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    file = open("cookiesayings.txt", "r", encoding="utf-8")
    i = 0
    while True:
        next_line = file.readline()
        fortunes.append(next_line)
        i = i + 1
        if not next_line:
            break

    file.close()




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!cookie'):



        response = "Here is your fortune: " + random.choice(fortunes)
        await message.channel.send(response)


load_dotenv(verbose=True)
client.run(os.getenv('TOKEN'))