import os
import discord
from discord import team, message
from discord.client import Client
from discord.ext import commands
from dotenv import load_dotenv
import random
from flask.globals import request
from pymongo import MongoClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')

cluster = MongoClient(os.getenv('MONGO_URL'))
db = cluster.exceed_group16
collection = db.admin_user

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
    if message.author == client.user:
        return 
    info_user(message)
    print(client.get_all_members())
    await client.process_commands(message)
    if 'นาทัน' in message.content:
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

@client.command()
async def add_admin(message):
    user = {}
    user['author_name'] = message.author.name + '#' + message.author.discriminator
    user['name'] = message.author.name
    user['author_ID'] = message.author.id
    user['permission'] = 0
    print(user)
    try:
        filt = {'author_name':user['author_name']}
        already_in = collection.find(filt)
        for ele in already_in:
            return await message.channel.send("พี่เพิ่มไปแล้ว ตั้งใจหน่อยค้าบ")
        collection.insert_one(user)
        await message.channel.send("เพิ่มละค้าบบบบ")
    except:
        await message.channel.send("นาทันงอง")

@client.command()
async def add_permission(message,arg):
    filt2 = {'name':arg} 
    filt = {'author_name': message.author.name + '#' + message.author.discriminator }
    admin = collection.find(filt)
    for ele in admin:
        admin = ele
    if admin["permission"] == 1:
        updated_content = {"$set": {'permission' : 1}}
        collection.update_one(filt2, updated_content)
        await message.channel.send("เป็น admin ละค้าบ")
    else :
        await message.channel.send("พี่ขอไม่ให้ผ่านนะ")




if __name__ == '__main__':
    client.run(TOKEN)   