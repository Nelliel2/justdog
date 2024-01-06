import json
from dotenv import load_dotenv
from discord.ext import commands
import discord
import random
import datetime
from datetime import date, timedelta
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
    meal = ['яд', 'кофе', 'какао', 'черный чай', 'зеленый чай', 'горячий шоколад', 'сливочное пиво', 'картоха похогвартски', 'пирог с почками', 'кофе  шотов', 'холодец хуаляни', 'шарлотка поучительски', 'ром полеми', 'отбивные из квокк нелль', 'каменные кексы хагрида', 'минералка', 'мухья в сырном соусе', 'тыквенное печенье', 'медовуха', 'колбаса из программистов детей трансгендеров и фрилансеров', 'веревка и мыло', 'праший чай хуагию', 'чебуреки старейшина', 'морковный пирог', 'огненный виски', 'яичница с плесенью', 'кулюбис', 'горная вода', 'желатиновые червячки', 'медовые ириски', 'летучие шипучки', 'плитка шоколада', 'пестрые пчелки', 'засахаренные ананасы', 'мятные жабы', 'жевательная резинка джубблс', 'драже берти боттс', 'мышкиледышки', 'карамельные бомбы', 'сахарные перья', 'тараканьи гроздья', 'пингвиньи вафли', 'пирог тето это', 'кошачий корм тафф']
    bells = ['Гречки', ' Маслин', ' Какао', ' Соли', ' banano', ' Кактуса', ' Первого свидания с Бездной', ' Предательства в Мафии', ' Долгов в пять миллионов свитеров', ' Кубани на Аляске', ' Мела из Таймырского Муниципального Казенного Общеобразовательного Учреждения «Диксонская средняя Дуршкола» г. СИЦГ', ' Первого заклинателя, прыгнувшего в ирисы', ' Зелёной плесени', ' Желтого снега', ' Чипсиков с лососем', ' Глины', ' Разбитого стекла', ' Мертвого голубя']


    pMetla = [10000,9500,9500,9500,9500,8500,9000,8000,8000,4000]
    pFamiliar =[5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
    pMantia = [3000, 5000, 5000, 5000]
    pWand = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
    pMeal = [5000, 50, 50, 50, 50, 50, 200, 300, 300, 150, 500, 300, 200, 500, 300, 150, 500, 150, 100, 1000, 500, 150, 500, 200, 200, 300, 200, 10000, 50, 50, 60, 65, 50, 70, 100, 99, 50, 60, 80, 100, 300, 1000, 500, 500]
    
    shop = [metla, familiar, mantia, wand, meal]
    price = [pMetla, pFamiliar, pMantia, pWand,  pMeal]
    allI = {0: 'car', 1: 'animal', 2: 'coat', 3: 'wand'}
    
    admins = ['540593371597766673','543016290164670464','553238950865666063', '489750983497482261']  

    attackSpells = ['петрификус тоталус', 'инсендио', 'редукто', 'риктусемпра', 'обскуро', 'серпенсортиа', 'мелофорс', 'лик джинкс', 'диффиндо', 'ешь слизней', 'релашио', 'тентакулус', 'орбис', 'левикорпус']
    attackSpellsDescriptions = ['замораживает противника', 'пытается сжечь противника!', 'взрывает противника!', 'защекотал противника до смерти', 'закрыл противнику глаза', 'призвал змей! противник пропустил удар в пах', 'насадил на голову противника тыкву', 'сглазил противника луком-пореем', 'решил приготовить из противника салат', 'заставляет противника съесть слизней', 'впечатывает противника в стену', 'связывает противника растениями', 'заставляет противника провалиться под землю', 'подвешивает противника за ногу']
    protectiveSpells = ['протего', 'экспеллиармус', 'депульсо', 'иммобулюс']
    protectiveSpellsDescriptions= ['создал вокруг себя щит!', 'выбил у противника палочку!', 'отталкнул противника!', 'заставил противника замереть!']
    forbiddenSpells = ['круциатус', 'империус', 'авада кедавра', 'авадакедавра']




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
            self.defends = 0
            

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
                
                if not self.firstPlayer.spells[-1].atack:
                    self.firstPlayer.defends += 1
                    if self.firstPlayer.defends <= 2:
                        self.secondPlayer.spells[-1].block_damage()
                    else:
                        self.spread_damage()      

                if not self.secondPlayer.spells[-1].atack:
                    self.secondPlayer.defends += 1
                    if self.secondPlayer.defends <= 2:
                        self.firstPlayer.spells[-1].block_damage()
                    else:
                        self.spread_damage()
            else:
                self.spread_damage()

        def spread_damage(self):
            if self.firstPlayer.spells[-1].atack:
                self.damage(self.secondPlayer, self.firstPlayer.spells[-1].damage)
            if self.secondPlayer.spells[-1].atack and not self.is_somebody_dead():
                self.damage(self.firstPlayer, self.secondPlayer.spells[-1].damage)
                
        def get_info(self):
            return f'{self.firstDisplay.hp}❤️ {self.firstDisplay.user.mention} *vs* {self.secondDisplay.user.mention} {self.secondDisplay.hp}❤️', f'{self.get_info_damage(self.firstPlayer)}\n{self.get_info_damage(self.secondPlayer)}'
        
        def get_info_damage(self, body):
            if self.is_somebody_dead():
                if body == self.firstPlayer:
                    return f'{body.user.display_name} {body.spells[-1].get_discription()} -{body.spells[-1].damage} HP'
                elif body == self.get_winner_body():
                     return f'{body.user.display_name} {body.spells[-1].get_discription()} -{body.spells[-1].damage} HP'
                elif body == self.secondPlayer:
                    return ''
            elif body.spells[-1].passing or body.defends >= 3:
                return f'{body.user.display_name} пропустил ход'
            elif not body.spells[-1].atack:
                return f'{body.user.display_name} {body.spells[-1].get_discription()}'
            else:
                return f'{body.user.display_name} {body.spells[-1].get_discription()}! -{body.spells[-1].damage} HP'
            

        def is_somebody_dead(self):
            if self.firstPlayer.hp <= 0 or self.secondPlayer.hp <= 0:
                return True
            else:
                return False

        def get_winner_body(self):
            if self.firstPlayer.hp <= 0:
                return self.secondPlayer
            elif self.secondPlayer.hp <= 0:
                return self.firstPlayer

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
            people['users'][userID]['money'] = 2000
            people['users'][userID]['wand'] = '\u2014'
            people['users'][userID]['coat'] = '\u2014'
            people['users'][userID]['car'] = '\u2014'
            people['users'][userID]['animal'] = '\u2014'
            people['users'][userID]['spending'] = 0
            people['users'][userID]['bells'] = []

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

    async def edit_var_people(userID, var, value):
        people['users'][userID][var] = value

    async def add_var_people(userID, var, value):
        people['users'][userID][var] += value

    def return_var_people(userID, var):
        return people['users'][userID][var]



    async def saveDuel():
        with open('Duel.json', 'w') as p:
            json.dump(duel,p, indent=4)

    async def clearDuel(userID, duelistID):
        duel['users'][userID]['duelist'] = ''
        duel['users'][duelistID]['duelist'] = ''
        await saveDuel()       

    async def edit_var_duel(userID, var, value):
        duel['users'][userID][var] = value

    async def add_var_duel(userID, var, value):
        duel['users'][userID][var] += value

    def return_var_duel(userID, var):
        return duel['users'][userID][var]
    
    def return_duelist(userID):
        "Возвращает id оппонента"
        return duel['users'][userID]['duelist']




    def checkAdmin(id):
        if (id in admins): return True
        else: return False   

    def clean(text):
            cleaned_text = ''
            text = text.replace('ё','е') 
            for char in text.lower():
                if char in 'абвгдежзийклмнопрстуфхцчшщъыьэюя ':
                    cleaned_text += char #cleaned_text = cleaned_text + char
            return cleaned_text

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
        msg = clean(msg).replace('купить ', '')

        if msg in str(meal):
            if int(pMeal[meal.index(msg)]) <= int(people['users'][userID]['money']):
                if msg == 'драже берти боттс':
                    bell = random.choice(bells)
                    if bell not in people['users'][userID]['bells']:
                        people['users'][userID]['bells'].append(bell)
                    await spend_money_bells(people, userID, int(pMeal[meal.index(msg)]))
                    embed = discord.Embed(description=f'Вы получили драже со вкусом {bell}', color=0xff0000)
                    await  message.reply(embed=embed)
                    if len(people['users'][userID]['bells']) == len(bells):
                        embed = discord.Embed(description=f'🎉 Поздравляю! Вы собрали все вкусы!', color=0xff0000)
                        await  message.reply(embed=embed)   
                await spend_money(people, userID, int(pMeal[meal.index(msg)]))
                await message.add_reaction('✅')
                return
            else:
                await message.reply('❌ Недостаточно средств')
                return   
        #Старая продажа
        for j in range (0,len(shop)):
            for i in range (0,len(shop[j])):
                if shop[j][i] in msg:
                    if int(price[j][i]) <= int(people['users'][userID]['money']):
                        # Подтверждение покупки
                        if j < len(allI) and people['users'][userID][allI[j]] != '\u2014':
                            embed = discord.Embed(content = f'{message.author.mention}', description= f'Вы уверены, что хотите купить "' + shop[j][i] + '"?\n Оно займёт место "' + people['users'][userID][allI[j]]+'".', color=0xff0000)
                            sendmessage = await message.channel.send(embed=embed)
                            await sendmessage.add_reaction('✅')
                            await sendmessage.add_reaction('❌')
                            reaction, userok = await bot.wait_for('reaction_add', check=check)
                            if reaction == '❌':
                                await message.add_reaction('❌')
                                return
                            people['users'][userID][allI[j]] = shop[j][i] 
                            await spend_money(people, userID, int(price[j][i]))
                            await message.add_reaction('✅')
                    else:
                        await message.channel.send('❌ Недостаточно средств')
                        return
    
    async def spend_money(people,userID,value):
        people['users'][userID]['money'] -= value

    async def spend_money_bells(people,userID,value):    
        people['users'][userID]['spending'] += value

    async def add_var(people,userID,var,value):
        people['users'][userID][var] += value

    async def toCoin(userID):
        if people['users'][userID]['money'] == 0:
            people['users'][userID]['money'] = 50000

    def GetEmbed(msg):
        embed = discord.Embed(description=msg, color=0xff0000)
        return embed

    def stock(n):
        # text = f'**{shop[n][0]}** \n'
        text = f''
        for i in range (0,len(shop[n])):
            text += shop[n][i] +' — ' + str(price[n][i]) + ' \n'
        embed = discord.Embed(title='Косой переулок :convenience_store:', description= text, color=0xff0000)
        embed.set_footer(text='Напишите: "Купить..."', icon_url=message.author.avatar_url)
        return embed




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
                    

#region Дуэли
                    
    async def saidForbiddenSpell(firstPlayer, secondPlayer):
        await add_var_duel(str(firstPlayer.id), 'losing', 1)
        await add_var_duel(str(secondPlayer.id), 'win', 1)
        await add_var_duel(str(secondPlayer.id), str(datetime.date.today())+'win', 1)
        await add_var_duel(str(firstPlayer.id), str(datetime.date.today())+'losing', 1)
        await edit_var_duel(str(firstPlayer.id), 'ban', str(datetime.date.today()))
        await add_var_people(str(firstPlayer.id), 'money', -150)
        await clearDuel(str(firstPlayer.id), str(secondPlayer.id))
        embed = discord.Embed(description=f'{firstPlayer.mention} теряет  150 галеонов :coin: и сегодня больше не может примать участие в дуэли', color=0x960000)
        await message.channel.send(embed=embed)

    def checkDuel(reaction, user):
        "Проверяет согласие оппонента на дуэль через отправленную реакцию"
        emoji = ['✅', '❌']
        if user in message.mentions and str(reaction.emoji) in emoji:
            return str(reaction.emoji) and message.author  

    async def DuelCanceling():
        embed = discord.Embed(description=f'Дуэль с <@{return_duelist(str(message.author.id))}> отменена', color=0xff0000)
        await  message.channel.send(embed=embed)
        await clearDuel(str(message.author.id), return_duelist(str(message.author.id)))

    async def DuelSpending():

        def checkSpell(message_spell):
            "Проверяет является ли слово заклинанием"
            message_spell.content = clean(message_spell.content)
            if message_spell.author.id == _duel.firstPlayer.id and (str(message_spell.content) in attackSpells or str(message_spell.content) in protectiveSpells or str(message_spell.content) in forbiddenSpells or str(message_spell.content) in "отменить дуэль"):
                return str(message_spell.content) 
            
        _duel = Duel(message.mentions[0], message.author)
        passCon = 0
        
        while not _duel.is_somebody_dead():
            for i in range(0, 2):
                text = f'{_duel.firstPlayer.mention}, произнесите заклинание'
                sendmessage =  await message.channel.send(content=text)

                try:
                    spell = await bot.wait_for('message', check=checkSpell, timeout=40.0)
                    spell.content = clean(spell.content)
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
                    if str(spell.content) in "отменить дуэль":
                        return
                    elif (str(spell.content) in str(_duel.firstPlayer.spells)) or (str(spell.content) in str(_duel.secondPlayer.spells)):
                        _duel.add_spell(_duel.firstPlayer, spell.content, True)
                        text = f'{_duel.firstPlayer.mention}, заклинание "{spell.content}" уже было использовано в этом бою'
                    elif len(_duel.firstPlayer.spells) > 0 and not _duel.firstPlayer.spells[-1].is_spell_atack(str(spell.content)) and _duel.firstPlayer.defends >= 2:
                        _duel.add_spell(_duel.firstPlayer, spell.content, True)
                        text = f'{_duel.firstPlayer.mention}, вы защищаетесь больше 2-ух раз'                    
                    else:
                        _duel.add_spell(_duel.firstPlayer, spell.content, False)
                        text = f'{_duel.firstPlayer.mention} произнес заклинание "{spell.content}"'
                    await sendmessage.edit(content=text)
                    passCon = 0 

                _duel.new_move()

            _duel.heat()    
            title, info = _duel.get_info()
            embed = discord.Embed(description=f'{title}\n', color=0xff0000)
            embed.set_footer(text=f'{info}')
            await message.channel.send(embed=embed)
            _duel.new_move()    


        embed = discord.Embed(description=f'{_duel.get_winner().mention} победил в дуэли! И получает 150 галеонов :coin:', color=0xff0000)
        await message.channel.send(embed=embed)
        await add_var_duel(str(_duel.get_winner().id), 'win', 1)
        await add_var_duel(str(_duel.get_looser().id), 'losing', 1)
        await add_var_duel(str(_duel.get_winner().id), str(datetime.date.today())+'win', 1)
        await add_var_duel(str(_duel.get_looser().id), str(datetime.date.today())+'losing', 1)
        await add_var_people(str(_duel.get_winner().id), 'money', 150)

        await saveDuel()
        await saveData()
        await clearDuel(userID, duelistID)

    
    if ('отменить дуэль' in msg and 'отменить' in words[0]):  
        if return_duelist(str(message.author.id)) != '':
            await DuelCanceling()
        else:
            embed = discord.Embed(description=f'У вас нет активной дуэли', color=0xff0000)
            await message.reply(embed=embed)
        return


    elif ('дуэль' in words[0]):   
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
        if (str(datetime.date.today()) == str(return_var_duel(userID, 'ban'))):
            embed = discord.Embed(description=f'❌ Вам запрещено сегодня участвовать в дуэли', color=0xff0000)
            await message.channel.send(embed=embed)           
            return
        elif (str(datetime.date.today()) == str(return_var_duel(duelistID, 'ban'))):
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
                        
#endregion



#region Топ
    async def topbells(humanID, avatar_url):
        top = []
        for user in duel['users']:
            top.append([return_var_people(str(user),'name'), len(return_var_people(str(user),'bells')), return_var_people(str(user),'spending')])
        top = sorted(top, key=lambda x: x[1], reverse=True) 
        answer = ''
        for i in range(0,10):
            human = top[i][0]
            answer += f'{i+1}. {human} — {top[i][1]} ▲ | {top[i][2]} ▼\n'
        embed = discord.Embed(description=answer, color=0xff0000, title=f'Лучшие покупатели драже 🪄', )
        for i in range(0,1000):
            human = top[i][0]
            if return_var_people(humanID,'name')==human:
                embed.set_footer(text=f'{i+1}. {human} — {top[i][1]} ▲ | {top[i][2]} ▼', icon_url=avatar_url)
                break
        embed.set_image(url='https://media1.tenor.com/m/-sauCodHWLIAAAAd/rainbow-border.gif')
        top.clear()  
        return embed   


    async def top(comparator, comparator2, humanID, avatar_url):
        top = []
        for user in duel['users']:
            top.append([return_var_people(str(user),'name'), return_var_duel(str(user),comparator), return_var_duel(str(user),comparator2)])
        top = sorted(top, key=lambda x: x[1], reverse=True) 
        answer = ''
        for i in range(0,10):
            human = top[i][0]
            answer += f'{i+1}. {human} — {top[i][1]} ▲ | {top[i][2]} ▼\n'
        embed = discord.Embed(description=answer, color=0xff0000, title=f'Лучшие дуэлянты Хогвартса 🪄', )
        for i in range(0,1000):
            human = top[i][0]
            if return_var_people(humanID,'name')==human:
                embed.set_footer(text=f'{i+1}. {human} — {top[i][1]} ▲ | {top[i][2]} ▼', icon_url=avatar_url)
                break
        embed.set_image(url='https://media1.tenor.com/m/-sauCodHWLIAAAAd/rainbow-border.gif')
        top.clear()  
        return embed   

    if checkAdmin(str(message.author.id)):
        
        if ('топ побед общий' in msg and 'топ' in words[0]): 
            await message.channel.send(embed=await top('win', 'losing', str(message.author.id), message.author.avatar_url))

        elif ('топ побед сегодня' in msg and 'топ' in words[0]): 
            date = str(datetime.date.today())
            await message.channel.send(embed=await top(date+'win', date+'losing', str(message.author.id), message.author.avatar_url))

        elif ('топ побед вчера' in msg and 'топ' in words[0]): 
            date = str(datetime.date.today() - timedelta(days=1))
            await message.channel.send(embed=await top(date+'win', date+'losing', str(message.author.id), message.author.avatar_url))

        elif ('топ драже' in msg and 'топ' in words[0]): 
                await message.channel.send(embed=await topbells(str(message.author.id), message.author.avatar_url))

        elif ('даровать' in words[0]):
            if len(message.mentions) > 0:
                num = re.findall(r'\d+', msg)
                try:
                    if str(num[0]) != str(message.mentions[0].id):
                        await add_var_people(str(message.mentions[0].id),'money', int(num[0]))
                        await message.add_reaction('🪄')
                    elif len(num) > 1 and str(num[1]) != str(message.mentions[0].id):
                        await add_var_people(str(message.mentions[0].id),'money', int(num[1]))
                        await message.add_reaction('🪄')
                    else:
                        await message.add_reaction('❌') 
                except:
                    await message.add_reaction('❌') 

        elif ('отнять' in words[0]):
            if len(message.mentions) > 0:
                num = re.findall(r'\d+', msg)
                try:
                    if str(num[0]) != str(message.mentions[0].id):
                        await add_var_people(str(message.mentions[0].id),'money', -1*int(num[0]))
                        await message.add_reaction('🪄')
                    elif len(num) > 1 and str(num[1]) != str(message.mentions[0].id):
                        await add_var_people(str(message.mentions[0].id),'money', -1*int(num[1]))
                        await message.add_reaction('🪄')
                    else:
                        await message.add_reaction('❌') 
                except:
                    await message.add_reaction('❌') 


        elif ('косой переулок' in msg and 'косой' in words[0]):  
            def check(reaction, user):
                emoji = ['⬅', '➡']
                if user == message.author and str(reaction.emoji) in emoji:
                    ind = emoji.index(reaction.emoji)
                    return str(reaction.emoji) and message.author 
            
            n = 0
            sendmessage = await message.channel.send(embed=stock(n))
            await sendmessage.add_reaction('⬅')
            await sendmessage.add_reaction('➡')
            while (True):
                try:
                    reaction, user = await bot.wait_for('reaction_add', check=check, timeout=60)
                except asyncio.TimeoutError:
                    embed = discord.Embed(description=f'Магазин закрыт', color=0xff0000)
                    await sendmessage.edit(embed=embed) 
                    return
                else:
                    print('ok')
                    if str(reaction.emoji) == '⬅':
                        n = len(shop)-1 if n == 0 else n-1
                        await sendmessage.edit(embed=stock(n)) 
                    elif str(reaction.emoji) == '➡':
                        n = 0 if n == len(shop)-1 else n+1
                        await sendmessage.edit(embed=stock(n)) 
#endregion



    if ('купить' in words[0]):   
        await sell(message)

    elif ('гринготтс счет' in msg and 'гринготтс' in words[0]):
        humanid = str(humanchange(message.author.id, msg))
        human = '<@' + humanid + '>'
        money = people['users'][humanid]['money']
        embed = discord.Embed(description=f'Баланс {human}: {money} галеонов :coin:', color=0xff0000)
        await message.channel.send(embed=embed)

    elif ('магопрофиль' in words[0]):     
        humanid = str(humanchange(str(message.author.id), msg))
        humanid = str(humanchange(humanid, msg))
        try:
            await update_data(humanid, humanid)
            human = '<@' + humanid + '>'
            you = message.author if int(message.author.id)==int(humanid) else message.mentions[0]
            description = f'**Имя:** {human} ('+str(you.name)+') \n🪙・__Галеоны:__ '+str(people['users'][humanid]['money']) +'\n\n🪄・Палочка: '+people['users'][humanid]['wand']+'\n👚・Мантия: '+people['users'][humanid]['coat']+'\n🦉・Фамильяр: '+people['users'][humanid]['animal']+'\n🧹・Метла: '+str(people['users'][humanid]['car'])
            embed = discord.Embed(title='Магопрофиль ✨', description=description, color=you.color)
            embed.set_thumbnail(url=you.avatar_url) 
            embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
            await message.channel.send(embed=embed)
        except:
            return

    # elif ('перевод' in words[0]):  
    #     num = re.findall(r'\d+', msg)
    #     if len(message.mentions) > 0:
    #         if True:  
    #             humanID = str(message.mentions[0].id)
    #             human = '<@' + str(message.mentions[0].id) + '>'
    #             humanauthorid = str(message.author.id)
    #             if message.author.mention != human:

    #                 if int(num[0] if num[0] !=humanID else num[1]) <= int(people['users'][humanauthorid]['money']):

    #                     if int(num[0] if num[0] !=humanID else num[1]) >= 0:

    #                         people['users'][humanID]['money'] = int(num[0] if num[0] !=humanID else num[1]) + int(people['users'][humanID]['money'])
    #                         people['users'][humanauthorid]['money'] = int(people['users'][humanauthorid]['money']) - int(num[0] if num[0] !=humanID else num[1])
    #                         embed = discord.Embed(description=f'{int(num[0] if num[0] !=humanID else num[1])} :coin: {human}', color=0xff0000, title='Переведено')                  
    #                     else:
    #                         embed = discord.Embed(description=f'❌ Минимальная сумма перевода 1 :coin:', color=0xff0000)
    #                 else:
    #                     embed = discord.Embed(description=f'❌ Недостаточно средств', color=0xff0000)
    #             else:
    #                 embed = discord.Embed(description=f'💸 Вы не можете передать деньги самому себе', color=0xff0000)
    #             await message.channel.send(embed=embed)
    #         else:
    #             await message.channel.send('💤 Денежные операции временно недоступны')

    await saveDuel()
    await saveData()

    await bot.process_commands(message)


















    