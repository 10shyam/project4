import emoji, telegram
from telegram import Updater
from telegram import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



#general functions
#def start(bot, update):
token = "5514395922:AAE31akNKsZ1GnlV10QPM9lmzo0M8WSTBRQ"
bot = telegram.Bot(token=token)
pic = "./Total_M2M_Image.png"
chat_id = '-1001703229995'
bot.send_photo(chat_id, open(pic,'rb'))
update.message.reply_text(text="hello",
                          reply_markup=menu_keyboard())

