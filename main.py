import discord
import os
from dotenv import load_dotenv

load_dotenv()

math_jokes_dict = {}

def fill_dict():

    i = 0
    lines = []
    with open('math_jokes.txt', 'r', encoding="mbcs") as f:
        lines = f.readlines()

    for line in lines:
        math_jokes_dict[str(i)] = line
        i += 1

    return

fill_dict()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$mathjoke'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))