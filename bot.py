import os
from telegram.ext import Updater, CommandHandler

# Tu token viene de las variables de entorno en Render
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Hola 👋, tu bot ya está funcionando en Render 🚀")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
