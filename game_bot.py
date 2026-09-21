"""Модуль для игры «Угадай число» в Telegram-боте"""

import random

async def game_start(update, context):
    secret = random.randint(1, 100)
    context.user_data["secret"] = secret
    context.user_data["attempts"] = 0
    context.user_data["in_game"] = True

    await update.message.reply_text(
        "Я загадал число от 1 до 100. Угадай!\n"
        "Напиши число в чат."
        )

async def game_guess(update, context):
    if not context.user_data.get("in_game"):
        return
    
    text = update.message.text.strip()

    if not text.isdigit():
        await update.message.reply_text("Ошибка! Введите число.")
        return

    guess = int(text)
    secret = context.user_data["secret"]
    context.user_data["attempts"] += 1
    attempts = context.user_data["attempts"]

    if guess < secret:
        await update.message.reply_text("Загаданное число больше!")
    elif guess > secret:
        await update.message.reply_text("Загаданное число меньше!")
    else:
        await update.message.reply_text(f"Поздравляю! Ты угадал за {attempts} попыток!")
        context.user_data["in_game"] = False 