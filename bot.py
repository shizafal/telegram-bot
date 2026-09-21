"""Мульти бот Telegram"""

import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from config import TOKEN
from telegram.ext import CommandHandler
from api import get_rate
from notes import handle_note
from game_bot import game_start, game_guess

logging.basicConfig(level=logging.INFO)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Неизвестная команда. Напиши /help, чтобы увидеть список."
    )

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

async def course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 2:
        await update.message.reply_text(
            "Использование /course USD 100\n"
            "Где USD - код валюты, 100 - количество."
        )
        return
    code = args[0].upper()
    amount_str = args[1]

    if not amount_str.replace(".", "").isdigit():
        await update.message.reply_text("Ошибка! Количетсво должно быть числом.")
        return
    amount = float(amount_str)
    rate = get_rate(code)

    if rate is None:
        await update.message.reply_text(f"Валюта '{code}' не найдена.")
        return

    result = amount * rate
    await update.message.reply_text(f"{amount} {code} = {round(result, 2)} RUB")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("course", course))
    app.add_handler(CommandHandler("note", handle_note))
    app.add_handler(CommandHandler("game", game_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, game_guess))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))
    app.run_polling()

if __name__ == "__main__":
    main()