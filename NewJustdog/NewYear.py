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
 

    
    metla = ["Молния", "Осколок звезды", "Вьюга", "Северный ветер", "Туманная вспышка", "Метла-хтонь", "Чистомёт-2000", "Обычная-метла-дворника-дяди-Валеры", "Эль", "Бездонное ведро"]
    familiar = ["Котопингвин обыкновенный", "Горстка пепла от ежа", "Манул один", "Манул два", "Манул сто", "Саламандра огненная", "Сова генриевитая", "Песец полный", "Мерзопак", "Пушишка", "Камень", "Шлёппи", "Фвупер", "Плотва", "Квокка"]
    mantia = ["Простая мантия", "Согревающая мантия", "Лесная мантия", "Космическая мантия"]
    wand = ['Дампис', 'Ситарри', 'Энеас', 'Кейн', 'Кисмония', 'Нотли', 'Ирнас', 'Удейс', 'Астер', 'Эсме', 'Аманора', 'Эваэль', 'Нисса', 'Мэйв', 'Тарья', 'Зена', 'Вахоне', 'Селеста', 'Ифес', 'Кроу', 'Фавн', 'Эймс', 'Жое']
    elexir = ['Амортенция','Антисглазной лак','Болтливое зелье','Болтушка для молчунов','Вечно прочные ресницы','Волшебный искристый порошок','Драконий тоник','Животворящий эликсир','Зелье красоты','Зелье смеха','Зелье собачьего дыхания','Зелье урчания в животе','Зелье чихания','Икотное зелье','Крысиная микстура','Охранное зелье','Универсальный волшебный пятновыводитель миссис Чистикс',' Феликс Фелицис (жидкая удача)','Целующееся зелье','Эйфорийный эликсир (Эликсир радости)','Экстракт бадьяна']
    cat = ['Кусающая кружка', 'Карликовый декоративный безопасный пушистик', 'Многофункциональный веник', 'Встряска электрическим шоком', 'Бенгальский Китти Поттер огонек', 'Шоколад без последствий (осторожно, могут быть необратимые последствия)', 'Мармеладные живые пиявки', 'Китти-Поттер конфеты', 'Шоколадная живая кошка', 'Подушка-Мяушка']
    pMetla = [10000,9500,9500,9500,9500,8500,9000,8000,8000,4000]
    pFamiliar =[5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
    pMantia = [3000, 5000, 5000, 5000]
    pWand = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
    pElexir = [2000, 1000, 1300, 1400, 1600, 2000, 1900, 2000, 2000, 2000, 2000, 2000, 1500, 1500, 1500, 2000, 1500, 2000, 2000, 1900, 2000]
    pCat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    shop = [metla, familiar, mantia, wand, elexir, cat]
    price = [pMetla, pFamiliar, pMantia, pWand, pElexir, pCat]
    allI = {0: 'car', 1: 'animal', 2: 'coat', 3: 'wand', 4: 'stock', 5: 'cat'}

    attackSpells = ['атака1', 'атака2', 'атака3']
    protectiveSpells = ['защита1', 'защита2']

    with open('NewYear.json', 'r', encoding='utf-8') as p:
        people = json.load(p)
    with open('Duel.json', 'r', encoding='utf-8') as p:
        duel = json.load(p)

    async def update_data(userID, author_name):
        if not str(userID) in people['users']:
            people['users'][userID] = {}
            people['users'][userID]['name'] = author_name
            people['users'][userID]['money'] = 50000
            people['users'][userID]['wand'] = '\u2014'
            people['users'][userID]['coat'] = '\u2014'
            people['users'][userID]['car'] = '\u2014'
            people['users'][userID]['animal'] = '\u2014'
            people['users'][userID]['stock'] = ''
            people['users'][userID]['cat'] = ''
            people['users'][userID]['spending'] = 0


    async def update_duel(userID):
        if not str(userID) in duel['users']:
            duel['users'][userID] = {}
            duel['users'][userID]['hp'] = 100
            duel['users'][userID]['attackSpells'] = []
            duel['users'][userID]['protectiveSpells'] = []
            duel['users'][userID]['win'] = []
            duel['users'][userID]['losing'] = []
            duel['users'][userID]['duelist'] = ''

    
    await update_data(message.author.id, message.author.name)
    await update_duel(message.author.id)        

    async def clear_duel(userID):
        duel['users'][userID]['hp'] = 100
        duel['users'][userID]['attackSpells'] = []
        duel['users'][userID]['protectiveSpells'] = []
        duel['users'][userID]['duelist'] = ''
        

    async def add_spell( userID, spell, attackSpells = True):
        if attackSpells:
            duel['users'][userID]['attackSpells'].append(spell)
        else:
            duel['users'][userID]['protectiveSpells'].append(spell)
    
    async def edit_var(userID, var, value):
        duel['users'][userID][var] = value

    def return_var(userID, var):
        return duel['users'][userID][var]
    
    def return_duelist(userID):
        return duel['users'][userID]['duelist']

    async def damage(duelist):
        await add_var(duelist, 'hp', -random.randint(15,20))

    async def heat(user, duelist, spell):
        await damage(duelist)
        await add_spell(user, spell)
        


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
   
    def check(reaction, userID):
        emoji = ['✅', '❌']
        if userID == message.author and str(reaction.emoji) in emoji:
            ind = emoji.index(reaction.emoji)
            return str(reaction.emoji) and message.author 
   
    async def sell(msg):
        userID = str(msg.author.id)
        msg = str(msg.content)
        for j in range (0,len(shop)):
            for i in range (0,len(shop[j])):
                if shop[j][i] in msg:
                    if int(price[j][i]) <= int(people['users'][userID]['money']):
                        # Подтверждение покупки
                        if people['users'][userID][allI[j]] != '\u2014' and allI[j]!='stock' and allI[j]!='cat':
                            embed = discord.Embed(content = f'{message.author.mention}', description= f'Вы уверены, что хотите купить "' + shop[j][i] + '"?\n Оно займёт место "' + people['users'][userID][allI[j]]+'".', color=0xff0000)
                            sendmessage = await message.channel.send(embed=embed)
                            await sendmessage.add_reaction('✅')
                            await sendmessage.add_reaction('❌')
                            reaction, userok = await bot.wait_for('reaction_add', check=check)
                            if reaction == '❌':
                                await message.add_reaction('❌')
                                return
                        elif allI[j]=='stock':
                            people['users'][userID][allI[j]] += '⚗・' + shop[j][i] + '\n'
                            await spend_money(people,userID, int(price[j][i]))
                            await message.add_reaction('✅')
                            return
                        elif allI[j]=='cat':
                            people['users'][userID][allI[j]] += ':cat2:・' + shop[j][i] + '\n'
                            await spend_money(people,userID, int(price[j][i]))
                            await message.add_reaction('✅')
                            return
                        people['users'][userID][allI[j]] = shop[j][i] 
                        await spend_money(people, userID, int(price[j][i]))
                        await message.add_reaction('✅')
                    else:
                        await message.channel.send('❌ Недостаточно средств')
                        return
    
    async def spend_money(people,userID,value):
        people['users'][userID]['money'] -= value
        people['users'][userID]['spending'] += value

    async def add_var(people,userID,var,value):
        people['users'][userID][var] += value

    async def toCoin(userID):
        if people['users'][userID]['money'] == 0:
            people['users'][userID]['money'] = 50000
            
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

    # elif ('удалитьdddd' in msg):
    # await message.delete()
    # await addrole()
    # print('deleted')

    def checkDuel(reaction, user):
        emoji = ['✅', '❌']
        if user in message.mentions and str(reaction.emoji) in emoji:
            return str(reaction.emoji) and message.mentions[0] 

    if ('дуэль' in words[0]):   
        if len(message.mentions) == 0:
            embed = discord.Embed(description=f'❌ Упомяните существо, которое вы хотите вызвать на дуэль', color=0xff0000)
            await message.channel.send(embed=embed)
            return
        
        #в других местах тоэе в стринг переделать
        userID = str(message.author.id)
        duelistID = str(message.mentions[0].id)

        if return_duelist(duelistID) != '' or return_duelist(userID) != '':
            embed = discord.Embed(description=f'❌ Нельзя вести сразу несколько дуэлей', color=0xff0000)
            await message.channel.send(embed=embed)
            return
        else:
            await edit_var(userID, 'duelist', duelistID)
            await edit_var(duelistID, 'duelist', userID)

            embed = discord.Embed(description=f'{message.author.name} вызывает {message.mentions[0].name} на дуэль', color=0xff0000)
            sendmessage =  await message.channel.send(embed=embed)
            await sendmessage.add_reaction('✅')
            await sendmessage.add_reaction('❌')
            reaction, userok = await bot.wait_for('reaction_add', check=checkDuel)
            
            if reaction == '❌':
                embed = discord.Embed(description=f'{message.author.name}, {message.mentions[0].name} отклонил ваше предложение', color=0xff0000)
                await message.channel.send(embed=embed)
                return
            if reaction == '✅':
                embed = discord.Embed(description=f'Начинается дуэль между {message.author.name} и {message.mentions[0].name} отклонил ваше предложение', color=0xff0000)
                await message.channel.send(embed=embed)
        
            


    if ('купить' in words[0]):   
        await sell(message)

    elif ('гринготтс счет' in msg):
        humanid = str(humanchange(message.author.id, msg))
        human = '<@' + humanid + '>'
        money = people['users'][humanid]['money']
        embed = discord.Embed(description=f'Баланс {human}: {money} галеонов :coin:', color=0xff0000)
        await message.channel.send(embed=embed)

    elif ('магопрофиль' in words[0]):
        await update_data(people,message.author)
        humanid = str(humanchange(message.author.id, msg))
        humanid = str(humanchange(humanid, msg))
        human = '<@' + humanid + '>'
        you = message.author if int(message.author.id)==int(humanid) else message.mentions[0]
        description = f'**Имя:** {human} ('+str(you.name)+') \n🪙・__Галеоны:__ '+str(people['users'][humanid]['money']) +'\n\n🪄・Палочка: '+people['users'][humanid]['wand']+'\n👚・Мантия: '+people['users'][humanid]['coat']+'\n🦉・Фамильяр: '+people['users'][humanid]['animal']+'\n🧹・Метла: '+str(people['users'][humanid]['car'])+'\n**Зелья:**\n'+str(people['users'][humanid]['stock'])+'**Штучки-мяучки:**\n'+str(people['users'][humanid]['cat'])
        embed = discord.Embed(title='Магопрофиль ✨', description=description, color=you.color)

        embed.set_thumbnail(url=you.avatar_url) 
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)
    




    with open('NewYear.json', 'w') as p:
        json.dump(people,p, indent=4)

    with open('Duel.json', 'w') as p:
        json.dump(duel,p, indent=4)

    await bot.process_commands(message)


















    