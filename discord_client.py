import random
import discord

class DiscordClient(discord.Client):
    def __init__(self, math_jokes_dict):
        super().__init__()
        
        self.math_jokes_dict = math_jokes_dict
        self.math_jokes_dict_len = len(self.math_jokes_dict)

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        random_joke_index = str(random.randint(0, self.math_jokes_dict_len))

        if message.content.startswith('$mathjoke'):
            await message.channel.send(self.math_jokes_dict[random_joke_index])