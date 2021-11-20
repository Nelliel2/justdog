import discord
from discord import utils
from discord.ext import commands
import random
from random import choice
import time
import re
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
seconds = [0]*10
hello0 = ['привет', 'день', 'вечер', 'утро', ' утра', ' дня', 'вечера', 'дна', 'приветик', 'приветики', ' ку ', ' хай ', 'хэллоу', ' hi ', 'алоха', 'здравствуй']
bye0 = ['пока', 'прощай', 'ухожу', 'покидаю']
slippers0 = ['тапки', 'тапку', 'тапочки', 'тапочка']
war0 = ['бой', 'атака', 'армия']
sleep0 = ['спать', 'засыпай', 'баю бай', 'закрывай глазки', ' спи']
bite0 = ['кусь', 'укуси', 'кусай']
gav0 = ['гав','мяу','кря','ква','гаф','фыр']
die0 = ['я умру','я сдох','я мертв','я погиб','я умер','*умер*','*помер*','*погиб*','*сдох*','я труп']
goodboy = ['я умру', 'я умру',]

@bot.event
async def on_ready():
    print('Бинпап в полном порядке!')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.listen('on_message')
async def bingpups(message):
    if message.author == bot.user or message.author.bot:
        return
    humanid = message.author
    human = message.author.mention
    humanauthor = message.author.mention
    msg = message.content.lower()
    guild = bot.guilds[0]
    membs = message.author.guild.members
    people = choice(membs)
    words = re.findall(r'\w+', msg)
    with open('C:\\Users\\annas\\Documents\\Bingpup\\lvl.json','r') as f:
        users = json.load(f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]['exp'] = 0
            users[user]['lvl'] = 1
            users[user]['bing'] = 0
            users[user]['angry'] = 0
            users[user]['money'] = 0
            for i in range(10):
                users[user]['seconds'+str(i)] = 0
    async def add_exp(users,user,exp):
        users[user]['exp'] += exp
    async def add_bing(users,user,bing):
        users[user]['bing'] += bing
    async def add_angry(users,user,angry):
        users[user]['angry'] += angry
    async def add_money(users,user,money):
        users[user]['money'] += money  
    async def add_seconds(users,user,seconds,k):
        users[user]['seconds'+k] = seconds  
    async def add_lvl(users,user):
        exp = users[user]['exp']
        lvl = users[user]['lvl']
        bing = users[user]['bing']
        if exp > lvl:
            await message.channel.send(f'{message.author.mention} повысил свой уровень!')
            users[user]['exp'] = 0
            users[user]['lvl'] = lvl + 1
    async def on_ping(message):
        if message.mention_everyone:
            return
        elif "<@!707538636580716554>" in message.content:
            if users[str(message.author.id)]['angry'] < 3:
                ment = ["Да, это я!", "> Бинпап, что ты умеешь?", "Бинпап лучший на свете пёс!", "Гав~"]
                await message.channel.send(random.choice(ment)) 
                await message.channel.send("<:bingpup_6:716960326389727253>")
            else:
                ment1 = ["<:bingpup_5:710240672707248238>","<:bingpup_6:751028614681722920>"]
                await message.channel.send(random.choice(ment1))

    await update_data(users,str(message.author.id))      
    await add_lvl(users,str(message.author.id))
    await on_ping(message)


    if message.content.startswith('Бинпап, '):
        await add_exp(users,str(message.author.id),0.1) 
        if any(word in msg for word in hello0): #реакиция
            hello = ['Рад тебя видеть!', 'Хорошо сегодня выглядишь', 'И тебе гав', 'Добрый гав!', 'Я скучал по тебе ', '*Виляет хвостиком* ∪･ω･∪']
            await message.channel.send(random.choice(hello))
            await message.add_reaction('👋🏿')
        elif any(word in msg for word in bye0):
            bye = ['Уже уходишь?(', ' не покидай меня!', f'{humanauthor}, ты не уйдёшь.', 'ээ. давай ещё поговорим!', 'Я не могу без тебя... Я всё думаю о нас', 'Пока :"/', 'Уходи! Дверь закрой']
            await message.channel.send(random.choice(bye))
        elif any(word in msg for word in slippers0):
            slippers = ['<:emoji_23:714248847160770560>', ' <:emoji_24:714249306546372679>', ' <:emoji_25:714249352788312074>', ' <:emoji_26:714249389547192441>']
            await message.channel.send(random.choice(slippers))
        elif any(word in msg for word in war0):
            war = ['ГАВ!!!', ' За Гору и двор стреляю в упор', ' Бинпап №' + random.randint(0, 9) + ' к бою готов!']
            await message.channel.send(random.choice(war))
        elif any(word in msg for word in sleep0):
            sleep = ['Я не умею', ' Но я хочу ещё немного посидеть с тобой!', ' Что такое "спать"?', ' Не хочу. Давай лучше вместе выть на луну❤️', ' *притворился спящим*', ' не в этот месяц', ' *наелся и спит*']
            await message.channel.send(random.choice(sleep))
        elif any(word in msg for word in bite0):
            bite = ['ам ням-ням', ' *кусь*']
            await message.channel.send(random.choice(bite))
            
        if ('@' in msg):
            human = '<'
            for i in range(msg.find('@'), len(msg)):
                human = human + msg[i]
                if msg[i] == '>':
                    break

        elif ('фас ' in msg) or (('фас' in msg) and not('фасо' in msg) and not('фаса' in msg) and not('фасе' in msg)):
                fas = ['***Ррррр***', ' *рычит*', ' (╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻', ' *Скулит*', ' ❌ Бинпап покинул чат', ' Ты справишься сам! <:s_binghe_k_noge1:806178446509735998> Я верю в тебя', ' *злобный тяф!*', '*Воет на луну, в надежде, что она даст ему силы*', 'В которой стороне выход?', f'Мне страшно, {human}!', 'Давайте найдём мирный способ решения проблемы...?', 'Может, чаю?', f'{human}, фас!', 'А я тут при чём?', 'Я пас', f'*укусил {humanauthor}*', '*притворяется мёртвым*', 'Оу, нет, я только что почистил зубы', 'А премия за это полагается?', f'{humanauthor}, уверен, что хочешь узреть мою ужасающую силу?']
                await message.channel.send(random.choice(fas))
        elif ('фу ' in msg) or (('фу' in msg) and not('фуг' in msg) and not('фут' in msg) and not('фур' in msg)):
                fu = ['Бинпап не фу!', ' РррРрРр', ' Сам ты фу!', ' *выплёвывает арбуз*', 'И чего тебе не понравилось?', 'Давай просто обсудим этот момент', 'Уверен, что ты тут главный?', '*остановился*', 'Я не люблю, когда мне приказывают', 'Неа', '*жуёт*']
                await message.channel.send(random.choice(fu))
        elif ('пат-пат' in msg): 
            pat = ['мррр', ' мур-гав', 'а можно ещё?', '*не понимает, что произошло*', 'это... это был пат-пат??', '*радуется*', '*счастливо виляет хвостом*', 'Кто хороший мальчик? Я хороший мальчик!', '*завис*']
            await message.channel.send(random.choice(pat))
        elif ('🥒' in msg): 
            cucumber = ['🥒🥒<:s_binghe_k_noge7:834416426986897449>🥒🥒', ' спасибо, люблю малосольные огурчики!', ' Учитель! Прекрасно выглядите.', ' Большой, длинный, толстый огурец <:s_binghe_k_noge7:834416426986897449> Спасибо!', ' Люблю💚🥒']
            await message.channel.send(random.choice(cucumber))
        elif ('лежать' in msg) or ('лежи' in msg): 
            lay = ['*притворяется мёртвым*', ' только после вас', ' давай потом?', ' Я уже лежу 😑', ' *лежит*']
            await message.channel.send(random.choice(lay))
    
        if ('в ирисы' in msg): 
            v_irisi = ['Помилуйте!!', ' Каюсь. Я больше так не буду :(', ' Я требую адвоката', ' Чуть что и сразу в ирисы?', ' А там есть косточки? *виляет хвостиком*', ' Еда <:s_binghe_k_noge8:783240472138088458>', ' Я сейчас занят. Давай завтра?', ' Надеюсь, в шоколадные? 🍫 <:s_binghe_k_noge6:806172964956930068>', ' Да, давно там не был! :>', 'Ириски! Уже соскучился по ним', 'Интересно, останутся ли от меня косточки...', 'Ты меня не любишь?']
            await message.channel.send(random.choice(v_irisi))
        elif ('ирисы' in msg) or ('ирисах' in msg):
            irisi = ['вкусняшка?', ' *жуёт цветок*', ' люблю эти цветы!💐', f'*вручает букет {humanauthor}', ' тяф?', 'Прекрасные цветы!', 'Люблю их аромат', 'Я скучаю по ним...', 'Да, Бинпап живёт в ирисах', 'иРиСы! Мои любимые', 'Надеюсь, Учитель не забывает их кормить...', 'А кто сейчас там?', f'{humanauthor}, тоже скучаешь по ним?((']
            await message.channel.send(random.choice(irisi))
        if ('к руке' in msg) and (time.time() - users[str(message.author.id)]['seconds0'] > 60): #кулдаун
            await add_seconds(users,str(message.author.id),round(time.time(),2),str(0)) 
            ruka = ['уже бегу!', '*выбирает левую руку* 🤚🏿', '*выбирает правую руку* 👊🏿', 'тоже хочу руки', ' *прыгает и кусает за руку*', ' Будет исполнено!', ' Тяф точно!', '*пожимает руку* 🤝', 'к которой?', 'ох, мне так нравятся твои руки!', 'красивый маникюр', '*лизнул руку*', '*думает какую выбрать руку*', f'*медленно подошёл к {human}*', f'*взял {human} за ручку*  Пойдём-пойдём']
            await message.channel.send(random.choice(ruka))
        elif ('к руке' in msg):
            await message.channel.send('Бинпап уже здесь')

        elif ('учитель' in msg): 
            await message.channel.send('<:n_hua_cheng2:834401540759486484>🥒')
        elif ('лапу' in msg) or ('лапой' in msg): 
            await message.channel.send('<:work_1:709195275725439027>')

        if ('голос' in words[1]): #случайный пользователь
            await message.channel.send(f'Голосую за {people.name}!')
        elif ('голос' in msg):
            golos = ['Не думаю, что в этом есть смысл', 'Гав!', '*Эээээто Голос!*', 'у меня бас']
            await message.channel.send(random.choice(golos))
        if ('кто' in words[1]): 
            if ('бинпап' or 'хороший' in words[2]) and ('бинпап' or 'хороший' in words[3]) and ('ты' in words[3]):
                who = ['Ходят слухи, что это Бинпап', ' Несомненно, Бинпап', ' Гав-гав? Бинпап!', 'Носом чую, что Бинпап', ' Очевидно, Бинпап', 'откуда я знаю']
            else:
                who = [f'Ходят слухи, что это {people.name}', f' Несомненно, {people.name}', f' Гав-гав? {people.name}!', f'Носом чую, что {people.name}', f' Очевидно, {people.name}', 'откуда я знаю']
            await message.channel.send(random.choice(who))
        elif ('кого' in words[1]): 
            kogo = [f'Я слышал, что {people.name}', f'Скорее всего, {people.name}', f'Гав? {people.name}!', f'Носом чую, что {people.name}', f'Очевидно, {people.name}', 'откуда я знаю', f'*жуёт {people.name}*  Ты что-то хотел?']
            await message.channel.send(random.choice(kogo))
    else:
        if any(word in msg for word in gav0):
            if users[str(message.author.id)]['angry'] < 3:
                gav = ['тяф-тяф','мяу?',' афф',' гав-гав',' гав?',' Гав.',' **ВУФ**',' Фыр-фыр',' *Гав?*','гав!',' тяф-тяф','мяу? ∪￣-￣∪',' афф','гав!',' тяф-тяф','мяу? ∪￣-￣∪',' афф',' гав-гав V●ᴥ●V',' гав?',' гав.','гав ∪･ω･∪','авууу','вуф F','гав (▽◕ ᴥ ◕▽)','гаффф','гав. ∪￣ᴥ￣∪','г-гав...?','гав-гав!?!','вааф','*тяф* 🌸','гав, ваф гафф?']
                await add_exp(users,str(message.author.id),0.1)
                await add_bing(users,str(message.author.id),1)
                await message.channel.send(random.choice(gav))
                if message.content.startswith('мяу'):
                        await message.add_reaction('<:bingpup_2:709143279291203605>')
            else:
                gav = ['*кусает <@authorID>*',' **ГАВ!! (╯°益°)╯彡┻━┻**']
                await message.channel.send(random.choice(gav))

        if message.content.startswith('Бинпап плохой'): 
            bad = ['Я с тобой больше не гавкаю!', ' **Я ХОРОШИЙ** (╯°益°)╯彡┻━┻', ' Это ты плохой, рррр', ' И почему же? 😑', ' за оскорбление чувств бинпапов я тебя съем']
            await message.channel.send(random.choice(bad))
            await add_angry(users,str(message.author.id),1) 
        elif message.content.startswith('бинпап, '):
            await message.channel.send('Я **Б**инпап <:s_qingqiu1:806170533045469224>')
    with open('C:\\Users\\annas\\Documents\\Bingpup\\lvl.json','w') as f:
        json.dump(users,f)
    await bot.process_commands(message)

bot.run('NzA3NTM4NjM2NTgwNzE2NTU0.XrKQtA.G55i1ziHtvJG_0ii8QT_VIBAr68')

# py -3 main.py  await message.edit(content="newcontent")

