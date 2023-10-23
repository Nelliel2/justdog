import json
from dotenv import load_dotenv
from discord.ext import commands
import discord
import random
import os
import re
from bot import *


bot = return_bot()
load_dotenv()

@bot.event
async def on_ready():
    print('Бинпап в полном порядке!')

@bot.listen('on_message')
async def bingpupic(message):
    if message.author == bot.user or message.author.bot:
        return
    msg = str(message.content).replace('\n', ' ').replace('ё', 'е').lower().replace(',', '')
    words = re.findall(r'\w+', msg)
    if len(words)==0:
        return
 
    with open('Halloween.json', 'r', encoding='utf-8') as p:
        people = json.load(p)


    def checkAlive():
        if (message.author.top_role.name == "мёртвые"): return False
        if (message.author.top_role.name == "живые?"): return True
        return False

    async def update_data(people,user):
        if not str(user.id) in people['users']:
            people['users'][user.id] = {}
            people['users'][user.id]['name'] = str(user.name)
            if checkAlive():
                people['users'][user.id]['candy'] = 1
                people['users'][user.id]['pumpkin'] = 0
            else:
                people['users'][user.id]['candy'] = 0
                people['users'][user.id]['pumpkin'] = 1               
            people['users'][user.id]['debuff'] = '\u2014'
            people['users'][user.id]['told'] = []


    await update_data(people,message.author)

    def humanchange(humanid, msg):
        if ('@' in msg):
            humanid = ''
            if ('!' in msg):
                for i in range(msg.find('!') + 1, len(msg)):
                    if msg[i] == '>':
                        break
                    humanid += msg[i]
            else:
                for i in range(msg.find('@') + 1, len(msg)):
                    if msg[i] == '>':
                        break
                    humanid += msg[i]
            print(humanid)
        return humanid
   
    async def add_var(people,user,var,value):
        people['users'][user][var] += value


    def check(reaction, user):
        if user == message.author and str(reaction.emoji) == '❌':
            return '❌' and user
        elif user == message.author and str(reaction.emoji) == '❌':
            return '❌' and user
        elif user == message.author and str(reaction.emoji) == '❌':
            return '❌' and user
        elif user == message.author and str(reaction.emoji) == '❌':
            return '❌' and user

    async def story():
        you = message.author
        #description = f'Текст истории'
        #embed = discord.Embed(title='История 🕸️', description=description, color=you.color) 
        embed = discord.Embed(color=you.color) 
        embed.set_author(name = str(you.name), icon_url=you.avatar_url)
        embed.set_footer(text=f'история для {message.mentions[0].name}', icon_url=message.mentions[0].avatar_url)

        sendmessage = await message.channel.send(embed=embed)      

        emoji = ['🤣','❤️','💔'] if (checkAlive()) else ['😱','❤️','💔'] 
        for i in emoji:
            await sendmessage.add_reaction(i)
            reaction, user = await bot.wait_for('reaction_add', check=check)


        

    # def check(reaction, user):
    #         emoji = ['⬅', '➡']
    #         if user == message.author and str(reaction.emoji) in emoji:
    #             ind = emoji.index(reaction.emoji)
    #             return str(reaction.emoji) and message.author 

    # def stock(n):
    #     text = f'**{shop[n][0]}** \n'
    #     for i in range (1,len(shop[n])):
    #         text += shop[n][i] +' — ' + str(price[n][i-1]) + ' \n'
    #     return text

    # if ('косой переулок' in msg):  
    #     n = 0
    #     embed = discord.Embed(title='Косой переулок :convenience_store:', description= f'{stock(n)}', color=0xff0000)
    #     embed.set_footer(text='Напишите: "Купить..."', icon_url=message.author.avatar_url)
    #     sendmessage = await message.channel.send(embed=embed)
    #     await sendmessage.add_reaction('⬅', '➡')
    #     reaction, user = await bot.wait_for('reaction_add', check=check)
    #     if reaction == '⬅':
    #         n += len(stock) if n == 0 else n+1
    #         sendmessage.edit(embed=stock(n)) 
    #     elif reaction == '➡':
    #         n = 0 if n == len(stock) else n-1
    #         sendmessage.edit(embed=stock(n)) 

    async def addrole():
        member = message.author
        guild = bot.guilds[0]
        role = guild.get_role(1046779916756189274)
        print(role)
        await member.add_roles(role)
        

    if ('рассказать' in words[0]): 
        if (len(message.mentions) != 0):  
            await story()
        else:
            textAlive = "мёртвое" if checkAlive() else "живое"          
            await message.channel.send(f'{message.author.mention}, упомяните {textAlive} cущество')          

    elif ('гринготтс счет' in msg):
        humanid = str(humanchange(message.author.id, msg))
        human = '<@' + humanid + '>'
        money = people['users'][humanid]['money']
        embed = discord.Embed(description=f'Баланс {human}: {money} галеонов :coin:', color=0xff0000)
        await message.channel.send(embed=embed)

    elif ('профиль' in words[0]):
        await update_data(people,message.author)
        humanid = str(humanchange(message.author.id, msg))
        humanid = str(humanchange(humanid, msg))
        human = '<@' + humanid + '>'
        you = message.author if int(message.author.id)==int(humanid) else message.mentions[0]

        description = f'**Имя:** {human} ('+str(you.name)+') '+'\n**Состояние:** __'+str(you.roles[1])+'__\n\n '+str(people['users'][humanid]['candy']) +' 🍬      '+str(people['users'][humanid]['pumpkin'])+' 🎃 \n '
        embed = discord.Embed(title='Профиль 🕸️', description=description, color=you.color) 
        embed.set_thumbnail(url=you.avatar_url) 
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)
    




    with open('Halloween.json', 'w') as p:
        json.dump(people,p, indent=4)
    await bot.process_commands(message)


















    