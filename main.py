import discord
import asyncio
import os
from commands import test
from commands import iplookup

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    yield from test.test(client, message)
    yield from iplookup.iplookup(client, message)


client.run(os.environ.get('BOT_TOKEN'))