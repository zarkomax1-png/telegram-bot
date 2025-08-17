from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")  # El token lo pones en Render → Environment Variables

def start(update, context):
    update.message.reply_text("¡Tu bot está vivo en Render 🚀!")

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
