import json
import discord

with open('lvl.json', 'r', encoding='utf-8') as f:
    users = json.load(f)

async def add_user(userID,key,value):
    users['users'][str(userID)][str(key)] += value

async def rewrite_user(userID,key,value):
    users['users'][str(userID)][str(key)] = value

def return_user(userID, key):
    return users['users'][userID][key]

async def update_data(userID, author_name):
    if not userID in users['users']:
        users['users'][userID] = {}
        rewrite_user(userID,'name',str(author_name).split('#')[0])
        rewrite_user(userID,'exp', 0)
        rewrite_user(userID,'lvl',1)
        rewrite_user(userID,'bing',0)
        rewrite_user(userID,'money',0)
        rewrite_user(userID,'angry',0)
        rewrite_user(userID,'wife','—')
        rewrite_user(userID,'master','—')
        rewrite_user(userID,'servants','—')
        rewrite_user(userID,'angmsg','')
        rewrite_user(userID,'oldmsg','')
        rewrite_user(userID,'remember','')
        for i in range(5):
            rewrite_user(userID,'seconds'+str(i),0)
            
async def add_lvl(userID):
    if return_user(userID, 'exp') > return_user(userID, 'lvl')*return_user(userID,'lvl'):
        #await message.channel.send(f'{message.author.mention} повысил свой уровень!')
        rewrite_user(userID, 'exp', 0)
        add_user(userID,'lvl',1)

async def top(comparator, who, measure, humanID, avatar_url):
    top = []
    for user in users['users']:
        top.append([return_user(user,'name'), return_user(user,comparator)])
    top = sorted(top, key=lambda x: x[1], reverse=True) 
    answer = ''
    for i in range(0,10):
        human = top[i][0]
        answer += f'{i+1}. {human} — {top[i][1]} {measure}\n'
    embed = discord.Embed(description=answer, color=0xff0000, title=f'Лучшие {who} Бинпапа 🌈', )
    for i in range(0,1000):
        human = top[i][0]
        if return_user(str(humanID),'name')==human:
            embed.set_footer(text=f'{i+1}. {human} — {top[i][1]} {measure}', icon_url=avatar_url)
            break
    embed.set_image(url='https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif')
    top.clear()  
    return embed   

def dump_user():
    with open('lvl.json', 'w', encoding='utf8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
