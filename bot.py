# Эхо бот

import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from config import TOKEN
from telegram.ext import CommandHandler

logging.basicConfig(level=logging.INFO)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Эхо: {update.message.text}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот-помощник.\n"
        "Напиши /help, чтобы увидеть доступные команды."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды.\n"
        "/start - приветствие.\n"
        "/help - список команд.\n"
        "/course - курс валют.\n"
        "/note - заметки.\n"
        "/game - игра.\n"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()