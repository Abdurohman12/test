import telebot

bot = telebot.TeleBot("8466837704:AAEts5snWIbcihpZIHw4ExBMCOqv6DN_izU")

@bot.message_handler(commands=["start"])

def start(id):
    print("ishlamoqda")
    print(id)
    bot.reply_to(id,"Assalomu alaykum barsamusur.uz_botimizga xush kelibsiz")
    
@bot.message_handler(commands=["help"])

def help(id):
    print("ishlamoqda")
    print(id)
    bot.reply_to(id,"sizga qanday yordam bera olaman ")

@bot.message_handler(commands=["footbool"])

def footbool(id): 
    print("ishlamoqda")
    print(id)
    bot.reply_to(id," 5 vs 5 footbool o'ynaysizmi ")
@bot.message_handler(func=lambda xabar:True)

def eco_all(xabar):
    print(xabar)
    bot.reply_to(xabar, xabar.text)

bot.infinity_polling() 

@bot.message_handler(commands=["xa"])

def xa(id): 
    print("ishlamoqda")
    print(id)
    bot.reply_to(id,"ok")

@bot.message_handler(func=lambda xabar:True)

def eco_all(xabar):
    print(xabar)
    bot.reply_to(xabar, xabar.text)

bot.infinity_polling() 
