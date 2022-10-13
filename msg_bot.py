import os
import telebot


API_TOKEN = 'PASTE_HERE_YOUR_BOT_API_TOKEN'

bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(content_types=['text'])
def message_recieved(msg):
    os.system(f"cmd /c msg * /TIME:0 {msg.text}")
    bot.send_message(chat_id=msg.from_user.id, text="Done!")

bot.polling(True)