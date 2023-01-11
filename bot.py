import telebot
import random 
from config import  API_TOKEN, API_key
import requests
from telebot import types
from bs4 import BeautifulSoup as bs
from weather import *

bot=telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f'Привет, <b>{message.from_user.first_name}  {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')  
    bot.send_message(message.chat.id, 'Нажми, расскажу анекдот - ' '/anekdot')
    bot.send_message(message.chat.id, 'Погода в вашем городе - ' '/weather')

url = 'https://www.anekdot.ru/'

def parser(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(url)
random.shuffle(list_of_jokes)

@bot.message_handler(content_types=['anekdot'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, введи любую цифру от 1 до 9')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите цифру')
    



bot.polling(none_stop=True)