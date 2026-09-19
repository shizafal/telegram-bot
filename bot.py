# Эхо бот

import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from config import TOKEN

logging.basicConfig(level=logging.INFO)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Эхо: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()