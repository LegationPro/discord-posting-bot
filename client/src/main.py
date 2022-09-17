import os
import discord
import asyncio

from api import get_tweets

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def fetch_tweets():
    while True:
        a = get_tweets(query="cats")
        print(a)
        await asyncio.sleep(5)


@client.event
async def on_ready():
    client.loop.create_task(fetch_tweets())


    
if __name__ == '__main__':
    client.run(os.getenv("token"))