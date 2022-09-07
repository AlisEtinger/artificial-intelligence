from telebot import types  # Импортируем типы из модуля, чтобы создавать кнопки
import telebot  # Подключаем модуль для Телеграма
#  import config
import DataBase as d


bot = telebot.TeleBot(d.k)


def pp(message):
    if message.text == 'Vl':
        d.Vl.append(message.chat.id)
    elif message.text == 'Vl':
        d.Vl.append(message.chat.id)


@bot.message_handler(commands=['start'])
def start(message):
    # список из id пользователей
    if message.chat.id in d.vll:
        keys = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="A1", callback_data="New")
        but_2 = types.InlineKeyboardButton(text="Новости", callback_data="New")
        but_3 = types.InlineKeyboardButton(text="A2", callback_data="New")
        keys.add(but_1, but_2, but_3,)
        bot.send_message(message.chat.id, "Что бы вы хотели?)", reply_markup=keys)

    elif message.chat.id in d.vll2:
        keys = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Ссылки", callback_data="A1")
        but_2 = types.InlineKeyboardButton(text="Найти фото", callback_data="A2")
        but_3 = types.InlineKeyboardButton(text="Новости", callback_data="A3")
        but_4 = types.InlineKeyboardButton(text="Правила", callback_data="A4")
        keys.add(but_1, but_2, but_3, but_4)
        bot.send_message(message.chat.id, "Vl", reply_markup=keys)

    elif message.chat.id in d.MAIN:
        keys = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="статистика", callback_data="STAT")
        but_2 = types.InlineKeyboardButton(text="конференции", callback_data="CONF")
        but_3 = types.InlineKeyboardButton(text="Новости", callback_data="NEW")
        keys.add(but_1, but_2, but_3)
        bot.send_message(message.chat.id, "Vl", reply_markup=keys)

    else:
        sent = bot.send_message(message.from_user.id, "Введите пароль, затем снова нажмите на /start")
        bot.register_next_step_handler(sent, pp)

    @bot.callback_query_handler(func=lambda c: True)
    def inline(c):

# Я тут написала бота, который из меню выбирает,что ему нужно (кнопочкой)
# Затем переходит на другие ссылки и отправляет по запросу в нужный кластер 
# тот кластер обрабатывет запрос и отправляет в нужным людям
 
        if c.data == 'Vl':
            keys = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="A1", callback_data="New")
        but_2 = types.InlineKeyboardButton(text="Новости", callback_data="New")
        but_3 = types.InlineKeyboardButton(text="A2", callback_data="New")
        keys.add(but_1, but_2, but_3,)
        bot.send_message(message.chat.id, "Что бы вы хотели?)", reply_markup=keys)


        elif c.data == 'Vl':
        keys = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Ссылки", callback_data="A1")
        but_2 = types.InlineKeyboardButton(text="Найти фото", callback_data="A2")
        but_3 = types.InlineKeyboardButton(text="Новости", callback_data="A3")
        but_4 = types.InlineKeyboardButton(text="Правила", callback_data="A4")
        keys.add(but_1, but_2, but_3, but_4)
        bot.send_message(message.chat.id, "Vl", reply_markup=keys)


        elif message.chat.id in d.MAIN:
        keys = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="статистика", callback_data="STAT")
        but_2 = types.InlineKeyboardButton(text="конференции", callback_data="CONF")
        but_3 = types.InlineKeyboardButton(text="Новости", callback_data="NEW")
        keys.add(but_1, but_2, but_3)
        bot.send_message(message.chat.id, "Vl", reply_markup=keys)

 