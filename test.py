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
from Build.NewYear import *
intents = discord.Intents.all()
load_dotenv()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Бинпап в полном порядке?')

@bot.listen('on_message')
async def bingpups(message):
    print("test1")
    if message.author == bot.user or message.author.bot:
        return
    msg = str(message.content).replace('\n', ' ').replace('ё', 'е').lower().replace(',', '')
    words = re.findall(r'\w+', msg)
    if len(words)==0:
        return

    print("test2")
    if ('в лс 1' in msg):
        print("test")
        user = bot.get_user(message.author.id)
        await user.send('test')
    

    await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))