import discord
import asyncio
from commands import test

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

client.run("Mzc1MzU3MDUyOTIwMzk3ODM3.DNvZ2Q.kJ121b9i0LgIoWacXxIS3AF3FUg")