import discord
from discord.ext import commands
import random
from random import choice
import time
import re
from random import randint
import json
import os
import nltk
import requests
import string
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
from PIL import Image
intents = discord.Intents.all()
bank = True
load_dotenv()
bot = commands.Bot(command_prefix='!', intents=intents)
OKgoogle = ['что такое', 'окей бинпап']
shop = ['реклама']
price = ['10000']
alphabet =['. ',' ','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
coelum = ['\n','.','એ ','બી ','વી ','જી ','ಎ ','ನ್ ','ም ','რ ','ഞാ ','უ ','ए ','ਡੀ ','అ ','ຂ້ ','າ ','ພ ','ຈົ້ ','ໂ ','Մ ','ভি ','এ ','র ','დ ',' ტ ','ლ ','ಲ್ ','ದು ','ຖ ','ບໍ່ ','ਹੈ ','ਬੀ ','എ ','मैं ']

@bot.event
async def on_ready():
    print('Бинпап в полном порядке!')

@bot.listen('on_message')
async def bingpups(message):
    if message.author == bot.user or message.author.bot:
        return
    msg = str(message.content).replace('\n', ' ').replace('ё', 'е').lower().replace(',', '')
    words = re.findall(r'\w+', msg)
    if len(words)==0:
        return
    humanid = message.author.id
    human = message.author.mention
    humanauthor = message.author.mention
    membs = message.author.guild.members
    people = choice(membs)
    variants = {}
    ints=[]
    num = re.findall(r'\d+', msg)
    with open('lvl.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
    with open('state.json', 'r', encoding='utf-8') as f4:
        fstate = json.load(f4)
    with open('taro.json', 'r', encoding='utf-8') as t:
        tarodis = json.load(t)
    with open('BOT_CONFIG.json', 'r', encoding='utf-8') as f2:
        BOT_CONFIG = json.load(f2)
    with open('BOT_CONFIG2.json', 'r', encoding='utf-8') as f3:
        BOT_CONFIG2 = json.load(f3)
    async def update_data(user):
        if not user in users['users']:
            users['users'][user] = {}
            users['users'][user]['name'] = str(message.author).split('#')[0]
            users['users'][user]['exp'] = 0
            users['users'][user]['lvl'] = 1
            users['users'][user]['bing'] = 0
            users['users'][user]['money'] = 0
            users['users'][user]['angry'] = 0
            users['users'][user]['wife'] = '—'
            users['users'][user]['master'] = '—'
            users['users'][user]['servants'] = '—'
            users['users'][user]['angmsg'] = ''
            users['users'][user]['oldmsg'] = ''
            users['users'][user]['remember'] = ''
            for i in range(5):
                users['users'][user]['seconds'+str(i)] = 0
    async def user_add_var(user,var,value):
        users['users'][user][var] += value
    async def user_equate_var(user,var,value):
         users['users'][user][var] = value
    async def user_add_lvl(user):
        if users['users'][user]['exp'] > users['users'][user]['lvl']*users['users'][user]['lvl']:
            #await message.channel.send(f'{message.author.mention} повысил свой уровень!')
            users['users'][user]['exp'] = 0
            users['users'][user]['lvl'] = users['users'][user]['lvl'] + 1
    def user_return_var(user,var):
        return(users['users'][user][var])
    async def bot_add_state(var):
        value = randint(5,10)
        if (state(var) + value < 100):
            fstate['bingpup'][var] += value
            if ((state('sad') == 1) and (state('clean') >= 60) and (state('hunger') >= 60) and (state('healf') >= 60) and (state('joy') >= 60)):
                fstate['bingpup']['sad'] = 0
        else:
            fstate['bingpup'][var] = 100
    async def on_ping(message):
        if message.mention_everyone:
            return
        elif '<@!707538636580716554>' in message.content:
            if users['users'][str(message.author.id)]['angry'] < 3:
                ment = ['Да, это я!', '> Бинпап, что ты умеешь?', 'Бинпап лучший на свете пес!', 'Гав~']
                await message.channel.send(random.choice(ment)) 
                await message.channel.send('<:bingpup_6:716960326389727253>')
            else:
                ment1 = ['<:bingpup_5:710240672707248238>', '<:bingpup_6:751028614681722920>']
                await message.channel.send(random.choice(ment1))
    async def top(comparator,who,measure):
        top = []
        for user in users['users']:
            top.append(user_return_var(user, 'name'), user_return_var(user, comparator))
        top = sorted(top, key=lambda x: x[1], reverse=True) 
        answer = ''
        for i in range(0,10):
            human = top[i][0]
            answer += f'{i+1}. {human} — {top[i][1]} {measure}\n'
        embed = discord.Embed(description=answer, color=0xff0000, title=f'Лучшие {who} Бинпапа 🌈', )
        for i in range(0,1000):
            human = top[i][0]
            if users['users'][str(humanid)]['name']==human:
                embed.set_footer(text=f'{i+1}. {human} — {top[i][1]} {measure}', icon_url=message.author.avatar_url)
                break
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        top.clear()    
        await message.channel.send(embed=embed)         
    def chatbot_query(query, index=0):
        fallback = 'Извини, я не знаю'
        result = ''

        try:
            search_result_list = list(search(query, tld='co.in', lang='rus', num=10, stop=3, pause=1, country='Russia'))

            page = requests.get(search_result_list[index])

            tree = html.fromstring(page.content)

            soup = BeautifulSoup(page.content, features='lxml')

            article_text = ''
            article = soup.findAll('p')
            for element in article:
                article_text += '\n' + ''.join(element.findAll(text = True))  
            bracket  = 0
            first_sentence = ''
            article_text = article_text.replace('\n', ' ')
            article_text = article_text.replace(' мн.', ' множественное')
            article_text = article_text.replace(' ед.', ' единственное')
            article_text = article_text.replace(' ч.', ' число')
            article_text = article_text.replace(' м.', ' мужской')
            article_text = article_text.replace(' ж.', ' женский')
            article_text = article_text.replace(' р.', ' род')
            article_text = article_text.replace('...', '')
            article_text = article_text.replace(' . ', ' ')
            article_text = article_text.replace('•', ' ')
            article_text = article_text.replace('1.', 'Во-первых,')
            article_text = article_text.replace('2.', 'Во-вторых,')
            article_text = article_text.replace('3.', 'В-третьих,')
            for char in article_text:
                if (char == '(') or (char == '['):
                    bracket = 1
                elif  (char == ')') or (char == ']'):
                    bracket  = 0
                elif char == '.' and bracket == 0:
                    breakout = 1
                    break
                first_sentence = first_sentence + str(char)
            first_sentence = first_sentence.replace('[1]', '')
            first_sentence = first_sentence.replace('[2]', '')
            first_sentence = first_sentence.replace('[3]', '')
            first_sentence = first_sentence.replace('  ', ' ')
            chars_without_whitespace = first_sentence.translate(
                { ord(c): None for c in string.whitespace }
        )

            if len(chars_without_whitespace) > 0:
                result = first_sentence
            else:
                result = fallback
            return result
        except:
            if len(result) == 0: result = fallback
            return result
    def clean(text):
        cleaned_text = ''
        text = text.replace('ё','е') 
        for char in text.lower():
            if char in 'абвгдежзийклмнопрстуфхцчшщъыьэюя ':
                cleaned_text += char #cleaned_text = cleaned_text + char
        return cleaned_text
    def get_intent(msg):   
        """
        with open('our_ml_model.pickle', 'rb') as f0:
            loaded_classifier = pickle.load(f0)
        with open('our_vectorizer.pickle', 'rb') as f0:
            loaded_vectorizer = pickle.load(f0)
        intent = loaded_classifier.predict(loaded_vectorizer.transform([clean(msg)]))[0]
        """
        words2 = re.findall(r'\w+', msg) 
        for intent in BOT_CONFIG['intents'].keys():
            for example in BOT_CONFIG['intents'][intent]['examples']:
                text1 = clean(example)
                words1 = re.findall(r'\w+', text1) 
                text2 = words2[0]
                for i in range(1,len(words1) if len(words1) <= len(words2) else len(words2)):
                    text2 += " " + words2[i]
                distance = nltk.edit_distance(text1, text2) / max(len(text1), len(text2))
                if distance < 0.4: 
                    if ((intent in variants) and (variants[intent] > distance)) or (intent not in variants):
                        variants[intent] = distance         
        intent = min(variants, key=variants.get, default='Не удалось определить интент')
        print(variants)
        print(msg + ' - это намерение ' + min(variants, key=variants.get, default='Не удалось определить интент'))
        variants.clear()
        
        return intent
    def get_intent2(msg):
        for intent in BOT_CONFIG2['intents'].keys():
            for example in BOT_CONFIG2['intents'][intent]['examples']:
                text1 = clean(example)
                text2 = clean(msg)
                distance = nltk.edit_distance(text1, text2) / max(len(text1), len(text2))
                if distance < 0.2: 
                    if ((intent in variants) and (variants[intent] > distance)) or (intent not in variants):
                        variants[intent] = distance         
        intent = min(variants, key=variants.get, default='Не удалось определить интент')
        variants.clear()
        return intent
    def botic(msg):
        intent = get_intent(msg)
        if intent == 'Не удалось определить интент':
            intent = 'yes?'
        return intent
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
    def edit(answer, humanauthor, human, msg, people, angmsg):
        if ('@' in msg):
            human = '<'
            for i in range(msg.find('@'), len(msg)):
                human = human + msg[i]
                if msg[i] == '>':
                    break
        if ('$' in answer):
            m = clean(msg)
            if angmsg != '2':
                for word in BOT_CONFIG['intents'][intent]['examples']:
                    m = m.replace(word, '')
            else:
                for word in BOT_CONFIG2['intents'][intent]['examples']:
                    m = m.replace(word, '')
            replace_values = {' я ': 'ты ', 'бинпап': 'я', 'тебе': 'Бинпапу', 'мне': 'тебе', 'твой': 'Бинпапа', 'мой': 'твой', 'эй ': '', 'меня': 'ты'}
            for i, j in replace_values.items(): 
                m = m.replace(i, str(j))
            offset = datetime.timedelta(hours=3)
            tz = datetime.timezone(offset, name='МСК')
            now = datetime.datetime.now(tz=tz)
            replace_values = {'$mentioned[1, yes]': human, '$authorID': humanauthor, '$randomUser': people, ' $message': m, '$message': m, '$angry': angmsg, '$username': people, '$random[0, 24]': randint(0,23), '$random[0, 60]': randint(0,60), '$random[0, 100]': randint(0,100), '$data': now.strftime('%d-%m-%Y %H:%M:%S')}
            for i, j in replace_values.items(): 
                answer = answer.replace(i, str(j))
        return answer 
    def state(char):
        return fstate['bingpup'][char]
    def answer0(intent):
        return random.choice(BOT_CONFIG['intents'][intent]['rancor' if users['users'][str(message.author.id)]['angry'] > 3 else 'sadness' if state('sad') == 1 else 'responses'])
    def answer1(intent, type):
        return random.choice(BOT_CONFIG['intents'][intent][type])
    def answer2(intent, type):
        return random.choice(BOT_CONFIG2['intents'][intent][type])
    async def bot_subtract_state():
        if time.time() - state('time') > 21600:
            fstate['bingpup']['time'] = round(time.time(),2)
            fstate['bingpup']['clean'] -= randint(3,10)
            fstate['bingpup']['hunger'] -= randint(3,10)
            fstate['bingpup']['healf'] -= randint(3,10)
            fstate['bingpup']['joy'] -= randint(3,10)
            if ((fstate['bingpup']['sad'] == 0) and ((fstate['bingpup']['clean'] <= 60) or (fstate['bingpup']['hunger'] <= 60) or (fstate['bingpup']['hunger'] <= 60) or (fstate['bingpup']['joy'] <= 60))):
                fstate['bingpup']['sad'] = 1
    async def sell(msg):
        if any(word in msg for word in shop):
            for i in range (0,len(shop)):
                if shop[i] in msg:
                    if int(price[i]) <= int(users['users'][str(humanid)]['money']):
                        if 'реклам' in msg:
                            fstate['bingpup']['ad'] = msg.replace('купить реклама ', '')
                        await user_add_var(users,str(message.author.id),'money',-int(price[i]))
                        await message.add_reaction('✅')
                        break
                    else:
                        await message.channel.send('❌ Недостаточно средств')
                        break
    async def taro(ints):
        colms = 3
        thumbnail_width = 356 #509
        thumbnail_height = 591 #845
        size = thumbnail_width, thumbnail_height
        ims = []
        new_im = Image.open('table.jpg').convert('RGBA')
        while len(ims) < 3: #выбор и поврот карт
            x = randint(0, 21)
            if x not in ints:
                ints.append(x)
                im = Image.open(str(x) + '.png').convert('RGBA')
                im.thumbnail(size)
                if len(ims) == 2:
                    im = im.rotate(randint(-10,-5), expand=True)
                else: 
                    im = im.rotate(randint(-10,10), expand=True)
                turn = randint(0,4)
                if turn == 0:
                    im = im.rotate(180, expand=True)
                ims.append(im)
        i = 0
        x = 1700
        y = 50      
        for i in range(colms): #создание картинки 
            print(i, x, y)
            im = ims[i]
            new_im.paste(im, (x, y),mask=im)
            y += 300 + randint(3,10)
            x += -thumbnail_width+ randint(10,20)+40
            x += -40 if i==1 else 0
            y += 100 if i==1 else 0
        new_im.save("Collage.png")
        ims.clear()
    await update_data(str(message.author.id))      
    await bot_subtract_state()
    await on_ping(message)
    if ('где деньги' in msg):
        if bank:
            if (time.time() - int(users['users'][str(message.author.id)]['seconds0']) > 180):
                await user_equate_var(str(message.author.id),'seconds0',round(time.time(),2)) 
                intent = 'money'
                answer = edit(random.choice(BOT_CONFIG2['intents']['money']['responses']), humanauthor, human, msg, people, '')
                embed = discord.Embed(description=answer, color=0xff0000)
                url=random.choice(BOT_CONFIG2['intents']['money']['responses2'])
                embed.set_image(url=url)
                sendmessage = await message.channel.send(embed=embed)
                await asyncio.sleep(10)

                money = randint(500,1000)
                embed = discord.Embed(description=f'{humanauthor} получает {money} 💵', color=0xff0000)
                
                embed.set_image(url=url)
                await sendmessage.edit(embed=embed)
                await user_add_var(users,str(message.author.id),'money',money)
            else:
                await message.channel.send('❌ Денег больше нет. Приходите через 3 минуты')
        else:
            await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('загадать желание' in msg):  
        if len(words) > 2:
            await user_equate_var(users,str(message.author.id),'wish',msg.replace('загадать желание ',''))
            embed = discord.Embed(description=f'🐾 Теперь киньте денежку в колодец ⛲', color=0xff0000)
        else:
            embed = discord.Embed(description=f'❌ Скажите ваше желание', color=0xff0000)
        await message.channel.send(embed=embed)
    elif (('таро' in msg and 'бинпап' in msg) or ('расклад для' in msg) and (len(msg)<4)):
        if round(time.time(),2) - fstate['bingpup']['t'] < 10:
            await message.channel.send('Бинпап еще анализирует предыдущий расклад!')
        else:
            await taro(ints)
            humanid = str(humanchange(humanid, msg))
            human = '<@' + humanid + '>'
            file = discord.File('Collage.png')
            answer = human + '... Вижу, вижу!'
            await message.channel.send(answer, file=file)
            answer = ''
            for i in range(0,3):
                answer += tarodis[str(ints[i])] + '\n'
            ints.clear()
            embed = discord.Embed(title='Описание карт 🃏', description=answer, color=0xff0000)
            tarologs = [users['users'][str(726066980427268097)]['name'], users['users'][str(700223724607242240)]['name'], users['users'][str(661545813138341919)]['name'], users['users'][str(456701198003601409)]['name'], users['users'][str(783253719026368523)]['name']]
            embed.set_footer(text=f'🔮 За подробностями обращайтесь к одному из тарологов: {tarologs[0]}, {tarologs[1]}, {tarologs[2]}, {tarologs[3]} и {tarologs[4]}! 🔮') 
            await message.channel.send(embed=embed)
            fstate['bingpup']['t']=round(time.time(),2)
    elif ('в колодец' in msg):  
        if bank:
            if len(words) >= 3 and words[3].isdigit():
                if int(words[3]) >= 100 and int(words[3]) <= users['users'][str(message.author.id)]['money']:
                    embed = discord.Embed(description=f'🌈 **{human}, ваше желание обязательно исполнится!** ✨\n★’ﾟ･::･｡'+users['users'][str(message.author.id)]['wish'] +'｡･::･ﾟ’☆', color=0xff0000)
                    await user_add_var(users,str(message.author.id),'money',-int(words[3]))
                else:
                    embed = discord.Embed(description=f'❌ Минимальная стоимость желания 100 💵', color=0xff0000)
            else:
                embed = discord.Embed(description=f'❌ Введите сумму пожертвования', color=0xff0000)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('баланс' in words[0]):
            humanid = str(humanchange(humanid, msg))
            human = '<@' + humanid + '>'
            money = users['users'][humanid]['money']
            embed = discord.Embed(description=f'Баланс {human}: {money} 💵', color=0xff0000)
            await message.channel.send(embed=embed)
    elif ('перевести' in words[0]):  
            if bank:
                humanid = str(humanchange(humanid, msg))
                human = '<@' + humanid + '>'
                humanauthorid = str(message.author.id)
                if humanauthor != human:
                    if int(num[0] if num[0] !=humanid else num[1]) <= int(users['users'][humanauthorid]['money']):
                        if int(num[0] if num[0] !=humanid else num[1]) >= 0:
                            users['users'][humanid]['money'] = int(num[0] if num[0] !=humanid else num[1]) + int(users['users'][humanid]['money'])
                            users['users'][humanauthorid]['money'] = int(users['users'][humanauthorid]['money']) - int(num[0] if num[0] !=humanid else num[1])
                            embed = discord.Embed(description=f'{int(num[0] if num[0] !=humanid else num[1])} 💸 {human}', color=0xff0000, title='Переведено')
                        else:
                            embed = discord.Embed(description=f'❌ Минимальная сумма перевода 1 💵', color=0xff0000)
                    else:
                        embed = discord.Embed(description=f'❌ Недостаточно средств', color=0xff0000)
                else:
                    embed = discord.Embed(description=f'💸 Вы не можете передать деньги самому себе', color=0xff0000)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('профиль' in words[0]):
        if 'бпрофиль' in words[0]:
            return
        humanid = str(humanchange(humanid, msg))
        human = '<@' + humanid + '>'
        you = message.author if int(message.author.id)==int(humanid) else message.mentions[0]
        description = f'Ник: {human} ('+str(you.name)+')\nАккаунт создан: '+str(you.created_at)[:10]+'\nЖена: '+users['users'][humanid]['wife']+'\nХозяин: '+users['users'][humanid]['master']+'\nСлуги: '+users['users'][humanid]['servants']+'\nХарактеристики:\n'+str(users['users'][humanid]['lvl'])+' 🏆 '+str(users['users'][humanid]['exp'])+' ⏳ '+str(users['users'][humanid]['money'])+' 💵 '+str(users['users'][humanid]['bing'])+' 🐶\nИнвентарь:\n*пусто~*'
        embed = discord.Embed(title='Бинпрофиль 🌈', description=description, color=you.color)
        ad = fstate['bingpup']['ad']
        embed.set_thumbnail(url=you.avatar_url) 
        embed.set_footer(text=f'💵 Реклама: "{ad}" 💵!') 
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)
    elif ('магазин' in words[0]):    
        embed = discord.Embed(title='Магазин :convenience_store:', description= f':frame_photo: {shop[0]} (в профиле) — {price[0]} :dollar:', color=0xff0000)
        embed.set_footer(text='Напишите: "Купить..."', icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    elif ('купить' in words[0]):   
        if bank:
            await sell(msg)
        else:
            await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('состояние' in words[0] or 'бинпап состояние' in msg):
        embed = discord.Embed(description=f'❤️ - ' + state('joy') + '%  🚿 - ' + state('clean') + '%  💊 - ' + state('healf') + '%  🍖 - ' + state('hunger') + '%', color=0xff0000)
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)
    elif ('забота' in words[0]):
        embed = discord.Embed(description='❤️ **Радость**\nОбнимитесь с Бинпапом, скажите ему какой он хороший, поиграйте с ним в "Бинбон" и поблагодарите его за работу\n\n🚿 **Чистота**\nВымойте Бинпапу лапки, попросите его принять ванну и почистить зубки\n\n💊 **Здоровье**\nЗаставьте Бинпапа бегать, кушать витамины, сидеть в тепле и побольше отдыхать\n\n🍖 **Сытость**\nПокормите Бинпапа\n\n• состояние — текущие показатели Бинпапа', title='Как заботиться о Бинпапе', color=0xff0000)
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)  
    elif ('таймер' in words[0]):
        if len(words) == 3 and words[1].isdigit():
            if 'ч' in msg:
                tm = int(words[1])*60*60
            elif 'м' in msg:
                tm = int(words[1])*60
            else:
                tm = int(words[1])
            print('таймер на ' + str(tm))
            await message.add_reaction('✅')
            await asyncio.sleep(tm)
            embed = discord.Embed(description=f'Время вышло! ' + str(random.choice(['Гав!','Тяф!','Гав-гав"','Вуф!','Афф.'])) + f'\nВы просили напомнить:\n*'+ users['users'][str(message.author.id)]['remember'] +'*', title='Бинтаймер', color=0xff0000)
            embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
            await message.channel.send(humanauthor, embed=embed)    
        else:
            embed = discord.Embed(description=f'❌ Укажите число и единицу времени', color=0xff0000)
            await message.channel.send(embed=embed)     
    elif (('чет' in words[0]) or ('нечет' in words[0])):     
        if (('чет ' in msg) and (len(msg)<4)):
            if bank:
                if len(words) == 2 and words[1].isdigit():
                    if int(words[1]) <= users['users'][str(message.author.id)]['money']:
                        if int(words[1]) >= 0:
                            cube1 = str(randint(0,5))
                            сube2 = str(randint(0,5))
                            print(cube1 + сube2)
                            result = 'чет' if ((int(cube1)+int(сube2)) % 2) == 0 else 'нечет'
                            cube1 = BOT_CONFIG['intents']['roll']['responses'][int(cube1)-1]
                            сube2 = BOT_CONFIG['intents']['roll']['responses'][int(сube2)-1]
                            await message.channel.send(cube1 + сube2)
                            await message.channel.send(random.choice(['<:emoji_21:739609346610298931>', '<:bingpup_12:902268416952512552>', '<:bingbon:902268449168965632>']))
                            if result == words[0]:
                                users['users'][str(humanid)]['money'] += int(words[1])
                                embed = discord.Embed(description=f'**{result.capitalize()}.** {human} получает {int(words[1])} 💵', color=0xff0000)
                            else:
                                users['users'][str(humanid)]['money'] -= int(words[1])
                                embed = discord.Embed(description=f'**{result.capitalize()}.** {human} теряет {int(words[1])} 💸', color=0xff0000)
                        else:
                            embed = discord.Embed(description=f'❌ Минимальная ставка: 1 💵', color=0xff0000)
                    else:
                        embed = discord.Embed(description=f'❌ Недостаточно средств', color=0xff0000)
                else:
                        embed = discord.Embed(description=f'❌ Ваша ставка?', color=0xff0000)
                await message.channel.send(embed=embed)
                await bot_add_state('joy')
            else:
                await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('лучшие' in words[0]):
        if 'друзья' in words[1]:
            await top('lvl', 'друзья', 'ур.')
        elif 'банкиры' in words[1]:
            await top('money', 'банкиры', '💵')
        elif 'бинпапы' in words[1]:
            await top('bing', 'бинпапы', '🐶')
    elif ('бинбон' in words[0]):    
        await message.channel.send("Бинбона больше нет! Говори сразу чет/нечет!")
    elif ('с коэлум' in msg):
        answer = str(message.content).replace('с коэлум ','') + ' '
        for i in range(len(alphabet)):
            answer = answer.replace(coelum[i],alphabet[i])
        await message.channel.send(answer)
    elif ('на коэлум' in msg):
        answer = str(message.content).lower().replace('на коэлум ','')
        for i in range(len(alphabet)):
            answer = answer.replace(alphabet[i],coelum[i])
        await message.channel.send(answer)
    elif ('хто я' in msg):
        await message.add_reaction('<:pyro:942842826633379841>')
        await message.add_reaction('<:hydro:942842826981527592>')
        await message.add_reaction('<:anemo:942842826746658957>')
        await message.add_reaction('<:electro:942842826994114690>')
        await message.add_reaction('<:cryo:942842827048620122>')
        await message.add_reaction('<:geo:942842827019255840>')
    elif ('бинпап что ты умеешь' in msg or 'бинпап help' in msg or 'что умеет бинпап' in msg):
        description = ':pencil: **Знаю команды** :pencil:\n• тапки/носок\n• фас/фу\n• лежать/стоять/бежать/служить/домой\n• дай лапу\n• умри\n• голос\n• ешь/кусай\n• скажи [текст]\n• найди [вещь]\n• принеси [вещь]\n• лови [вещь]\n• обними/согрей\n• в бой\n• к руке/к ноге\n• спать\n• завари чай\n• дай пендаль\n• похвали\n• гулять\n*и другое...*\n\n'
        description += ':crystal_ball: **Подскажу** :crystal_ball:\n• с коэлум/на коэлум [текст]\n• [что-то] или [что-то]\n• кого съедят ирисы\n• зачем/почему \n• где/куда\n• когда\n• кто\n• чьё\n• напомни\n• сколько\n• вероятность\n• возраст\n• цвет\n• дата сегодня\n•что такое [слово]/окей бинпап [вопрос]\n\n'
        description += ':game_die: **Поиграю** :game_die:\n• брось кубик\n• рандом [до]/рандом [от] [до]\n• буква\n• удар\n• забота\n• состояние\n\n'
        description += ':bank: **Деньги** :bank:\n*Для этих команд не нужно писать "Бинпап, "*\n• где деньги\n• баланс\n• перевести [сумма] [упоминание]\n• загадать желание/бросить в колодец\n• чет/нечет [ставка]\n• лучшие [друзья/бинпапы/банкиры]\n• профиль\n• магазин'
        embed = discord.Embed(title='Привет! Я Бинпап', description=description, color=0xff0000)
        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/Yx_PDy7yLOK3dIobeHhXUps6d9bBoZY4CJGJ0HlPzhw/https/pbs.twimg.com/media/EQJz34LU8AEiKfU.jpg') 
        embed.set_footer(text=f'Чтобы обратиться ко мне, пиши "Бинпап, "', icon_url=message.author.avatar_url) 
        await message.channel.send(embed=embed)
    else:
        saybing = 'бинпап' if 'бинпап' in msg else 'нет бинпапа' #Упоминается ли Бинпап?
        if ('бинпапов' in msg or 'бинподенег' in msg):
            return
        msg = clean(msg)
        parasite = ['бинпап', 'эй ', ' и ', ' в ', 'как бы', 'собственно говорят', 'аким образом', 'буквально', 'прямо', 'как говорится', 'так далее', 'скажем', 'ведь', 'как его', 'в натуре', 'так вот', 'короче', 'как сказать', 'видишь', 'слышишь', 'типа', 'на самом деле', 'вообще', 'в общем-то', 'в общем', 'в некотором роде', 'на фиг', 'на хрен', 'в принципе']
        parasite.extend(['итак', 'кстати', 'значит', 'типа того', 'только', 'вот', 'в самом деле', 'данет', 'все такое', 'в целом', 'то есть', 'это', 'это само', 'еешкин кот', 'ну', 'ну вот', 'ну это', 'прикинь', 'прикол', 'значит', 'так сказать', 'понимаешь', 'допустим', 'слушай', 'например', 'просто', 'конкретно', 'да ладно', 'блин', 'походу', 'а-а-а', 'э-э-э', 'не вопрос', 'без проблем', 'практически', 'фактически', 'как-то так', 'ничего себе','пожалуйста'])
        for i in range(len(parasite)):
            msg = msg.replace(parasite[i],'') 
        words = re.findall(r'\w+', msg)
        intent = get_intent2(msg)
        if intent != 'Не удалось определить интент':
            if ('утра' in msg):
                return
            answer = random.choice(BOT_CONFIG2['intents'][intent]['responses'])
            if intent == 'random': #случайное число
                if len(num) == 2:
                    answer += str(randint((int(num[0])),(int(num[1]))))
                elif len(num) == 1:
                    answer += str(randint(0, int(num[0])))
                else:
                    answer = '❌ Введите максимальное число'
            if answer2(intent, 'double') == 'embed': 
                embed = discord.Embed(description=edit(answer, humanauthor, human, msg, people, '2'), color=0xff0000, title=BOT_CONFIG2['intents'][intent]['title'])
                embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
                await message.channel.send(embed=embed)  
            else:
                await message.channel.send(edit(answer, humanauthor, human, msg, people, '2'))
                if answer2(intent, 'double') == ('reactions' or 'reactions&responses2'):
                    await message.add_reaction(random.choice(BOT_CONFIG2['intents'][intent]['reactions']))
                elif answer2(intent, 'double') == ('responses2' or 'reactions&responses2'):
                    answer = answer2(intent, 'responses2')
                    await message.channel.send(edit(answer, humanauthor, human, msg, people, '2'))          

        elif (OKgoogle[0] in msg or OKgoogle[1] in msg):
            if len(msg) < 5:
                for word in OKgoogle:
                    msg = msg.replace(word, '')
                await message.channel.send(chatbot_query(msg))


        elif saybing == 'бинпап': 
            blacklist = ['сказал', 'тогда']
            for i in range(len(blacklist)): #ЧерныйСписок
                if blacklist[i] in msg: 
                    await message.channel.send(answer0('gav')) 
                    await message.channel.send(answer0('bingpup'))
                    return   
            if 'или' in msg:
                words = re.findall(r'\w+', msg)
                answer = words[0]
                i = 1
                while 'или' != words[i]:
                    answer += " " + words[i]
                    i += 1   
                await message.channel.send(random.choice([answer, msg.replace(answer + ' или ', '', 1), f'*совещается с {people}*']))
            
            await user_equate_var(str(message.author.id),'oldmsg',msg)

            intent = botic(msg)
            double = answer1(intent, 'double')
            if user_return_var(str(message.author.id),'oldmsg') == msg:
                answer0('repead') 
                return 
            if intent == 'evil': #добавить злость
                user_add_var(str(message.author.id),'angry',1)
                user_equate_var(str(message.author.id),'angmsg',msg)
            if intent == 'sorry': #убавить злость
                if user_return_var(str(message.author.id),'angry') > 0: 
                    user_add_var(str(message.author.id),'angry',-1)
                elif user_return_var(str(message.author.id),'angry') == 1: 
                    user_equate_var(str(message.author.id),'angmsg','я на тебя не злюсь')
            if double == 'embed':  
                embed = discord.Embed(description=edit(answer, humanauthor, human, msg, people), color=0xff0000, title=answer0(intent, 'title'))
                embed.set_image(url=answer1(intent, 'responses2'))  
                if intent == 'remember':
                    await user_equate_var(users,str(message.author.id),'remember',msg.replace('напомни ',''))
                await message.channel.send(embed=embed)
            sendmessage = await message.channel.send(edit(answer0(intent), humanauthor, human, msg, people, ""))   
            if double == ('reactions' or 'reactions&responses2'): #реакция
                await message.add_reaction(answer1(intent, 'reactions')) 
            elif double == ('responses2' or 'reactions&responses2'): #второе сообщение
                await message.channel.send(edit(answer1(intent, 'responses2') , humanauthor, human, msg, people))
            elif double != ('none' or 'change'): #убавить грусть
                await bot_add_state(double)
                await user_equate_var(users,str(message.author.id),'oldmsg','')
                await user_add_var(users,str(message.author.id),'bing',1)
            if answer1(intent, 'time') > 0: #время 
                    answer = answer1(intent, 'responses2') 
                    await asyncio.sleep(answer1(intent, 'time')) 
                    if double == 'change':
                        await sendmessage.edit(content=edit(answer, humanauthor, human, msg, people))
                    else:
                        await message.channel.send(answer)
            await message.channel.send(answer0('bingpup'))
            await user_add_var(users,str(message.author.id),'exp',1)
            await user_add_lvl(users,str(message.author.id))
            await user_equate_var(users,str(message.author.id),'name',message.author.name)
    with open('state.json', 'w') as f4:
        json.dump(fstate,f4, indent=4)
    with open('lvl.json', 'w') as f:
        json.dump(users,f, indent=4)
    await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))