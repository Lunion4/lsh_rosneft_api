import api
import db
import telebot
bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)

@bot.message_handler(commands=['start'])
def welcome(message):
    mesg = bot.send_message(message.chat.id, "Быстро ввел свой город🔪")
    bot.register_next_step_handler(mesg, save_city)
def save_city(message):
    if db.save_user_city(message.chat.id, message.text):
        bot.send_message(message.chat.id, "Молодец, а я то думал тебя уже убить)")
    else:
        bot.send_message(message, "Ты издеваешься, ты где живешь? Переезжай в Новокуйбышевск, у меня он в бд есть")
        bot.register_next_step_handler(message, save_city)

@bot.message_handler(commands=['wind'])
def wind_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Сначала введите свой город👿')
    else:
        bot.send_message(message.chat.id, api.wind(shirota, dolgota))
        
@bot.message_handler(commands=['temp'])
def temp_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Сначала введите свой город👿')
    else:
        bot.send_message(message.chat.id, api.temperature_weather(shirota, dolgota))

@bot.message_handler(commands=['rain'])
def dojdick(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, "Сначала введите свой город👿")
    else:
        bot.send_message(message.chat.id, api.rainy_weather(shirota, dolgota))

@bot.message_handler(commands=['cloud'])
def get_cloud(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Сначала введите город😡')
    else:
        bot.send_message(message.chat.id, api.cloudcover(shirota,dolgota))

@bot.message_handler(commands=['all'])
def all_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, "Сначала введите свой город😡")
    else:
        bot.send_message(message.chat.id, api.all_weather(shirota, dolgota))

@bot.message_handler(commands=['granny'])
def grandmother(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Сначала введите город😡')
    else:
        bot.send_message(message.chat.id, api.pressure(shirota,dolgota))
        bot.send_photo(message.chat.id, "https://tenor.com/view/%D0%B4%D0%BE%D0%B1%D1%80%D0%BE%D0%B5-%D1%83%D1%82%D1%80%D0%BE-%D1%86%D0%B2%D0%B5%D1%82%D1%8B-%D1%87%D0%B0%D0%B9-%D1%84%D0%B5%D1%8F-gif-16293114")

bot.infinity_polling()
