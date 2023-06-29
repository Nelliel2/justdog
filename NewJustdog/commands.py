import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
from control_user import *
from bot import *

bot = return_bot()

async def hugs(message, msg):
    price = 1000
    hugs = ['https://media.discordapp.net/attachments/717880112565190720/1122909168228126770/PV8Rz.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917849715970122/wholesome-sad.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917849330106378/tpn-ray.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917846838689922/noragami-hug.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917846394085386/love-anime.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917845936914594/kitsune-upload-anime.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917845131595806/hug-k-on.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917844808646666/hug-anime-hug.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917844426956871/hug-anime.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917844087214170/hug-anime_2.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917843802013757/hug-anime_1.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917843441295450/toilet-bound-hanakokun.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917802802688110/horimiya-hug-anime.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917802416816278/hmmmm-hugs.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917801997381733/hanakokun-yashiro.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917801628274809/enage-kiss-anime-hug.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917801296936991/dazai-osamu-dazai.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917800948797532/chobits-hideki-motosuwa.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917800588099584/cat-murr.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917800269328534/anya-forger-spy-x-family.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917799946358884/anime-love.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917799531135057/hug.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917744711581736/anime-hug-anime-girls.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917744250191892/anime-hug.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917743864328304/anime-hug_7.gif', 'https://media.discordapp.net/attachments/717880112565190720/1122917743461679144/anime-hug_6.gif', 'https://media.tenor.com/b3Qvt--s_i0AAAAM/hugs.gif', 'https://media.tenor.com/B3R3eEskky8AAAAC/anime-hug.gif', 'https://media.tenor.com/Ki8Qxz-kP68AAAAM/hug.gif', 'https://media.tenor.com/ojWN5tfPmxkAAAAM/hug.gif', 'https://media.tenor.com/XLtShugxTWsAAAAM/hug-anime.gif', 'https://media.tenor.com/KUYvQTOUCVUAAAAM/kitsune-upload-violet-evergarden.gif', 'https://media.tenor.com/tNSZYxo1ZKwAAAAM/anime-hug.gif', 'https://media.tenor.com/ApfJHef4J1UAAAAM/love-anime.gif', 'https://media.tenor.com/TLnFZarBe6IAAAAM/sasaki-to-miyano-sasaki-and-miyano.gif', 'https://media.tenor.com/eEIEnCzpIFYAAAAM/anime-hug-anime-hug-couple.gif', 'https://media.tenor.com/eEIEnCzpIFYAAAAM/anime-hug-anime-hug-couple.gif', 'https://media.tenor.com/RHVWhd6l_pQAAAAM/princess-connect-anime-hug.gif', 'https://media.tenor.com/5KnzpCDEyMEAAAAM/princess-conet-hug.gif', 'https://media.tenor.com/Pc0J3qy-MMIAAAAM/anime-hug.gif', 'https://media.tenor.com/6ybwqR18Qy0AAAAM/dazai-osamu-dazai.gif', 'https://media.tenor.com/Xv2zxcT3TmsAAAAM/dazai-dazai-osamu.gif', 'https://images-ext-2.discordapp.net/external/v53u7xqdmHY9rVduQcpGDD5UT78Y6BSM1XjPsgFpAbI/https/media.tenor.com/vFwu0XE-7mwAAAAM/smeshno-lol.gif', 'https://media.tenor.com/ZkXihkbBIkAAAAAM/hug-hugmasc.gif', 'https://media.discordapp.net/attachments/737913032138817646/1122927031827582996/OKwi_2.gif', 'https://media.tenor.com/LmU-9TVgZrsAAAAM/sk8-the.gif']
    embed = discord.Embed(description=f'{message.author.mention} обнял(а) {msg}', color=0xff0000)
    embed.set_footer(text=f'-{price} 💸', icon_url=message.author.avatar_url)
    embed.set_image(url=random.choice(hugs))
    await add_user(message.author.id,'money', -price)
    await message.channel.send(embed=embed) 

@bot.command(description="Обнимашки!") 
async def обнял(message, *, msg): 
    await hugs(message, msg)

@bot.command(description="Обнимашки!")     
async def обняла(message, *, msg): 
    await hugs(message, msg)