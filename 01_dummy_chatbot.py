from telegram.ext import Updater, MessageHandler, Filters
import openai

openai.api_key = "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"
TELEGRAM_API_TOKEN = "6627740106:AAGhQjoWNFQP00HwbzLvNOvIyf7p1lGnkL8"

def text_message(update, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": "Ass a silly phrase after each one of your answers"}]
    )
    update.message.reply_text(response["choices"][0]["message"]["content"])


updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_message))
updater.start_polling()
updater.idle()