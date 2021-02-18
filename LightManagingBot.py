import os
import discord
from discord import team, message,embeds
from discord.client import Client
from discord.ext import commands
from dotenv import load_dotenv
from flask.globals import request
from pymongo import MongoClient
from datetime import datetime

room_size = 2

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')
client.remove_command('help')

cluster = MongoClient(os.getenv('MONGO_URL'))
db = cluster.exceed_group16
collection = db.admin_user
collection_room = db.room_info

def embed_send(Title,role,Color,args : tuple,line=False):
    embedVar = discord.Embed(title=Title, description=role, color=Color)
    for i in range(0,len(args),2):
        embedVar.add_field(name=args[i], value=args[i+1], inline=line)
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

@client.command()
async def color(message,room,*args):
    if len(args) == 0 : 
        await message.channel.send("Error syntax please try...")
        await message.channel.send("$color [room] [color1] [color2] ...")
    elif len(args) > 4:
        await message.channel.send("Error syntax. There is only 4 colors. ")
    author = collection.find_one({'author_name': message.author.name + '#' + message.author.discriminator })
    if author["permission"] >=1 :
        filt = {'ID':int(room),'Time_out' : None }
    else:
        filt = {'ID':int(room),'Time_out' : None ,'Discord' : message.author.name + '#' + message.author.discriminator}
    auth = collection_room.find_one(filt)
    print(auth)
    try:
        print(auth["Discord"])
    except:
        return await message.channel.send("That isn't your room.")
    updated_content = [0,0,0,0]
    str_color = ''
    for ele in args:
        if str(ele).lower() == 'red':
            updated_content[0]= 1
            str_color += 'red '
        elif str(ele).lower() == 'green':
            updated_content[1] = 1
            str_color += 'green '
        elif str(ele).lower() == 'blue':
            updated_content[2] = 1
            str_color += 'blue '
        elif str(ele).lower() == 'white':
            updated_content[3] = 1
            str_color += 'white '
    print(updated_content)
    collection_room.update_one(filt,{'$set' : {'r':updated_content[0]}})
    collection_room.update_one(filt,{'$set' : {'g':updated_content[1]}})
    collection_room.update_one(filt,{'$set' : {'b':updated_content[2]}})
    collection_room.update_one(filt,{'$set' : {'w':updated_content[3]}})
    command = ('change color to...',str_color)
    print(command)
    embedVar = embed_send(f"Room {room}                                        💡",None,0xFFC2E2,command,line=True)
    await message.channel.send(embed=embedVar)

@client.command()
async def login(message,arg):
    filt = {'ID':int(arg),'Time_out' : None ,'Discord' : None}
    author = collection_room.find_one(filt)
    print (author)
    try:
        print(author['ID'])
        updated_content = {'$set' :{'Discord' : message.author.name + '#' + message.author.discriminator}}
        collection_room.update_one(filt,updated_content)
        await message.channel.send('You are now login.')
    except:
        await message.channel.send("You can't login. Please check room status.") 

@client.command()
async def logout(message,arg):
    author = collection.find_one({'author_name': message.author.name + '#' + message.author.discriminator })
    print( author)
    if author["permission"] >=1 :
        filt = {'ID':int(arg),'Time_out' : None }
    else:
        filt = {'ID':int(arg),'Time_out' : None ,'Discord' : message.author.name + '#' + message.author.discriminator}
    # auth = collection_room.find_one(filt)
    # print(auth)
    try:
        info = collection_room.find_one(filt)
        print(info)
        updated_content = {'$set' :{'Discord' : None}}
        collection_room.update_one(filt,updated_content)
        if author["permission"] <1 :
            print(info['Discord'])
            await message.channel.send('You are now logout.')
        else :
            await message.channel.send('Set logout successfully.')
    except:
        await message.channel.send("You don't have permission to set that room information. that isn't your room.") 

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
    command += ('$login','Login in your room by\n$login [room]')
    if author["permission"] == 0:
        command += ('$status',"Show all of the room's status by \n$status or $status [room1] [room2] ..")
        command += ('$color','Change color in your room by \n$color [room] [color1] [color2] ...')
        command += ('$turn_on','Turn on switch in your room by \n$turn_on [room] [color1] [color2] ...')
        command += ('$turn_off','Turn on switch in your room by \n$turn_off [room]')
    else:
        command += ('$add_permission','Change user to be admin by \n$add_permission [user1] ...')
        if author["permission"] == 2:
            command += ('$delete_permission','Change admin to be user by \n$add_permission [user1] ...')
        command += ('$status',"Show all of the room's status by \n$status or $status [room1] [room2] ..")
        command += ('$color','Change color in any room by \n$color [room] [color1] [color2] ...')
        command += ('$turn_on','Turn on switch in any room by \n$turn_on [room] [color1] [color2] ...')
        command += ('$turn_off','Turn on switch in any room by \n$turn_off [room]')
    if author["permission"] == 2:
        role = f"These are Super Admin commands."
    elif author["permission"] == 1:
        role = f"These are Admin commands."
    else :
        role = f"These are User commands."
    embedVar = embed_send("What I can help you?                                         ⚙️",role,0x95FFF7,command)
    await message.channel.send(embed=embedVar)

@client.command()
async def status(message,*args):
    if len(args) == 0:
        filt = {'Time_out':None}
        room = collection_room.find(filt)
        room_num = []
        for i in range(room_size):
            room_num.append('Room '+str(i))
        color_room = ['empty room']*room_size
        for ele in room:
            print(ele)
            if ele["ID"] >= room_size:
                continue
            color_room[ele["ID"]] = 'red '*ele["r"]+'green '*ele["g"]+'blue '*ele["b"]+'white '*ele["w"]
            if len(color_room[ele["ID"]]) == 0:
                color_room[ele["ID"]] = 'no light'
            color_room[ele["ID"]] = "light color :" + color_room[ele["ID"]] 
        status_room = (room_num[0],color_room[0],room_num[1],color_room[1])
        embedVar = embed_send(f"Status                                             💡",None,0xFFC2E2,status_room,line=True)
        await message.channel.send(embed=embedVar)
    else:
        status_room = tuple()
        for room in args:
            filt = {'Time_out':None,'ID':int(room)}
            ele = collection_room.find_one(filt)
            print (ele)
            print (room)
            if ele == None :
                status_room += ('Room ' + str(room)),
                status_room += 'empty room',
                continue
            color_room = 'red '*ele["r"]+'green '*ele["g"]+'blue '*ele["b"]+'white '*ele["w"]
            if len(color_room) == 0:
                color_room = 'no light'
            color_room = "light color :" + color_room
            status_room += ('Room ' + str(room)),
            status_room += color_room,
        embedVar = embed_send(f"Status"+"                    "*len(args)+"💡",None,0xFFC2E2,status_room,line=True)
        await message.channel.send(embed=embedVar)




if __name__ == '__main__':
    client.run(TOKEN)   