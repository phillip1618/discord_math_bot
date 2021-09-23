import os
import sentry_sdk

from dotenv import load_dotenv
from discord_client import DiscordClient

load_dotenv()

if (os.getenv('SENTRY_PROD') == 'PROD'): 
    sentry_sdk.init(os.getenv('SENTRY_SDK_INIT'), traces_sample_rate=1.0)


math_jokes_dict = {}

def fill_dict():

    i = 0
    lines = []
    with open('math_jokes.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        math_jokes_dict[str(i)] = line
        i += 1

    return

fill_dict()

client = DiscordClient(math_jokes_dict = math_jokes_dict)
client.run(os.getenv('TOKEN'))
