import discord
from discord.ext import commands
import random
from random import choice
import time
import re
from random import randint
import json
import nltk
import requests
import string
import os
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import datetime
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from pymorphy2 import MorphAnalyzer
import pickle
import asyncio
from PIL import Image, ImageDraw, ImageFont


load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print('Бинпап в полном порядке!')
import datetime

@bot.listen('on_message')
async def bingpups(message): 
    human = message.author.mention

    msg = str(message.content).replace('\n', ' ')
    msg = msg.replace('бинпап','')



    if ('дурак' in msg):
        pack = []

        hand_user = []
        elder= []

        hand_bingpup = []
        same =[]
        table = []

        colors = ['♥️', '♦️', '♣','♠']
        colors2 = ['♥️', '♦️', '<:club:1002944982732255302>','<:spades:1002944996376326194>']

        #наполнить колоду
        def fullPack():
            for i in range(6, 15):
                pack.append(str(i)+'♥️')
                pack.append(str(i)+'♦️')
                pack.append(str(i)+'♣️')
                pack.append(str(i)+'♠️')

        #наполнить руку
        def fullHand(hand):
                random_card = random.choice(pack)
                hand.append(random_card)
                pack.remove(random_card)

        #раздать карты (не по правилам, тк сначала всё Бинпапу)
        def dealCards():
            while len(pack)!=0:
                if len(hand_bingpup) < 6:
                    fullHand(hand_bingpup)
                elif len(hand_user) < 6:    
                    fullHand(hand_user)           
                else:
                    break
                                            
        def whoMove():
            if botMoving:
                return hand_user, hand_bingpup, elder
            else:
                return hand_bingpup, hand_user, same
    
        async def deleteReactions():
            await sendmessage.clear_reactions()

        async def addStartReactions():
            await deleteReactions()
            emoji = ['1️⃣','2️⃣', '3️⃣','4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
            for i in range(0, len(hand_user)):
                await sendmessage.add_reaction(emoji[i])

        async def addReactions(sendmessage, elder):
            await deleteReactions()
            emoji = ['1️⃣','2️⃣', '3️⃣','4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
            for i in range(0, len(elder)):
                await sendmessage.add_reaction(emoji[i])
            await sendmessage.add_reaction('❌')
            
        def check(reaction, user):
            emoji = ['1️⃣','2️⃣', '3️⃣','4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
            if user == message.author and str(reaction.emoji) in emoji:
                ind = emoji.index(reaction.emoji)
                if botMoving:
                    card = elder[ind]
                elif botMoving == None:
                    card = hand_user[ind]
                else:
                    card = same[ind]
                hand_user.remove(card)
                table.append(card)
                return str(reaction.emoji) and message.author 
            elif user == message.author and str(reaction.emoji) == '❌':
                return '❌' and message.author 

        def botMove(cards_to_go):
            random_card = random.choice(cards_to_go)
            hand_bingpup.remove(random_card)
            table.append(random_card)

        def take(hand):
            for i in range(0, len(table)):
                hand.append(table[i])
            clearTable() 

        def clearTable():
            table.clear()
            elder.clear()
            same.clear()

        #Козыри                   
        def handTrump(hand):
            if trump in table[-1]:
                for i in range(0, len(hand)):
                    if trump not in hand[i] and hand[i] in elder:
                        elder.remove(hand[i])
            else:
                for i in range(0, len(hand)):
                    if trump in hand[i] and hand[i] not in elder:
                        elder.append(hand[i])
            return elder   

        #Старшие
        def findElder(hand, elder):
            elder.clear()
            if len(hand) != 0:
                elder.clear()  
                for i in range(0, len(hand)-1):
                    if (int(hand[i].translate({ord(i): None for i in '♦️♥️♣️♠️'})) > int(table[-1].translate({ord(i): None for i in '♦️♥️♣️♠️'}))): 
                        if table[-1].translate({ord(i): None for i in '0123456789ВДКТ'}) in hand[i]:
                            elder.append(hand[i])
                elder = handTrump(hand)   
                return elder   
             
        #Добавить          
        def findSame(hand, same):
            same.clear()
            if len(hand) != 0:
                same.clear()
                for i in range(0,len(hand)):
                    if int(hand[i].translate({ord(i): None for i in '♦️♥️♣️♠️'})) == int(table[-1].translate({ord(i): None for i in '♦️♥️♣️♠️'})):
                        same.append(hand[i]) 
                return same    
                                                               
        def replaceNames(text):
            replace_values = {'11': 'В', '12': 'Д', '13': 'К', '14': 'Т', '♠️': '<:spades:1002944996376326194>', '♣️': '<:club:1002944982732255302>'}
            for i, j in replace_values.items(): 
                text = text.replace(i, str(j))
            return text
        
        #Обновление стола при добавлении
        def сhangeTable():
            description1 = '**Стол:** \n'
            description2 = ''
            for i in range(1, len(table)+1):
                if i % 2 == 1:
                    description1 += '|' + str(table[i-1]) +'|_   _'
                else:
                    description2 +='|' + str(table[i-1]) +'|_   _'
            return description1 + '\n' + description2
        
        def headEmbed():
            embed=discord.Embed(title=f'Дурак 🃏{trump2} {len(pack)}', url='https://legkonauchim.ru/igry/kak-nauchitsya-igrat-v-duraka-na-kartah-s-nulya', description=replaceNames(сhangeTable()), color=0xff0000)
            embed.set_footer(text='Нажмите на реакцию для выбора карты')

            valueHand = ''
            for i in range(0, len(hand_user)):
                valueHand += '|' + hand_user[i] + '| '
            embed.add_field(name='Рука:', value=replaceNames(valueHand), inline=False)

            valueHand = ''
            for i in range(0, len(hand_bingpup)):
                valueHand += '|' + hand_bingpup[i] + '| '
            embed.add_field(name='Лапа:', value=replaceNames(valueHand), inline=False)
            return embed
        
        def addEmbed(elder, same):
            embed = headEmbed()
            hand1, hand2, field = whoMove()
            elder = findElder(hand1, elder)
            same = findSame(hand2, same) 
            for i in range(0, len(field)):
                embed.add_field(name=f'{i+1}.', value='|'+replaceNames(field[i])+'|', inline=True)
            return embed
            
        def refreshTable():
            embed = headEmbed()
            if not botMoving: #Первый ход человека
                for i in range(0, len(hand_user)):
                    embed.add_field(name=f'{i+1}.', value='|'+replaceNames(hand_user[i])+'|', inline=True)
            return embed 


        fullPack()  
        dealCards() 
        k = random.randint(0, len(colors))
        trump = colors[k]
        trump2 = colors2[k]    

        embed=discord.Embed(title=f'Дурак 🃏{trump2} {len(pack)}', url='https://legkonauchim.ru/igry/kak-nauchitsya-igrat-v-duraka-na-kartah-s-nulya', description='Игра началась!', color=0xff0000)
        sendmessage = await message.channel.send(embed=embed)  

        while len(pack)!=0 and (hand_user !=0 or hand_bingpup !=0):
            
            botMoving = True
            botMove(hand_bingpup)
            while (botMoving or len(hand_bingpup) != 0):   
                #Игрок отбивается
                await sendmessage.edit(embed=addEmbed(elder, same), content = f'{human}, ваш ход!') 
                await addReactions(sendmessage, elder)
                reaction, user = await bot.wait_for('reaction_add', check=check)
                print(reaction)
                await deleteReactions()

                #Бинпап подкидывает
                same = findSame(hand_bingpup, same)
                #Игрок берет
                if str(reaction.emoji) == '❌':
                    take(hand_user)
                    dealCards() 
                #Бито
                elif len(same) == 0 or len(table) == 12:
                    await sendmessage.edit(embed=refreshTable(), content = f'Бито! <a:a_11_bao:997930200467767417>') 
                    time.sleep(random.randint(6,9)) 
                    break
                #Подкидывание
                else:
                    await sendmessage.edit(embed=addEmbed(elder, same), content = f'Ход Бинпапа... <a:a4:854647529093988362>') 
                    table.append(botMove(same))
                    time.sleep(random.randint(6,9))

            botMoving = False 
            clearTable()
            dealCards() 

            #Ход игрока
            await sendmessage.edit(embed=refreshTable(), content = f'{human}, ваш ход!')
            await addStartReactions()
            reaction, user = await bot.wait_for('reaction_add', check=check)

            while (not botMoving or len(hand_user) != 0):
                #Игрок подкидывает
                elder = findElder(hand_bingpup, elder)
                #Бито
                if str(reaction.emoji) == '❌':    
                    await sendmessage.edit(embed=refreshTable(), content = f'Бито! <a:a_11_bao:997930200467767417>') 
                    time.sleep(random.randint(6,9))
                    break
                #Бинпап берет
                elif (len(elder) == 0 or len(table) == 12):
                    take(hand_bingpup)
                    dealCards() 
                    await addStartReactions() 
                    reaction, user = await bot.wait_for('reaction_add', check=check)
                else: 
                    await sendmessage.edit(embed=addEmbed(elder, same), content = f'Ход Бинпапа... <a:a4:854647529093988362>') 
                    table.append(botMove(elder))
                    time.sleep(8)
                    
                    await sendmessage.edit(embed=addEmbed(elder, same), content = f'{human}, ваш ход!') 
                    await addReactions(sendmessage, same)
                    reaction, user = await bot.wait_for('reaction_add', check=check)
                    await deleteReactions()
                    print(reaction)
            clearTable()
            dealCards() 
        print('end')        
        if hand_user == 0:
            await sendmessage.edit(embed=refreshTable(), content = f'{human}, вы победили!')    
        elif hand_bingpup == 0:
            await sendmessage.edit(embed=refreshTable(), content = f'Победа Бинпапа! Гав!')       

                


    if ('удалитьdssd' in msg):
        message = await discord.send_message(discord.channel, 933717449063432202)
        await asyncio.sleep(3) 
        await discord.delete_message(message)

bot.run(os.getenv('BOT_TOKEN'))