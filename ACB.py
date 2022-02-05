import telebot
from telebot import types

API = "https://core.telegram.org/bots/api/{}"



bot = telebot.TeleBot('5046963515:AAE8hS-pHvSNfGbejF6UMW_IptBst8-neZ8')
button = telebot.types.ReplyKeyboardMarkup(True)
button2 = telebot.types.ReplyKeyboardMarkup(True)
button3 = telebot.types.ReplyKeyboardMarkup(True)
button4 = telebot.types.ReplyKeyboardMarkup(True)
admin = telebot.types.ReplyKeyboardMarkup(True)

admin.row("💰 Hisobim","📤 Forword")
admin.row("⚒ Bot Sozlash","📈 Statistika")
admin.row("Ortga")

button.row("🏠 Bosh bo'lim")
button.row("📰 Malumot","Tarmoq")
button.row("Xabar","")



button2.row("📠 Kantakt","Bot")
button2.row("Ortga")


button3.row("Buyurtma","Tarix")
button3.row("Hamyon","Yangi maxsulot")
button3.row("Ortga")

button4.row("Ortga")



@bot.message_handler(commands=['start'])
def start_message(message):
        bot.send_message(message.chat.id, f'Salom janab {message.from_user.first_name} bizning online magazinimizga hush kelibsz',reply_markup=button)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'tarmoq':
        markup = types.InlineKeyboardMarkup()
        btn_my_grm= types.InlineKeyboardButton(text='Telegram o\'tish', url='https://t.me/missbella_turkiya_optom')
        btn_my_insta= types.InlineKeyboardButton(text= 'Gruh o\'tish', url='https://t.me/missbellachat')
        markup.add(btn_my_grm,btn_my_insta)
        bot.send_message(chat_id=message.chat.id, text="<b>Saidmaruf Partfolio</b>", parse_mode='HTML', reply_markup = markup)

        # //menyu// #

    elif message.text.lower() == '📰 malumot':
        bot.send_message(chat_id=message.chat.id, text="<b>🖐Ассалoму алайкум!\n🇹🇷Турция Фабрика\n✅Банныn Халат, Пододеяльник,\n✔Покрывал Полотенца Одеяло,\n♻️Подушки и так далее!\n💲Оптовая цена супер качество!\n\n@MissBella_Optom\n📞 +998946016009\n\nMade in Turkey 🇹🇷</b>", parse_mode='HTML')
    elif message.text.lower() == 'ortga':
        bot.send_message(message.chat.id, 'Bosh menyu',reply_markup=button)
    elif message.text.lower() == 'xabar':
        bot.send_message(message.chat.id, 'Bosh menyu',reply_markup=button2)
    elif message.text.lower() == '📠 kantakt':
        bot.send_message(chat_id=message.chat.id, text="<b>Boshlig\' Abdujalil\nTelefon: +998946016009\nUser: @ABDUJALIL_miss_bella</b>", parse_mode='HTML')
    elif message.text.lower() == '🏠 bosh bo\'lim':
        bot.send_message(message.chat.id, 'Bosh bo\'lim',reply_markup=button3)
    elif message.text.lower() == 'buyurtma':
        bot.send_message(message.chat.id, 'Bo\'limni tanlang')

        # //backend// #

    elif message.text.lower() == 'yodgorov/saidmaruf\nking007boy':
        bot.send_message(1902504138, "Salom admin",reply_markup=admin)


    elif message.text.lower() == 'bot':
        bot.send_message(message.chat.id, message.text,reply_markup=button4)

bot.polling(none_stop = True)