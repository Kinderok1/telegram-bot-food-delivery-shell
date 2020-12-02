import telebot
import const

from telebot import types

bot = telebot.TeleBot(const.TOKEN)


@bot.message_handler(commands=['start'])
def startpg(message):
    startmenu = types.ReplyKeyboardMarkup(True, False)
    startmenu.row('🍴 Menu', '🛍 Basket')
    startmenu.row('📦 Orders', '📢 News')
    startmenu.row('⚙️ Settings', '❓ Help')
    bot.send_message(message.chat.id, 'You are welcome!', reply_markup=startmenu)



def menu():
    glavmenu = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Japanese menu', callback_data='yponmenu')
    but_2 = types.InlineKeyboardButton(text='European menu', callback_data='evropmenu')
    but_3 = types.InlineKeyboardButton(text='Pizza', callback_data='pizza')
    glavmenu.add(but_1, but_2, but_3)
    return glavmenu



@bot.message_handler(content_types=['text'])
def osnov(message):
    if message.text == '🏠 Start page':
        global nachalo
        nachalo = 'nachalo'
        startpg(message)
    elif message.text == '🏠':
        startpg(message)
    elif message.text == '🍴 Menu':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('🏠 Start page')
        bot.send_message(message.chat.id, 'Menu', reply_markup=back)
        bot.send_message(message.chat.id, 'Select a section to display a list of dishes:', reply_markup=menu())
    elif message.text == '🍴':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('🏠 Start page')
        bot.send_message(message.chat.id, 'Menu', reply_markup=back)
        bot.send_message(message.chat.id, 'Select a section to display a list of dishes:', reply_markup=menu())
    elif message.text == '📢 News':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('🏠 Start page')
        bot.send_message(message.chat.id, '? Do you want such a store? \ N The store is powered by....  ?', reply_markup=back)
    elif message.text == '❓ Help':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('🏠 Start page')
        bot.send_message(message.chat.id, 'Your future team list:', reply_markup=back)
    elif message.text == '⚙️ Settings':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('🏠 Start page')
        bot.send_message(message.chat.id, 'Сhange Settings:',reply_markup=back)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'yponmenu':
        yaponmenu = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Gunkans', callback_data='gunkani')
        but_2 = types.InlineKeyboardButton(text='Appetizers and salads', callback_data='zakuskiisalat')
        but_3 = types.InlineKeyboardButton(text='Noodles and rice', callback_data='lapshairis')
        but_4 = types.InlineKeyboardButton(text='Nigiri sushi', callback_data='nigirisushi')
        but_5 = types.InlineKeyboardButton(text='Main dishes', callback_data='osnovbluda')
        but_6 = types.InlineKeyboardButton(text='Rolls', callback_data='rolli')
        but_7 = types.InlineKeyboardButton(text='Start page Menu', callback_data='vnachalo')
        yaponmenu.add(but_1)
        yaponmenu.add(but_2)
        yaponmenu.add(but_3, but_4)
        yaponmenu.add(but_5, but_6)
        yaponmenu.add(but_5, but_6)
        yaponmenu.add(but_7)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=yaponmenu)
#JAPAN Menu
    elif c.data == 'gunkani':
        gunkani1 = types.ReplyKeyboardMarkup(True, False)
        gunkani1.row('🏠', '🍴', '🛍', 'NEXT 5')
        bot.send_message(c.message.chat.id, 'Gunkans:', reply_markup=gunkani1)
        gunkani11 = types.InlineKeyboardMarkup()
        but_11 = types.InlineKeyboardButton(text='1peace-69', callback_data='gunkani11')
        gunkani11.add(but_11)
        bot.send_photo(c.message.chat.id, 'AgADAgADxKoxG_gXEUppdfUQ3Ip9vw4ABO3hbgSLuH2OYFAAEC', caption='Икура\nИкра лосося\nВес: 28г\nОбъем: 1шт', reply_markup=gunkani11)
        gunkani12 = types.InlineKeyboardMarkup()
        but_12 = types.InlineKeyboardButton(text='1peace-75', callback_data='gunkani12')
        gunkani12.add(but_12)
        bot.send_photo(c.message.chat.id, 'AgADAgADx6oxG_gXEUoVim-FFYabJB7ABPH-G0qSxQ50O_gAAgI', caption='Нику темпура\nСыр эдам, бекон, соус авокадо\nВес: 150/30г', reply_markup=gunkani12)
    elif c.data == 'zakuskiisalat':
        zakuski1 = types.ReplyKeyboardMarkup(True, False)
        zakuski1.row('🏠', '🍴', '🛍')
        bot.send_message(c.message.chat.id, 'Gunkans:', reply_markup=zakuski1)
        zakuski11 = types.InlineKeyboardMarkup()
        but_11 = types.InlineKeyboardButton(text='210 Р', callback_data='zakuski11')
        zakuski11.add(but_11)
        bot.send_photo(c.message.chat.id, 'AgADAgADyKoxG_gXEUqcRXYCn2BIFZOQ8gZTnJccpiY7L0BAAEC', caption='Икура\nИкра лосося\nВес: 28г\nОбъем: 1шт', reply_markup=zakuski11)
        zakuski12 = types.InlineKeyboardMarkup()
        but_12 = types.InlineKeyboardButton(text='145', callback_data='zakuski12')
        zakuski12.add(but_12)
        bot.send_photo(c.message.chat.id, 'AgADAgADyaoxG_gXEUquYUd-Mlx4vMXw8AcU7DtW9U-VJPkAAgI', caption='Чука салат\nВодоросли и ореховый соус\nВес: 75/30г', reply_markup=zakuski12)
#В START page
    elif c.data == 'vnachalo':
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=menu())
#EUROPE Menu
    elif c.data == 'evropmenu':
        evropmenu1 = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Side dishes', callback_data='garni')
        but_2 = types.InlineKeyboardButton(text='Side dishes', callback_data='desert')
        but_3 = types.InlineKeyboardButton(text='Additionally', callback_data='dopol')
        but_4 = types.InlineKeyboardButton(text='Snacks', callback_data='zakus')
        but_5 = types.InlineKeyboardButton(text='Paste', callback_data='pasta')
        but_6 = types.InlineKeyboardButton(text='Fish', callback_data='riba')
        but_7 = types.InlineKeyboardButton(text='Start page Menu', callback_data='vnachalo')
        evropmenu1.add(but_1, but_2)
        evropmenu1.add(but_2)
        evropmenu1.add(but_3, but_4)
        evropmenu1.add(but_5, but_6)
        evropmenu1.add(but_5, but_6)
        evropmenu1.add(but_7)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=evropmenu1)

bot.polling()