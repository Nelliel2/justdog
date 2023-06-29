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
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from pymorphy2 import MorphAnalyzer
import pickle
import asyncio
from PIL import Image
from control_state import *
from control_user import *
from bot import *

bank = True
bot = return_bot()
OKgoogle = ['что такое', 'окей бинпап']
shop = ['реклама', 'душа', 'котэ']
price = ['10000', '0', '1']
alphabet =['. ',' ','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
coelum = ['\n','.','એ ','બી ','વી ','જી ','ಎ ','ನ್ ','ም ','რ ','ഞാ ','უ ','ए ','ਡੀ ','అ ','ຂ້ ','າ ','ພ ','ຈົ້ ','ໂ ','Մ ','ভি ','এ ','র ','დ ',' ტ ','ლ ','ಲ್ ','ದು ','ຖ ','ບໍ່ ','ਹੈ ','ਬੀ ','എ ','मैं ']


async def bingpup(message):
    if message.author == bot.user or message.author.bot:
        return
    msg = str(message.content).replace('\n', ' ').replace('ё', 'е').lower().replace(',', '')
    words = re.findall(r'\w+', msg)
    if len(words)==0:
        return
    humanID = str(message.author.id)
    human = message.author.mention
    authorID = str(message.author.id)
    author_mention = message.author.mention
    author_name = message.author.name
    author_avatar = message.author.avatar_url
    try: 
        membs = message.author.guild.members
    except:
        membs = str(message.author)
    people = choice(membs)
    variants = {}
    ints=[]
    num = re.findall(r'\d+', msg)
    with open('BOT_CONFIG.json', 'r', encoding='utf-8') as f2:
        BOT_CONFIG = json.load(f2)
    with open('taro.json', 'r', encoding='utf-8') as t:
        tarodis = json.load(t)
    with open('BOT_CONFIG2.json', 'r', encoding='utf-8') as f3:
        BOT_CONFIG2 = json.load(f3)




    async def on_ping(message):
        if message.mention_everyone:
            return
        elif '<@!707538636580716554>' in message.content:
            if return_user(authorID, 'angry') < 3:
                ment = ['Да, это я!', '> Бинпап, что ты умеешь?', 'Бинпап лучший на свете пес!', 'Гав~']
                await message.channel.send(random.choice(ment)) 
                await message.channel.send('<:bingpup_6:716960326389727253>')
            else:
                ment1 = ['<:bingpup_5:710240672707248238>', '<:bingpup_6:751028614681722920>']
                await message.channel.send(random.choice(ment1))
   
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
    def humanchange(humanID, msg):
        if ('@' in msg):
            humanID = ''
            if ('!' in msg):
                for i in range(msg.find('!') + 1, len(msg)):
                    if msg[i] == '>':
                        break
                    humanID += msg[i]
            else:
                for i in range(msg.find('@') + 1, len(msg)):
                    if msg[i] == '>':
                        break
                    humanID += msg[i]
            print(humanID)
        return humanID
    def edit(answer, author, human, msg, people, angmsg):
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
            replace_values = {'$mentioned[1, yes]': human, '$authorID': author, '$randomUser': people, ' $message': m, '$message': m, '$angry': angmsg, '$username': people, '$random[0, 24]': randint(0,23), '$random[0, 60]': randint(0,60), '$random[0, 100]': randint(0,100), '$data': now.strftime('%d-%m-%Y %H:%M:%S')}
            for i, j in replace_values.items(): 
                answer = answer.replace(i, str(j))
        return answer 
    async def sell(msg):
        if any(word in msg for word in shop):
            for i in range (0,len(shop)):
                if shop[i] in msg:
                    if int(price[i]) <= int(users['users'][str(humanID)]['money']):
                        if 'реклам' in msg:
                            await rewrite_state('ad', msg.replace('купить реклама ', ''))
                        await add_user(str(message.author.id),'money',-int(price[i]))
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
        new_im = Image.open('content/table.jpg').convert('RGBA')
        while len(ims) < 3: #выбор и поврот карт
            x = randint(0, 21)
            if x not in ints:
                ints.append(x)
                im = Image.open('content/' + str(x) + '.png').convert('RGBA')
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
        new_im.save("content/Collage.png")
        ims.clear()
    await update_data(authorID, author_name)      
    await update_state()
    await on_ping(message)
    if ('где деньги' in msg):
        if bank:
            if (time.time() - int(return_user(authorID, 'seconds0')) > 180):
                await rewrite_user(str(message.author.id),'seconds0',round(time.time(),2)) 
                intent = 'money'
                answer = edit(random.choice(BOT_CONFIG2['intents']['money']['responses']), author_mention, human, msg, people, '')
                embed = discord.Embed(description=answer, color=0xff0000)
                url=random.choice(BOT_CONFIG2['intents']['money']['responses2'])
                embed.set_image(url=url)
                sendmessage = await message.channel.send(embed=embed)
                await asyncio.sleep(10)

                money = randint(500,1000)
                embed = discord.Embed(description=f'{author_mention} получает {money} 💵', color=0xff0000)
                
                embed.set_image(url=url)
                await sendmessage.edit(embed=embed)
                await add_user(str(message.author.id),'money',money)
            else:
                await message.channel.send('❌ Денег больше нет. Приходите через 3 минуты')
        else:
            await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('загадать желание' in msg):  
        if len(words) > 2:
            await rewrite_user(str(message.author.id),'wish',msg.replace('загадать желание ',''))
            embed = discord.Embed(description=f'🐾 Теперь киньте денежку в колодец ⛲', color=0xff0000)
        else:
            embed = discord.Embed(description=f'❌ Скажите ваше желание', color=0xff0000)
        await message.channel.send(embed=embed)
    elif ('отправить поздравление' in msg):  
        embed = discord.Embed(title='8 марта!?!?!? 💐🌹🌷🌻', description=f'Агавь! Я разнюхал, что сегодня день бублика, а я очень люблю бублики. Как же хорошо, что у нас Гора бубликов!!\nСпасибо, что вы есть и пить 🥯\nВы самые аппетитные. Вьяф! ❤', color=0xff0000)
        file = discord.File("dog.gif", filename="dog.gif")
        embed.set_image(url="attachment://dog.gif")
        channel2 = bot.get_channel(663909348157947904)
        await channel2.send(file=file, embed=embed)
    elif (('таро' in msg and 'бинпап' in msg) or ('расклад для' in msg) and (len(msg)<4)):
        if ((round(time.time(),2) - return_state('t')) < 5):
            await message.channel.send('Бинпап еще анализирует предыдущий расклад!')
        else:
            await taro(ints)
            humanID = str(humanchange(humanID, msg))
            human = '<@' + humanID + '>'
            file = discord.File('content/Collage.png')
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
            print(round(time.time(),2))
            await rewrite_state('t', round(time.time(),2))
    elif ('бинтинка' in msg):
        try:
            answer = str(message.content).replace(words[len(words)-1], '').replace('бинтинка', '').replace('Бинтинка', '').replace('БИНТИНКА', '')
            user = bot.get_user(int(words[len(words)-1]))
           
            if len(message.attachments) > 0:
                await message.attachments[0].save(f'content/valentine.png')
                file = discord.File('content/valentine.png', filename='valentine.png')
                embed = discord.Embed(title='💗 **Вам пришла Бинтинка!** 💌', description=f'{answer}', color=0xff0000)
                embed.set_image(url='attachment://valentine.png')
                embed.set_footer(text=f'💞 от тайного Бинтина')
                await user.send(embed=embed, file=file)
            else:
                embed = discord.Embed(title='💗 **Вам пришла Бинтинка!** 💌', description=f'{answer}', color=0xff0000)
                embed.set_footer(text=f'💞 от тайного Бинтина')
                await user.send(embed=embed)
            await message.author.send('Отгавлено!')
        except:
            if len(answer)==1 and len(message.attachments) == 0:
                await message.author.send('Я не могу отправить пустоту, у меня лапки(((')
            else:
                await message.author.send('А кому отправить-то? Не понимаю!')
    elif ('в колодец' in msg):  
        if bank:
            if len(words) >= 3 and words[3].isdigit():
                if int(words[3]) >= 100 and int(words[3]) <= return_user(authorID, 'money'):
                    embed = discord.Embed(description=f'🌈 **{human}, ваше желание обязательно исполнится!** ✨\n★’ﾟ･::･｡'+return_user(authorID, 'wish') +'｡･::･ﾟ’☆', color=0xff0000)
                    await add_user(str(message.author.id),'money',-int(words[3]))
                else:
                    embed = discord.Embed(description=f'❌ Минимальная стоимость желания 100 💵', color=0xff0000)
            else:
                embed = discord.Embed(description=f'❌ Введите сумму пожертвования', color=0xff0000)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('баланс' in words[0]):
            humanID = str(humanchange(humanID, msg))
            human = '<@' + humanID + '>'
            money = users['users'][humanID]['money']
            embed = discord.Embed(description=f'Баланс {human}: {money} 💵', color=0xff0000)
            await message.channel.send(embed=embed)
    elif ('перевести' in words[0]):  
            if bank:
                humanID = str(humanchange(humanID, msg))
                human = '<@' + humanID + '>'
                humanauthorid = str(message.author.id)
                if author_mention != human:
                    if int(num[0] if num[0] !=humanID else num[1]) <= int(users['users'][humanauthorid]['money']):
                        if int(num[0] if num[0] !=humanID else num[1]) >= 0:
                            users['users'][humanID]['money'] = int(num[0] if num[0] !=humanID else num[1]) + int(users['users'][humanID]['money'])
                            users['users'][humanauthorid]['money'] = int(users['users'][humanauthorid]['money']) - int(num[0] if num[0] !=humanID else num[1])
                            embed = discord.Embed(description=f'{int(num[0] if num[0] !=humanID else num[1])} 💸 {human}', color=0xff0000, title='Переведено')
                            if humanID == '569641898420076554' and int(num[0] if num[0] !=humanID else num[1]) == 50000:
                                if people['users'][humanauthorid]['money'] == 0:
                                   people['users'][humanauthorid]['money'] = 50000
                                   embed = discord.Embed(description=f'{int(num[0] if num[0] !=humanID else num[1])} 🪙 <@{humanauthorid}>', color=0xff0000, title='Зачислено')
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
        if 'магопрофиль' in words[0]:
            return
        humanID = str(humanchange(humanID, msg))
        human = '<@' + humanID + '>'
        you = message.author if int(message.author.id)==int(humanID) else message.mentions[0]
        description = f'Ник: {human} ('+str(you.name)+')\nАккаунт создан: '+str(you.created_at)[:10]+'\nЖена: '+users['users'][humanID]['wife']+'\nХозяин: '+users['users'][humanID]['master']+'\nСлуги: '+users['users'][humanID]['servants']+'\nХарактеристики:\n'+str(users['users'][humanID]['lvl'])+' 🏆 '+str(users['users'][humanID]['exp'])+' ⏳ '+str(users['users'][humanID]['money'])+' 💵 '+str(users['users'][humanID]['bing'])+' 🐶\nИнвентарь:\n*пусто~*'
        embed = discord.Embed(title='Бинпрофиль 🌈', description=description, color=you.color)
        ad = return_state('ad')
        embed.set_thumbnail(url=you.avatar_url) 
        embed.set_footer(text=f'💵 Реклама: "{ad}" 💵!') 
        embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
        await message.channel.send(embed=embed)
    elif ('магазин' in words[0]):    
        embed = discord.Embed(title='Магазин :convenience_store:', description= f':frame_photo: {shop[0]} (в профиле) — {price[0]} :dollar:\n🌷 {shop[1]} — {price[1]} :dollar: \n🐈 {shop[2]} — {price[2]} :dollar:', color=0xff0000)
        embed.set_footer(text='Напишите: "Купить..."', icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    elif ('купить' in words[0]):   
        if bank:
            await sell(msg)
        else:
            await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('состояние' in words[0] or 'бинпап состояние' in msg):
        embed = discord.Embed(description=f'❤️ - ' + str(return_state('joy')) + '%  🚿 - ' + str(return_state('clean')) + '%  💊 - ' + str(return_state('healf')) + '%  🍖 - ' + str(return_state('hunger')) + '%', color=0xff0000)
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
            embed = discord.Embed(description=f'Время вышло! ' + str(random.choice(['Гав!','Тяф!','Гав-гав"','Вуф!','Афф.'])) + f'\nВы просили напомнить:\n*'+ return_user(authorID, 'remember') +'*', title='Бинтаймер', color=0xff0000)
            embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
            await message.channel.send(author_mention, embed=embed)    
        else:
            embed = discord.Embed(description=f'❌ Укажите число и единицу времени', color=0xff0000)
            await message.channel.send(embed=embed)     
    elif (('чет' in words[0]) or ('нечет' in words[0])):     
        if (('чет ' in msg) and (len(words)<4)):
            if bank:
                if len(words) == 2 and words[1].isdigit():
                    if int(words[1]) <= return_user(authorID, 'money'):
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
                                users['users'][str(humanID)]['money'] += int(words[1])
                                embed = discord.Embed(description=f'**{result.capitalize()}.** {human} получает {int(words[1])} 💵', color=0xff0000)
                            else:
                                users['users'][str(humanID)]['money'] -= int(words[1])
                                embed = discord.Embed(description=f'**{result.capitalize()}.** {human} теряет {int(words[1])} 💸', color=0xff0000)
                        else:
                            embed = discord.Embed(description=f'❌ Минимальная ставка: 1 💵', color=0xff0000)
                    else:
                        embed = discord.Embed(description=f'❌ Недостаточно средств', color=0xff0000)
                else:
                        embed = discord.Embed(description=f'❌ Ваша ставка?', color=0xff0000)
                await message.channel.send(embed=embed)
                await add_state('joy')
            else:
                await message.channel.send('💤 Денежные операции временно недоступны')
    elif ('лучшие' in words[0]):
        if 'друзья' in words[1]:
            await message.channel.send(embed=await top('lvl', 'друзья', 'ур.', humanID, author_avatar))   
        elif 'банкиры' in words[1]:
            await message.channel.send(embed=await top('money', 'банкиры', '💵', humanID, author_avatar))
        elif 'бинпапы' in words[1]:
            await message.channel.send(embed=await top('bing', 'бинпапы', '🐶', humanID, author_avatar))
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
    elif ('спкнч бин' in msg):
        print('Бинпап засыпает!')
        evening = ['Добрых снов!']
        my_channel = bot.get_channel(778933279654936597)
        try:
            await my_channel.send(random.choice(evening)) 
        finally:
            await bot.close()
    elif ('хто я' in msg):
        await message.add_reaction('<:pyro:942842826633379841>')
        await message.add_reaction('<:hydro:942842826981527592>')
        await message.add_reaction('<:anemo:942842826746658957>')
        await message.add_reaction('<:electro:942842826994114690>')
        await message.add_reaction('<:cryo:942842827048620122>')
        await message.add_reaction('<:geo:942842827019255840>')
    #elif ('высший разум' in msg):
    #    maind = ['Высший разум услышал вас?!?','Высший разум призадумался...','Гав? Гав!','*ожидается ответ высшего разума*','Высший разум обязательно ответит...']
    #    await message.channel.send(random.choice(maind))
    #    await message.channel.send(ask(msg.replace('высший разум', '')))
    elif ('бинпап что ты умеешь' in msg or 'бинпап help' in msg or 'что умеет бинпап' in msg):
        description = ':pencil: **Знаю команды** :pencil:\n• тапки/носок\n• фас/фу\n• лежать/стоять/бежать/служить/домой\n• дай лапу\n• умри\n• голос\n• ешь/кусай\n• скажи [текст]\n• найди [вещь]\n• принеси [вещь]\n• лови [вещь]\n• обними/согрей\n• в бой\n• к руке/к ноге\n• спать\n• завари чай\n• дай пендаль\n• похвали\n• гулять\n*и другое...*\n\n'
        description += ':crystal_ball: **Подскажу** :crystal_ball:\n• с коэлум/на коэлум [текст]\n• [что-то] или [что-то]\n• кого съедят ирисы\n• зачем/почему \n• где/куда\n• когда\n• кто\n• чьё\n• напомни\n• сколько\n• вероятность\n• возраст\n• цвет\n• дата сегодня\n•что такое [слово]/окей бинпап [вопрос]\n\n'
        description += ':game_die: **Поиграю** :game_die:\n• брось кубик\n• рандом [до]/рандом [от] [до]\n• буква\n• удар\n• забота\n• состояние\n\n'
        description += ':bank: **Деньги** :bank:\n*Для этих команд не нужно писать "Бинпап, "*\n• где деньги\n• баланс\n• перевести [сумма] [упоминание]\n• загадать желание/бросить в колодец\n• чет/нечет [ставка]\n• лучшие [друзья/бинпапы/банкиры]\n• профиль\n• магазин'
        embed = discord.Embed(title='Привет! Я Бинпап', description=description, color=0xff0000)
        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/Yx_PDy7yLOK3dIobeHhXUps6d9bBoZY4CJGJ0HlPzhw/https/pbs.twimg.com/media/EQJz34LU8AEiKfU.jpg') 
        embed.set_footer(text=f'Чтобы обратиться ко мне, пиши "Бинпап, "', icon_url=message.author.avatar_url) 
        await message.channel.send(embed=embed)
    elif ('обучись123' in msg):
        X, y = [], []
        for intent in BOT_CONFIG['intents']:
            for example in BOT_CONFIG['intents'][intent]['examples']:
                X.append(example)
                y.append(intent)
        """
        morph = MorphAnalyzer()
        def lemmatize(text):
            lemmatized_text = []
            for word in text.lower().split():
                lemmatized_text.append(morph.parse(word)[0].normal_form)
            return ' '.join(lemmatized_text)
        X_train = [lemmatize(text) for text in X_train]
        X_test = [lemmatize(text) for text in X_test]
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
        vectorizer = CountVectorizer(analyzer='word', ngram_range=(1,3))
        vectorizer.fit(X_train)
        X_vectors = vectorizer.transform(X_train)
        classifier = LogisticRegression(max_iter=200)
        classifier.fit(X_vectors, y_train)
        print(classifier.score(X_vectors, y_train))
        print(classifier.score(vectorizer.transform(X_test), y_test))
        with open('our_ml_model.pickle', 'wb') as f0:
            pickle.dump(classifier, f0)
        with open('our_vectorizer.pickle', 'wb') as f0:
            pickle.dump(vectorizer, f0)
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
            if BOT_CONFIG2['intents'][intent]['double'] == 'embed':
                embed = discord.Embed(description=edit(answer, author_mention, human, msg, people, '2'), color=0xff0000, title=BOT_CONFIG2['intents'][intent]['title'])
                embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
                await message.channel.send(embed=embed)  
            else:
                await message.channel.send(edit(answer, author_mention, human, msg, people, '2'))
                if BOT_CONFIG2['intents'][intent]['double'] == ('reactions' or 'reactions&responses2'):
                    await message.add_reaction(random.choice(BOT_CONFIG2['intents'][intent]['reactions']))
                elif BOT_CONFIG2['intents'][intent]['double'] == ('responses2' or 'reactions&responses2'):
                    answer = random.choice(BOT_CONFIG2['intents'][intent]['responses2'])
                    await message.channel.send(edit(answer, author_mention, human, msg, people, '2'))          

        elif (OKgoogle[0] in msg or OKgoogle[1] in msg):
            if len(msg) < 5:
                for word in OKgoogle:
                    msg = msg.replace(word, '')
                await message.channel.send(chatbot_query(msg))


        elif saybing == 'бинпап': 
            blacklist = ['сказал', 'тогда']
            for i in range(len(blacklist)):
                if blacklist[i] in msg:
                    await message.channel.send(random.choice(BOT_CONFIG['intents']['gav']['rancor' if return_user(authorID, 'angry') > 3 else 'sadness' if return_state('sad') == 1 else 'responses'])) 
                    await message.channel.send(random.choice(BOT_CONFIG['intents']['bingpup']['rancor' if return_user(authorID, 'angry') > 3 else 'sadness' if return_state('sad') == 1 else 'responses']))
                    return
            await add_lvl(str(message.author.id))
            if 'или' in msg:
                words = re.findall(r'\w+', msg)
                answer = words[0]
                i = 1
                while 'или' != words[i]:
                    answer += " " + words[i]
                    i += 1   
                await message.channel.send(random.choice([answer, msg.replace(answer + ' или ', '', 1), f'*совещается с {people}*']))
            elif len(words) > 0:
                if return_user(authorID, 'oldmsg') != msg:
                    await rewrite_user(str(message.author.id),'oldmsg',msg)
                    intent = botic(msg)
                    if intent == 'evil': #добавить злость
                        add_user(authorID, 'angry', 1)
                        rewrite_user(authorID, 'angmsg', msg)
                    elif intent == 'sorry': #убавить злость
                        if return_user(authorID, 'angry') > 0: 
                            return_user(authorID, 'angry', -1)
                        elif return_user(authorID, 'angry') == 1: 
                            rewrite_user(authorID, 'angmsg','я на тебя не злюсь')
                    else:
                        angmsg = return_user(authorID, 'angmsg') 
                    if return_user(authorID, 'angry') > 3: #злые сообщения
                        angmsg = return_user(authorID, 'angmsg')
                        answer = random.choice(BOT_CONFIG['intents'][intent]['rancor'])
                        await message.channel.send(edit(answer, author_mention, human, msg, people, angmsg))
                    elif return_state('sad') == 1: #грустные сообщения
                        answer = random.choice(BOT_CONFIG['intents'][intent]['sadness'])
                        angmsg = return_user(authorID, 'angmsg')
                        await message.channel.send(edit(answer, author_mention, human, msg, people, angmsg))
                        if BOT_CONFIG['intents'][intent]['double'] == 'joy' or 'hunger' or 'healf' or 'clean':
                                await add_state(BOT_CONFIG['intents'][intent]['double'])
                                await rewrite_user(str(message.author.id),'oldmsg','')
                                await add_user(str(message.author.id),'bing',1)
                    else: #обычные сообщения
                        answer = random.choice(BOT_CONFIG['intents'][intent]['responses'])
                        if BOT_CONFIG['intents'][intent]['double'] == 'embed':
                            embed = discord.Embed(description=edit(answer, author_mention, human, msg, people, angmsg), color=0xff0000, title=BOT_CONFIG['intents'][intent]['title'])
                            embed.set_image(url=random.choice(BOT_CONFIG['intents'][intent]['responses2']))
                            if intent == 'remember':
                                await rewrite_user(str(message.author.id),'remember',msg.replace('напомни ',''))
                            await message.channel.send(embed=embed)
                        else:
                            sendmessage = await message.channel.send(edit(answer, author_mention, human, msg, people, ""))     
                            if BOT_CONFIG['intents'][intent]['double'] == ('reactions' or 'reactions&responses2'): #реакция
                                await message.add_reaction(random.choice(BOT_CONFIG['intents'][intent]['reactions']))
                            elif BOT_CONFIG['intents'][intent]['double'] == ('responses2' or 'reactions&responses2'): #второе сообщение
                                answer = random.choice(BOT_CONFIG['intents'][intent]['responses2'])
                                await message.channel.send(edit(answer, author_mention, human, msg, people, angmsg))
                            elif BOT_CONFIG['intents'][intent]['double'] != ('none' or 'change'): #убавить грусть
                                await add_state(BOT_CONFIG['intents'][intent]['double'])
                                await rewrite_user(str(message.author.id),'oldmsg','')
                                await add_user(str(message.author.id),'bing',1)
                            if BOT_CONFIG['intents'][intent]['time'] > 0: #время
                                answer = random.choice(BOT_CONFIG['intents'][intent]['responses2'])
                                await asyncio.sleep(BOT_CONFIG['intents'][intent]['time'])
                                if BOT_CONFIG['intents'][intent]['double'] == 'change':
                                    await sendmessage.edit(content=edit(answer, author_mention, human, msg, people, angmsg))
                                else:
                                    await message.channel.send(answer)
                else:
                    await message.channel.send(random.choice(BOT_CONFIG['intents']['repead']['rancor' if return_user(authorID, 'angry') > 3 else 'sadness' if return_state('sad') == 1 else 'responses']))
            else: 
                await message.channel.send(random.choice(BOT_CONFIG['intents']['gav']['rancor' if return_user(authorID, 'angry') > 3 else 'sadness' if return_state('sad') == 1 else 'responses']))  
            await message.channel.send(random.choice(BOT_CONFIG['intents']['bingpup']['rancor' if return_user(authorID, 'angry') > 3 else 'sadness' if return_state('sad') == 1 else 'responses']))
            
            await add_user(str(message.author.id),'exp',1)
            await rewrite_user(str(message.author.id),'name',message.author.name)

    dump_state()
    dump_user()   





    
