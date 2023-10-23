
from discord.ext import commands
import os
from dotenv import load_dotenv
from talk import *
from commands import *
#from NewYear import *
#from Halloween import *

load_dotenv()


@bot.event
async def on_ready():
    print('Бинпап в полном порядке!')
    morning = ['Бинпап снова с вами!', 'Я проснулся!', 'Всем доброе утро!', 'Готов гавкать целый день!', 'Я вернулся из царства грёз!']
    my_channel = bot.get_channel(778933279654936597)
    #await my_channel.send(random.choice(morning)) 

@bot.event
async def on_member_join(member):
    try:
        channel = member.get_channel(778933279654936597)
        await channel.send("Приветствую тебя, {}!\nНадеюсь, ты станешь моим новым другом, аваф!".format(str(member.username)))
    except:
        print('Ошибка в приветсвии новичка')

'''@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(778933279654936597)
        await channel.send("{}, прощай... ты был прекрасным человеком! ".format(str(member.username)))
    except:
        print('Ошибка в прощании с человеком')'''
    
@bot.event
async def on_disconnect():    
    print('Бинпап уснул!')

@bot.listen('on_message')
async def bingpups(message):
    await bingpup(message)


bot.run(os.getenv('BOT_TOKEN'))


input("Press <Enter> to exit.")