import os
import discord
from discord import team, message
from discord.client import Client
from discord.ext import commands
from dotenv import load_dotenv
import random
from pymongo import MongoClient

#atipat.pa@ku.th

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')

mongo_url = "Mongo_url"

cluster = MongoClient('mongo_url')
db = cluster["UserData"]
collection = db["UserData"]

def info_user(message):
    print("category : ",message.channel.name)
    print("Author : ",message.author)
    print("Author name : ",message.author.name)
    print("Author ID: ",message.author.id)
    print("message : " ,message.content)
    print('+'*30)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    print(message)
    print(client)
    msg = message.content
    if message.author == client.user:
        return 
    info_user(message)
    print(client.get_all_members())
    await client.process_commands(message)
    if message.content.startswith('นาทัน'):
        await message.channel.send('สวัสดีครับน้องๆExceed')
    

    

@client.command()
async def mem(message):
    # await message.channel.send(", ".join([member.name for member in message.server.members]))
    await message.channel.send(message)

@client.command()
async def meme(message):
    await message.channel.send('https://cdn.marketingoops.com/wp-content/uploads/2017/05/meme-marketing2.png')

@client.command()
async def gif(message):
    await message.channel.send('https://compote.slate.com/images/697b023b-64a5-49a0-8059-27b963453fb1.gif')

@client.command()
async def banana(message):
    await message.channel.send('https://annemurray99.files.wordpress.com/2015/03/huge-dancing-banana-2.gif')

if __name__ == '__main__':
    client.run(TOKEN)   