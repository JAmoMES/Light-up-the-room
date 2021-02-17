import os
import discord
from discord import team, message
from discord import embeds
from discord.client import Client
from discord.ext import commands
from dotenv import load_dotenv
import random
from flask.globals import request
from pymongo import MongoClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')
client.remove_command('help')

cluster = MongoClient(os.getenv('MONGO_URL'))
db = cluster.exceed_group16
collection = db.admin_user

def embed_send(Title,role,Color,args : tuple):
    embedVar = discord.Embed(title=Title, description=role, color=Color)
    for i in range(0,len(args),2):
        embedVar.add_field(name=args[i], value=args[i+1], inline=False)
    return embedVar

def info_user(message):
    try:
        print("category : ",message.channel.name)
    except:
        pass
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
async def add_user(message):
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
async def add_permission(message,*args):
    if len(args) == 0 :
        return await message.channel.send("นาทันงอง")
    for arg in args:
        filt2 = {'name':arg} 
        filt = {'author_name': message.author.name + '#' + message.author.discriminator }
        admin = collection.find_one(filt)
        if admin["permission"] == 1 or admin["permission"] == 2:
            set_per = collection.find_one(filt2)
            print(set_per)
            if set_per["permission"] != 0:
                return await message.channel.send("ก้มียศละนิครับ")
            updated_content = {"$set": {'permission' : 1}}
            collection.update_one(filt2, updated_content)
            await message.channel.send("เป็น admin ละค้าบ")
        else :
            await message.channel.send("พี่ขอไม่ให้ผ่านนะ")

@client.command()
async def delete_permission(message,*args):
    if len(args) == 0 :
        return await message.channel.send("นาทันงอง")
    for arg in args:
        filt2 = {'name':arg} 
        filt = {'author_name': message.author.name + '#' + message.author.discriminator }
        admin = collection.find_one(filt)
        if admin["permission"] == 2:
            updated_content = {"$set": {'permission' : 0}}
            collection.update_one(filt2, updated_content)
            await message.channel.send("ปัดตกละค้าบ")
        else :
            await message.channel.send("อย่าปีนเกียว")

@client.command()
async def role(message,*args):
    if len(args) == 0:
        filt = {'author_name': message.author.name + '#' + message.author.discriminator }
        admin = collection.find_one(filt)
        if admin["permission"] == 2:
            await message.channel.send("You are Super Admin.")
        elif admin["permission"] == 1:
            await message.channel.send("You are Admin.")
        else :
            await message.channel.send("You are User.")
    else :
        for arg in args:
            filt = {'name': arg}
            admin = collection.find_one(filt)
            try:
                if admin["permission"] == 2:
                    await message.channel.send(f"{admin['name']} is Super Admin.")
                elif admin["permission"] == 1:
                    await message.channel.send(f"{admin['name']} is Admin.")
                else :
                    await message.channel.send(f"{admin['name']} is User.")
            except :
                await message.channel.send(f"Who is {arg} ?")

# @client.command()
# async def color(messege,*args):
#     if len(args) != 2:
#         await message.channel.send("color []")
#     embedVar = embed_send()

@client.command()
async def help(message):
    filt = {'author_name': message.author.name + '#' + message.author.discriminator }
    author = collection.find_one(filt)
    try:
        print (author["permission"])
    except:
        add_user(message=message)
        author = collection.find_one(filt)
    command = ('$add_user','Add you to be new user.')
    command += ('$role','Show your role.')
    if author["permission"] == 0:
        command += ('$color','Change color in your room by \n$color [room] [color1] [color2] ...')
        command += ('$turn_on','Turn on switch in your room by \n$turn_on [room] [color1] [color2] ...')
        command += ('$turn_off','Turn on switch in your room by \n$turn_off [room]')
    else:
        command += ('$add_permission','Change user to be admin by \n$add_permission [user1] ...')
        if author["permission"] == 2:
            command += ('$delete_permission','Change admin to be user by \n$add_permission [user1] ...')
        command += ('$color','Change color in any room by \n$color [room] [color1] [color2] ...')
        command += ('$turn_on','Turn on switch in any room by \n$turn_on [room] [color1] [color2] ...')
        command += ('$turn_off','Turn on switch in any room by \n$turn_off [room]')
    if author["permission"] == 2:
        role = f"These are Super Admin commands."
    elif author["permission"] == 1:
        role = f"These are Admin commands."
    else :
        role = f"These are User commands."
    embedVar = embed_send("What I can help you?",role,0x221222,command)
    await message.channel.send(embed=embedVar)

if __name__ == '__main__':
    client.run(TOKEN)   