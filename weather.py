import telebot
from config import API_key, API_TOKEN
from telebot import types
import requests

bot=telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['weather'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет ,хочешь узнать погоду? Введи название города:')
    

@bot.message_handler()
def get_weather(message): 
    
    try:
        r = requests.get (
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_key}&units=metric&lang=ru"
        )
        data = r.json()
        

        city = data['name']
        cur_weather = data['main'] ['temp']
        humidity = data['main'] ['humidity']
        pressure = data['main'] ['pressure']
        wind = data['wind'] ['speed']
        bot.send_message(message.chat.id,f'Погода в городе: {city}\nТемпература: {cur_weather}C°\n'
        f'Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nВетер: {wind}м/c')
    except:
        bot.send_message(message.chat.id,'проверьте название города: ')

bot.polling(none_stop=True)