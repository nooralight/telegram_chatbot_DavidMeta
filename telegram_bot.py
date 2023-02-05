import telebot
from class_replicate import Replicate_API
from class_chatgpt import Gpt_API
##Your telegram bot token here
BOT_TOKEN = "Your_Telegram_Bot_Token"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['ask'])
def ask(message):
    if len(message.text)<5:
        bot.reply_to(message, f"Please type your query after the command by having a space between them, like this:\n/ask Who is Joe Biden?")
    else:
        prompt = message.text[5:]
        gpt_obj = Gpt_API(prompt)
        result = gpt_obj.get_result()
        bot.reply_to(message, f"{result}")

@bot.message_handler(commands=['gen'])
def generate_image(message):
    if len(message.text)<5:
        bot.reply_to(message, f"Please type your prompt after the command by having a space between them, like this:\n/gen A fox looking at the sky, hd, dramatic lighting")
    else:
        sender = message.from_user
        prompt = message.text[5:]
        #print(prompt)
        obj = Replicate_API(prompt)
        bot.send_photo(message.chat.id,photo=obj.get_result()[0],caption = f"Hello @{sender.full_name}! , your prompt was \"{prompt}\"" )
        #bot.reply_to(message, f"Hello @{sender.username}! , your prompt was \"{prompt}\"")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, f"You will have two features in this bot.\n1. Image generation\n2.Text Generation\n\nBy typing,  /ask<space><your query> , you can ask the bot anything, and you will get answer.\n\nBy typing,  /gen<space><your prompt> , you can generate images with based on your prompt.")

bot.polling()
