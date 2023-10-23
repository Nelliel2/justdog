import time
from random import randint
import json

with open('state.json', 'r', encoding='utf-8') as f4:
    state = json.load(f4)

async def rewrite_state(key, value):
    state['bingpup'][key] = value

async def change_state(key, value):
    state['bingpup'][key] = state['bingpup'][key] + value

def return_state(key):
    return state['bingpup'][key]  

async def add_state(key):
    value = randint(5,10)
    try:
        if (return_state(key) + value < 100):
            await change_state(key, value)
            if ((return_state('sad') == 1) and (return_state('clean') >= 60) and (return_state('hunger') >= 60) and (return_state('healf') >= 60) and (return_state('joy') >= 60)):
                await rewrite_state('sad', 0)
        else:
            await rewrite_state(key, 100)
    except:
        print('error in state')

async def update_state():
    if (time.time() - return_state('time') > 61600):
        await rewrite_state('time', round(time.time(),2))
        await change_state('clean', -randint(3,10))
        await change_state('hunger', -randint(3,10))
        await change_state('healf', -randint(3,10))
        await change_state('joy', -randint(3,10))
        if ((return_state('sad') == 0) and ((return_state('clean') <= 60) or (return_state('hunger') <= 60) or (return_state('healf') <= 60) or (return_state('joy') <= 60))):
            await rewrite_state('sad', 1)

def dump_state():
    with open('state.json', 'w') as f4:
        json.dump(state, f4, indent=4)