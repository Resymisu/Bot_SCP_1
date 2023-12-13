import telebot
import info_bot

token = "6856983327:AAFaEgedb9gCYlAG0htJn8nlMCUSm0IXQLA"
bot = telebot.TeleBot(token=token)
chat_id = 2073876175

character = info_bot.Character()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет! Я бот-визитка персонажа {character.name}, напиши /help, чтобы узнать, что я умею.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''У бота имеется несколько комманд:
    /descrption - Текстовое описание персонажа
    /link - ссылка на страницу главного сайта по содержанию
    /video - краткое видео об этом объекте
    /photo - фото объекта
    /interactions - тест взамодействия с другими классами содежрания
    ''')



@bot.message_handler(commands=['descrption'])
def descrption(message):
    bot.send_message(message.chat.id, character.descrption)
@bot.message_handler(commands=['link'])
def link(message):
    bot.send_message(message.chat.id, character.link)

@bot.message_handler(commands=['video'])
def video(message):
    img = open(character.video_path, 'rb')
    bot.send_video(message.chat.id, img)
    img.close()

@bot.message_handler(commands=['photo'])
def photo(message):
    img = open(character.photo_path,'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
@bot.message_handler(commands=['interactions'])
def interactions(message):
    bot.send_message(message.chat.id, character.interactions)

def checking(message):
    if message == "/start" or message == "/help" or message == "/descrption" or message == "/link" or message == "/photo" or message == "/video" or message == "/interactions":
        return False
    else:
        return True

@bot.message_handler(func=checking)
def error_proc(message):
    bot.send_message(message.chat.id, "Простите, но я не понимаю данной команды или текста, пожалуйста введите коммадну /help для дальнейшего обращение с ботом")






bot.send_message(chat_id, "Пропишите комманду /start чтобы начать")

bot.polling()


