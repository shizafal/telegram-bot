"""Модуль для работы с заметками в Telegram-боте"""

import json

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Файл заметок повреждён. Создаю новый.")
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

async def handle_note(update, context):
    args = context.args

    if not args:
        await update.message.reply_text(
            "Использование:\n"
            "/note add <текст> - добавить заметку\n"
            "/note list - показать все заметки\n"
            "/note delete <номер> - удалить заметку"
        )
        return

    action = args[0].lower()

    if action == "add":
        if len(args) < 2:
            await update.message.reply_text("Введите текст заметки после 'add'.")
            return

        note = " ".join(args[1:])
        notes = load_notes()
        notes.append(note)
        save_notes(notes)
        await update.message.reply_text(f"Заметка добавлена: {note}")
    elif action == "list":
        notes = load_notes()
        if not notes:
            await  update.message.reply_text("Заметок нет.")
            return
        text =  "\n".join(f"{i}. {note}" for i, note in enumerate(notes, 1))
        await update.message.reply_text(text)
    elif action == "delete":
        if len(args) < 2:
            await update.message.reply_text("Введите номер заметки после 'delete'.")
            return
        num_str = args[1]
        if not num_str.isdigit():
            await update.message.reply_text("Ошибка! Введите число.")
            return
        index = int(num_str) - 1
        notes = load_notes()
        if 0 <= index < len(notes):
            deleted = notes.pop(index)
            save_notes(notes)
            await update.message.reply_text(f"Заметка '{deleted}' удалена.")
        else:
            await update.message.reply_text("Заметка с таким номером не найдена.")
    else:
        await update.message.reply_text("Неизвестное действие. Используй /note")