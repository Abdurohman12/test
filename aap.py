import telebot

import random

bot = telebot.TeleBot("7991741470:AAF6fzRcxVT3MktmR-avwRT8GdVI6L8hbic",parse_mode=None)

son = random.randint( 1,10 )

@bot.message_handler(commands=["start"])

def start(xabar):
 
 bot.reply_to(xabar,"Assalomu alaykum barsamusur.uz botimizga xush kelibsiz ")

@bot.message_handler(commands=["about"])

def start(xabar):
    
    Foto = open ("./imgCR7.jpg","rb")

    bot.send_photo(xabar.chat.id.foto)

    Foto.open()

    @bot.message_handler(commands=["game"])
    
    def game (xabar):
        
        bot.reply_to(xabar,"Komputer 1 dan 10 gacha sonlarni o'ylaydi, shuni top")

@bot.message_handler(func=lambda m: m.text.isdigit())

def guess(xabar):
    
    us = (xabar.text)

    if us == son:

      bot.reply_to(xabar,"barsmusur.uz bot yutkizdi ")

    else:
         
         bot.reply_to(xabar,"yutkzdingiz")

bot.infinity_polling()

print("ishlamoqda")
 

