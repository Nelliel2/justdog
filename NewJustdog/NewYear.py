import json
from dotenv import load_dotenv
from discord.ext import commands
import discord
import random
import datetime
import os
import re
import asyncio
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


    attackSpells = ['атака1', 'атака2', 'атака3', 'атака4', 'атака5']
    attackSpellsDescriptions = ['атака1!', 'атака2!', 'атака3!', 'атака4!', 'атака5!']
    protectiveSpells = ['защита1', 'защита2']
    protectiveSpellsDescriptions= ['защита1!', 'защита2!']
    forbiddenSpells = ['запрещенка1', 'запрещенка2']




    class Spell:
        def __init__(self, name, passing = False):
            self.name = name
            self.passing = passing
            self.atack = self.is_spell_atack(self.name)
            self.damage = random.randint(25,40) if self.atack and not self.passing else 0

        def __str__(self):
            return self.name
        
        def __repr__(self):
            return self.name

        @staticmethod
        def is_spell_atack(name):
            if name in attackSpells:
                return True
            else:
                return False
            
        def get_discription(self):
            if self.atack:
                return attackSpellsDescriptions[attackSpells.index(self.name)]
            else:
                return protectiveSpellsDescriptions[protectiveSpells.index(self.name)]
            

        def block_damage(self):
            self.damage = 0

    class Player:
        def __init__(self, user, duelist):
            self.user = user
            self.mention = user.mention
            self.id = user.id
            self.duelist = duelist
            self.hp = 100
            self.spells = []
            

        def __str__(self):
            return self.user.name + '#' + self.user.discriminator
        
    class Duel:
        def __init__(self, firstPlayer, secondPlayer):
            self.firstPlayer = Player(firstPlayer, secondPlayer)
            self.secondPlayer = Player(secondPlayer, firstPlayer)

            self.firstDisplay = self.firstPlayer
            self.secondDisplay = self.secondPlayer

        def new_move(self):
            self.firstPlayer, self.secondPlayer = self.secondPlayer, self.firstPlayer

        def damage(self, body, damage):
            body.hp = body.hp - damage

        def add_spell(self, body, spell, passing):
            if spell not in body.spells:
                body.spells.append(Spell(spell, passing))
                return True
            else:
                body.spells.append(Spell(spell, True))
                return False

        def heat(self):
            #Есть ли у кого защита?
            if (not self.firstPlayer.spells[-1].passing and not self.firstPlayer.spells[-1].atack) or (not self.secondPlayer.spells[-1].passing and not self.secondPlayer.spells[-1].atack):
                self.firstPlayer.spells[-1].block_damage()
                self.secondPlayer.spells[-1].block_damage()
            else:
                if self.firstPlayer.spells[-1].atack:
                    self.damage(self.secondPlayer, self.firstPlayer.spells[-1].damage)
                if self.secondPlayer.spells[-1].atack and not self.is_somebody_dead():
                    self.damage(self.firstPlayer, self.secondPlayer.spells[-1].damage)
                
        def get_info(self):
            return f'{self.firstDisplay.hp}❤️ {self.firstDisplay.user.mention} *vs* {self.secondDisplay.user.mention} {self.secondDisplay.hp}❤️', f'{self.get_info_damage(self.firstPlayer)}\n{self.get_info_damage(self.secondPlayer)}'
        
        def get_info_damage(self, body):
            if self.is_somebody_dead():
                if body == self.firstPlayer:
                    return f'{body.user.display_name} {body.spells[-1].get_discription()} и отнимает {body.spells[-1].damage} HP'
                elif body == self.secondPlayer:
                    return ''
            if body.spells[-1].passing:
                return f'{body.user.display_name} пропустил ход'
            elif not body.spells[-1].atack:
                return f'{body.user.display_name} {body.spells[-1].get_discription()}'
            else:
                return f'{body.user.display_name} {body.spells[-1].get_discription()} и отнимает {body.spells[-1].damage} HP'
            

        def is_somebody_dead(self):
            if self.firstPlayer.hp <= 0 or self.secondPlayer.hp <= 0:
                return True
            else:
                return False
            
        def get_winner(self):
            if self.firstPlayer.hp <= 0:
                return self.secondPlayer.user
            elif self.secondPlayer.hp <= 0:
                return self.firstPlayer.user
            
        def get_looser(self):
            if self.firstPlayer.hp <= 0:
                return self.firstPlayer.user
            elif self.secondPlayer.hp <= 0:
                return self.secondPlayer.user
            
            



                

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
            duel['users'][userID]['win'] = 0
            duel['users'][userID]['losing'] = 0
            duel['users'][userID]['duelist'] = ''
            duel['users'][userID]['ban'] = ''

    
    await update_data(str(message.author.id), message.author.name)
    await update_duel(str(message.author.id))        


    async def saveData():
        with open('NewYear.json', 'w') as p:
            json.dump(people,p, indent=4)


    async def clearDuel(userID, duelistID):
        duel['users'][userID]['duelist'] = ''
        duel['users'][duelistID]['duelist'] = ''
        await saveDuel()


    async def saveDuel():
        with open('Duel.json', 'w') as p:
            json.dump(duel,p, indent=4)
        

    async def add_spell(userID, spell, attackSpells = True):
        if attackSpells:
            duel['users'][userID]['attackSpells'].append(spell)
        else:
            duel['users'][userID]['protectiveSpells'].append(spell)
    

    async def edit_var_duel(userID, var, value):
        duel['users'][userID][var] = value

    async def add_var_duel(userID, var, value):
        duel['users'][userID][var] += value

    async def edit_var_people(userID, var, value):
        people['users'][userID][var] = value

    async def add_var_people(userID, var, value):
        people['users'][userID][var] += value

    def return_var(userID, var):
        return duel['users'][userID][var]
    
    def return_duelist(userID):
        "Возвращает id оппонента"
        return duel['users'][userID]['duelist']

    # async def damage(duelist):
    #     "Наносит урон оппоненту"
    #     await add_var(duelist, 'hp', -random.randint(15,20))

    # async def heat(user, duelist, spell):
    #     "Проводит атаку"
    #     await damage(duelist)
    #     await add_spell(user, spell)
        


    def humanchange(humanid, msg):
        "Пытается получить id упомянутого человека, иначе возвращает id автора"
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
    async def saidForbiddenSpell(firstPlayer, secondPlayer):

        await add_var_duel(str(firstPlayer.id), 'losing', 1)
        await add_var_duel(str(secondPlayer.id), 'win', 1)
        await edit_var_duel(str(firstPlayer.id), 'ban', str(datetime.date.today()))
        await add_var_people(str(firstPlayer.id), 'money', -100)
        await clearDuel(firstPlayer.id, secondPlayer.id)
        embed = discord.Embed(description=f'{firstPlayer.mention} теряет  100 галеонов :coin: и сегодня больше не может примать участие в дуэли', color=0x960000)
        await message.channel.send(embed=embed)


    def checkDuel(reaction, user):
        "Проверяет согласие оппонента на дуэль через отправленную реакцию"
        emoji = ['✅', '❌']
        if user in message.mentions and str(reaction.emoji) in emoji:
            return str(reaction.emoji) and message.author 
        
    def GetEmbed(msg):
        embed = discord.Embed(description=msg, color=0xff0000)
        return embed



    async def DuelSpending():

        def checkSpell(message_spell):
            "Проверяет является ли слово заклинанием"
            if message_spell.author.id == _duel.firstPlayer.id and (str(message_spell.content) in attackSpells or str(message_spell.content) in protectiveSpells or str(message_spell.content) in forbiddenSpells):
                return str(message_spell.content) 
            
        _duel = Duel(message.mentions[0], message.author)
        passCon = 0
        
        while not _duel.is_somebody_dead():
            for i in range(0, 2):
                text = f'{_duel.firstPlayer.mention}, произнисите заклинание'
                sendmessage =  await message.channel.send(content=text)

                try:
                    spell = await bot.wait_for('message', check=checkSpell, timeout=30.0)
                except asyncio.TimeoutError:
                    _duel.add_spell(_duel.firstPlayer, '', True)
                    text = f'{_duel.firstPlayer.mention} не произнес заклинание'
                    await sendmessage.edit(content=text)
                    passCon += 1
                    if passCon == 4:
                        text = f'Бой между {_duel.firstPlayer.mention} и {_duel.secondPlayer.mention} отменён'
                        await sendmessage.edit(content=text)
                        await clearDuel(userID, duelistID)
                        return
                else:         
                    if str(spell.content) in forbiddenSpells:
                        await saidForbiddenSpell(_duel.firstPlayer, _duel.secondPlayer) 
                        return
                    elif (str(spell.content) in str(_duel.firstPlayer.spells)) or (str(spell.content) in str(_duel.secondPlayer.spells)):
                        _duel.add_spell(_duel.firstPlayer, spell.content, True)
                        text = f'{_duel.firstPlayer.mention}, заклинание {spell.content} уже было использовано в этом бою'
                    else:
                        _duel.add_spell(_duel.firstPlayer, spell.content, False)
                        text = f'{_duel.firstPlayer.mention} произнес заклинание {spell.content}'
                    await sendmessage.edit(content=text)
                    passCon = 0 

                _duel.new_move()

            _duel.heat()    
            title, info = _duel.get_info()
            embed = discord.Embed(description=f'{title}\n', color=0xff0000)
            embed.set_footer(text=f'{info}')
            await message.channel.send(embed=embed)
            _duel.new_move()    


        embed = discord.Embed(description=f'{_duel.get_winner().mention} победил в дуэли! И получает 100 галеонов :coin:', color=0xff0000)
        await message.channel.send(embed=embed)
        await add_var_duel(str(_duel.get_winner().id), 'win', 1)
        await add_var_duel(str(_duel.get_looser().id), 'losing', 1)
        await add_var_people(str(_duel.get_winner().id), 'money', 100)

        await saveDuel()
        await saveData()
        await clearDuel(userID, duelistID)

        

        
    if ('отменить дуэль' in msg):  
        embed = discord.Embed(description=f'Дуэль с {message.author.mention} отменена', color=0xff0000)
        await  message.channel.send(embed=embed)
        await clearDuel(str(message.author.id), return_duelist(str(message.author.id)))
        return


    if ('дуэль' in words[0]):   
        if len(message.mentions) == 0 and len(words) <= 4:
            embed = GetEmbed(f'❌ Упомяните существо, которое вы хотите вызвать на дуэль')
            await message.channel.send(embed=embed)
            return 
        
        userID = str(message.author.id)
        duelistID = str(message.mentions[0].id)

        try:
            return_duelist(duelistID)
        except:
            embed = discord.Embed(description=f'❌ Упомянутый маг не может участвовать в дуэли', color=0xff0000)
            await message.channel.send(embed=embed)
            return
        if (str(datetime.date.today()) == str(return_var(userID, 'ban'))):
            embed = discord.Embed(description=f'❌ Вам запрещено сегодня участвовать в дуэли', color=0xff0000)
            await message.channel.send(embed=embed)           
            return
        elif (str(datetime.date.today()) == str(return_var(duelistID, 'ban'))):
            embed = discord.Embed(description=f'❌ Упомянутому магу запрещено сегодня участвовать в дуэли', color=0xff0000)
            await message.channel.send(embed=embed)           
            return
        elif return_duelist(duelistID) != '' or return_duelist(userID) != '':
            embed = discord.Embed(description=f'❌ Нельзя вести сразу несколько дуэлей', color=0xff0000)
            await message.channel.send(embed=embed)
            return
        elif duelistID == userID:
            embed = discord.Embed(description=f'❌ Нельзя вести дуэлей с самим собой', color=0xff0000)
            await message.channel.send(embed=embed)
            return
        else:
            await edit_var_duel(userID, 'duelist', duelistID)
            await edit_var_duel(duelistID, 'duelist', userID)
            await saveDuel()

            embed = GetEmbed(f'{message.author.mention} вызывает {message.mentions[0].mention} на дуэль')
            sendmessage = await message.reply(embed=embed)

            await sendmessage.add_reaction('✅')
            await sendmessage.add_reaction('❌')

            try:
                reaction, userok = await bot.wait_for('reaction_add', check=checkDuel, timeout=60)
            except asyncio.TimeoutError:
                embed = GetEmbed(f'{message.mentions[0].mention} не ответил на запрос. Приглашение отменено')
                await message.reply(embed=embed)
                await clearDuel(userID, duelistID)
                return   
            else:             
                if str(reaction.emoji) == '❌':
                    embed = GetEmbed(f'{message.author.mention}, {message.mentions[0].mention} отклонил ваше предложение')
                    await message.reply(embed=embed)
                    await clearDuel(userID, duelistID)
                    return
                elif str(reaction.emoji) == '✅':
                    embed = GetEmbed(f'Начинается дуэль между {message.author.mention} и {message.mentions[0].mention}!') 
                    await message.reply(embed=embed)

                    accident = await DuelSpending()

                    if accident:
                        embed = GetEmbed(f'Дуэль между {message.author.mention} и {message.mentions[0].mention} непредвиденно завершена')
                        await message.reply(embed=embed)
                        
    




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
    






    await saveDuel()
    await saveData()

    await bot.process_commands(message)


















    