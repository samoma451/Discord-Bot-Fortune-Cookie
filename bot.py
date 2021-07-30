# bot.py
import discord
import os
from dotenv import load_dotenv
import random

client = discord.Client()

fortunes = []

@client.event#sends message to python console confirming bot has logged in/ is online
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


@client.event#sends a message when the bot first joins the server
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! Type !cookie to hear your fortune')
        break

        
@client.event #checks if messages are sending commands to the bot and if so, responds accordingly
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!cookie'):
        response = "Here is your fortune: " + random.choice(fortunes)
        await message.channel.send(response)

    if message.content.startswith('!help'):
        response = "Type !cookie to hear your fortune"
        await message.channel.send(response)

load_dotenv(verbose=True)
client.run(os.getenv('TOKEN'))
