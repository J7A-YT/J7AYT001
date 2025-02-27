from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import requests

TOKEN = "7745412386:AAHBXHwzdqDnG6yQ6MmCvzADf6f5PMwASNo"
CHANNEL_ID = "@curly_alii"
REACTION = "🔥"  # می‌تونی اموجی دلخواهت رو بذاری

def react_to_message(update: Update, context: CallbackContext):
    if update.channel_post:
        message_id = update.channel_post.message_id
        url = f"https://api.telegram.org/bot{TOKEN}/setMessageReaction"
        data = {
            "chat_id": CHANNEL_ID,
            "message_id": message_id,
            "reaction": [{"type": "emoji", "emoji": REACTION}]
        }
        requests.post(url, json=data)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.chat(CHANNEL_ID), react_to_message))

updater.start_polling()
updater.idle()
