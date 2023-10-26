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
    try: 
        roleName = message.author.top_role.name    
    except:
        roleName = 'пользователь'


    if len(words)==0:
        return
 
    with open('Halloween.json', 'r', encoding='utf-8') as p:
        people = json.load(p)

    def checkAdmin(role = roleName):
        print(role)
        if (role == "святые и грешники"): return True
        else: return False
        

    def checkGame(role = roleName):
        if (role == "мёртвые"): return True
        elif (role == "живые?"): return True
        else: return False


    def checkAlive(role = roleName):
        if (role == "мёртвые"): return False
        if (role == "живые?"): return True

    def check(reaction, user):
        if user == message.author and str(reaction.emoji) == '❤️':
            return True and user
        elif user == message.author and str(reaction.emoji) == '🖤':
            return True and user
        
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
        return humanid          

    async def update_data(people,user):
        if not str(user.id) in people['users']:
            people['users'][user.id] = {}
            people['users'][user.id]['name'] = str(user.name)
            if checkAlive(user.top_role.name):
                people['users'][user.id]['candy'] = 1
                people['users'][user.id]['pumpkin'] = 0
            else:
                people['users'][user.id]['candy'] = 0
                people['users'][user.id]['pumpkin'] = 1               
            people['users'][user.id]['debuff'] = '\u2014'
            people['users'][user.id]['text'] = ''
            people['users'][user.id]['file'] = False
            people['users'][user.id]['told'] = []

    await update_data(people,message.author)

    try: 
        await update_data(people,message.mentions[0])  
    except:
        ctoto = 123

    async def add_var(user,var,value):
        people['users'][user][var] += value

    async def add_to_arr(user,var,value):
        people['users'][user][var].append(value)

    async def change_var(user,var,value):
        people['users'][user][var] = value
    
    def return_var(user,var):
        return people['users'][user][var]

    async def story():
        you = message.author
        description = return_var(str(message.mentions[0].id),'text')
        embed = discord.Embed(description=description, color=message.mentions[0].color) 

        # embed.set_author(name = str(message.mentions[0].name), icon_url=message.mentions[0].avatar_url)
        # embed.set_footer(text=f'история для {you.name}', icon_url=you.avatar_url)

        embed.set_author(name = f'история для {str(you.name)}', icon_url=you.avatar_url)
        embed.set_footer(text=f'от {message.mentions[0].name}', icon_url=message.mentions[0].avatar_url)

        sendmessage = await message.channel.send(embed=embed)      

        emoji = ['❤️','🖤'] 

        for i in emoji:
            await sendmessage.add_reaction(i)
        reaction, user = await bot.wait_for('reaction_add', check=check)

        if (str(reaction.emoji) == '❤️'):
            await message.channel.send(f'{you.mention} и {message.mentions[0].mention} мирно разошлись')
        elif (str(reaction.emoji) == '🖤'):
            emojiLoss = '🍬' if checkAlive() else '🎃'
            varLoss = 'candy' if checkAlive() else 'pumpkin'
            await add_var(str(message.mentions[0].id), varLoss, -1)
            await message.channel.send(f'-1 {emojiLoss} у {message.mentions[0].mention}')
        
        await add_to_arr(str(you.id),'told', message.mentions[0].id)
        
    async def notStory():
        you = message.author
        embed = discord.Embed(color=you.color) 
        emojiLoss = '🎃' if checkAlive() else '🍬'
        varLoss = 'pumpkin' if checkAlive() else 'candy'

        embed.set_author(name = f'{emojiLoss} для {str(you.name)}', icon_url=you.avatar_url)
        embed.set_footer(text=f'от {message.mentions[0].name}', icon_url=message.mentions[0].avatar_url)
        
        await add_var(str(message.mentions[0].id), varLoss, -1)
        await add_var(str(you.id), varLoss, 1)

        await message.channel.send(f'-1 {emojiLoss} у {message.mentions[0].mention}')
        
        await add_to_arr(str(you.id),'told', message.mentions[0].id)

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

    # async def addrole():
    #     member = message.author
    #     guild = bot.guilds[0]
    #     role = guild.get_role(1046779916756189274)
    #     print(role)
    #     await member.add_roles(role)


    if ('добавить историю' in msg):
        # try:
            answer = str(message.content).replace(words[len(words)-1], '').replace('добавить историю', '')
            if len(message.attachments) > 0:
                userid = str(message.author.id)
                msg = str(message.content)

                await message.attachments[0].save(f'content/'+ userid +'.png')
                # file = discord.File('content/valentine.png')

                await change_var(userid,'file', True)
                await change_var(userid,'text', msg)
                # await user.send(answer, file=file)
            else:
                # await user.send(answer)
                userid = str(message.author.id)
                msg = str(message.content)
                
                await change_var(userid,'file', False)
                await change_var(userid,'text', msg)

            await message.author.send('Я всё записал!')
        # except:
        #     if len(answer)==0:
        #         await message.author.send('Я не могу отправить пустоту, у меня лапки(((')
        #     else:
        #         await message.author.send('Что-то пошло не так!')


    if ('сладость' in words[0] and 'или' in words[1] and 'гадость' in words[2]) or ('гадость' in words[0] and 'или' in words[1] and 'сладость' in words[2]) : 
        if (checkGame()):
            if (len(message.mentions) != 0) and (checkAlive() != checkAlive(message.mentions[0].top_role.name)) and (checkGame(message.mentions[0].top_role.name)):  
                if not (message.mentions[0].id in return_var(str(message.author.id),'told')): 
                    var = 'pumpkin' if checkAlive() else 'candy'
                    if (return_var(str(message.mentions[0].id), var) > 0):
                        await notStory()
                    else:
                        await story()
                else:
                    await message.channel.send(f'{message.author.mention}, вы уже подходили к этому cуществу')              
            else:
                textAlive = "мёртвое" if checkAlive() else "живое"          
                await message.channel.send(f'{message.author.mention}, упомяните {textAlive} cущество')          
        else:
            await message.channel.send(f'{message.author.mention}, вы не участвуете в ивенте')          

    elif ('профиль' in words[0]):   
        humanid = str(humanchange(message.author.id, msg))
        humanid = str(humanchange(humanid, msg))
        human = '<@' + humanid + '>'
        you = message.author if int(message.author.id)==int(humanid) else message.mentions[0]
        textAlive = "живой" if checkAlive(you.top_role.name) else "мёртвый"    

        description = f'**Имя:** {human} ('+str(you.name)+') '+'\n**Состояние:** __'+textAlive+'__\n\n '+str(people['users'][humanid]['candy']) +' 🍬      '+str(people['users'][humanid]['pumpkin'])+' 🎃 \n '
        embed = discord.Embed(title='Профиль 🕸️', description=description, color=you.color) 
        embed.set_thumbnail(url=you.avatar_url) 
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)

    elif ('добавить' in words[0]):
        if checkAdmin():
            if ('тыкву' in words[2]):
                await add_var(str(message.mentions[0].id),'pumpkin', int(words[1]))
                await message.channel.send("Сделано!")
            elif ('конфету' in words[2]):
                await add_var(str(message.mentions[0].id),'candy', int(words[1]))
                await message.channel.send("Сделано!")
    elif ('убрать' in words[0]):
        if checkAdmin():
            if ('тыкву' in words[2]):
                await add_var(str(message.mentions[0].id),'pumpkin', -int(words[1]))
                await message.channel.send("Сделано!")
            elif ('конфету' in words[2]):
                await add_var(str(message.mentions[0].id),'candy', -int(words[1]))
                await message.channel.send("Сделано!")

    with open('Halloween.json', 'w') as p:
        json.dump(people,p, indent=4)

    await bot.process_commands(message)


















    