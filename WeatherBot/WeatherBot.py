import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

def weather(country,city):
    global temp
    url=f'https://www.foreca.ru/{country}/{city}'
    response = requests.get(url)
    bs = BeautifulSoup(response.content,"html.parser")
    temp=bs.find("span", {"class":"value temp temp_c warm"})           
                

bot = telebot.TeleBot('7857487927:AAHOBboJvYn0KRkh1J1PaadfnTLinjBBKDc')
country = ''
city = ''
@bot.message_handler(commands=['start'])
def StartMessage(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    support = types.KeyboardButton('Тех Поддержка 📨')
    weather = types.KeyboardButton('Узнать погоду')
    change_city_and_country = types.KeyboardButton('Установить/изменить город')
    markup.add(weather,change_city_and_country)
    markup.add(support)
    weather_picture = open('Ава.jpg','rb') 
    bot.send_photo(message.chat.id, weather_picture, caption='Вас приветствует бот погоды!!! \n\nУкажите страну, а после город чтобы узнать температуру воздуха там, на данный момент', reply_markup=markup)

@bot.message_handler(func=lambda call:True)

def Reply_to_KeyboardButton(message):
    if message.text == 'Установить/изменить город':
        inline_markup = types.InlineKeyboardMarkup()
        mrk_city = types.InlineKeyboardButton(text = 'Город', callback_data = 'Город')
        mrk_country = types.InlineKeyboardButton(text = 'Страна', callback_data = 'Страна')
        inline_markup.add(mrk_country)
        inline_markup.add(mrk_city)
        bot.send_message(message.chat.id, 'Выберите, что хотите изменить',reply_markup=inline_markup)
    elif message.text == 'Тех Поддержка 📨':
        bot.send_message(message.chat.id, 'По техническим неисправностям обращайтесь в личные сообщения к @iwannabenever')
    elif message.text == 'Узнать погоду':
        if country == '' and city == '':
            bot.send_message(message.chat.id, 'Для начала установите Страну и Город')
        elif country == '' and city != '':
            bot.send_message(message.chat.id, 'Для начала установите Страну')
        elif country != '' and city == '':
            bot.send_message(message.chat.id, 'Для начала установите Город')
        elif country != '' and city != '':
            weather(country,city)
            bot.send_message(message.chat.id, f'Установленная страна: {country}\nУстановленный город: {city}\nТемпература воздуха: {temp.text}')
    else:
        bot.send_message(message.chat.id, 'Не знаю команды, попробуйте снова')
    
@bot.callback_query_handler(func=lambda call:True)

def Reply_to_InlineKeyboardButton(call):
    global country,city
    if call.data == 'Страна':
       bot.delete_message(call.message.chat.id, call.message.id)
       inline_markup = types.InlineKeyboardMarkup()
       Russia = types.InlineKeyboardButton(text = 'Россия', callback_data = 'россия')
       Kazakhstan = types.InlineKeyboardButton(text = 'Казахстан', callback_data = 'казахстан')
       inline_markup.add(Russia)
       inline_markup.add(Kazakhstan)
       bot.send_message(call.message.chat.id, 'Выберите страну', reply_markup=inline_markup)
    elif call.data == 'Город':
        if country == '':
            bot.delete_message(call.message.chat.id, call.message.id)
            inline_markup = types.InlineKeyboardMarkup()
            Russia = types.InlineKeyboardButton(text = 'Россия', callback_data = 'россия')
            Kazakhstan = types.InlineKeyboardButton(text = 'Казахстан', callback_data = 'казахстан')
            inline_markup.add(Russia)
            inline_markup.add(Kazakhstan)
            bot.send_message(call.message.chat.id, 'Сначала выберите страну',reply_markup=inline_markup)
        elif country == 'Russia':
            bot.delete_message(call.message.chat.id, call.message.id)
            inline_markup = types.InlineKeyboardMarkup()
            Moscow = types.InlineKeyboardButton(text = 'Москва', callback_data = 'москва')
            Saint_petersburg = types.InlineKeyboardButton(text = 'Санкт-Петербург', callback_data = 'санкт-петербург')
            Kaliningrad = types.InlineKeyboardButton(text = 'Калининград', callback_data = 'калининград')
            Tyumen = types.InlineKeyboardButton(text = 'Тюмень', callback_data = 'тюмень')
            Sochi = types.InlineKeyboardButton(text = 'Сочи', callback_data = 'сочи')
            Nizhny_novgorod = types.InlineKeyboardButton(text = 'Нижний Новгород', callback_data = 'нижний новгород')
            Kazan = types.InlineKeyboardButton(text = 'Казань', callback_data = 'казань')
            Ekaterinburg = types.InlineKeyboardButton(text = 'Екатеринбург', callback_data = 'екатеринбург')
            Novosibirsk = types.InlineKeyboardButton(text = 'Новосибирск', callback_data = 'новосибирск')
            Barnaul = types.InlineKeyboardButton(text = 'Барнаул', callback_data = 'барнаул')
            inline_markup.add(Moscow,Saint_petersburg)
            inline_markup.add(Kaliningrad,Sochi)
            inline_markup.add(Nizhny_novgorod,Barnaul)
            inline_markup.add(Kazan,Ekaterinburg)
            inline_markup.add(Novosibirsk,Tyumen)
            bot.send_message(call.message.chat.id,'Выберите нужный вам город России',reply_markup=inline_markup)
        elif country == 'Kazakhstan':
            bot.delete_message(call.message.chat.id, call.message.id)
            inline_markup = types.InlineKeyboardMarkup()
            Almaty =  types.InlineKeyboardButton(text = 'Алмата', callback_data = 'алмата')
            Astana = types.InlineKeyboardButton(text = 'Астана', callback_data = 'астана')
            Shymkent = types.InlineKeyboardButton(text = 'Шимкент', callback_data = 'шимкент')
            Aktobe = types.InlineKeyboardButton(text = 'Актобе', callback_data = 'актобе')
            Karaganda = types.InlineKeyboardButton(text = 'Караганда', callback_data = 'караганда')
            Taraz = types.InlineKeyboardButton(text = 'Тараз', callback_data = 'тараз')
            Ust_Kamenogorsk = types.InlineKeyboardButton(text = 'Усть-Каменогорск', callback_data = 'усть-каменогорск')
            Pavlodar = types.InlineKeyboardButton(text = 'Павлодар', callback_data = 'павлодар')
            Atyrau = types.InlineKeyboardButton(text = 'Атырау', callback_data = 'атырау')
            Semey = types.InlineKeyboardButton(text = 'Семей', callback_data = 'семей')
            inline_markup.add(Almaty,Astana)
            inline_markup.add(Shymkent,Aktobe)
            inline_markup.add(Karaganda,Taraz)
            inline_markup.add(Ust_Kamenogorsk,Semey)
            inline_markup.add(Pavlodar,Atyrau)
            bot.send_message(call.message.chat.id,'Выберите нужный вам город Казахстана',reply_markup=inline_markup)
    elif call.data == 'россия':
        bot.delete_message(call.message.chat.id, call.message.id)
        country = 'Russia'
        city = ''
        bot.send_message(call.message.chat.id, f'Установлена страна: {country}')
    elif call.data == 'казахстан':
        bot.delete_message(call.message.chat.id, call.message.id)
        country = 'Kazakhstan'
        city = ''
        bot.send_message(call.message.chat.id, f'Установлена страна: {country}')
    elif call.data == 'москва':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'moscow'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'санкт-петербург':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'saint_petersburg'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'калининград':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'kaliningrad'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'тюмень':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'tyumen'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'сочи':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'sochi'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'нижний новгород':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'nizhny_novgorod'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'казань':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'kazan'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'екатеринбург':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'ekaterinburg'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'новосибирск':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'novosibirsk'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'барнаул':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'Barnaul'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'алмата':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'almaty'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'астана':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'astana'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'шимкент':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'shymkent'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'актобе':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'aktobe'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'караганда':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'karaganda'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'тараз':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'taraz'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'усть-каменогорск':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'ust_kamenogorsk'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'павлодар':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'pavlodar'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'атырау':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'atyrau'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')
    elif call.data == 'семей':
        bot.delete_message(call.message.chat.id, call.message.id)
        city = 'semey'
        bot.send_message(call.message.chat.id, f'Установлен город: {city}')



bot.polling(none_stop=True, interval=0)
