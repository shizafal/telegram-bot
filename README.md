# Telegram-бот на Python

Многофункциональный Telegram-бот с командами для курса валют, заметок и игры.

## Возможности

- **Курс валют** — `/course USD 100` — получает курс с API ЦБ РФ.
- **Заметки** — `/note add/list/delete` — добавление, просмотр, удаление заметок.
- **Игра «Угадай число»** — `/game` — классическая игра с подсказками.

## Технологии

- Python 3.10+
- `python-telegram-bot` — для работы с Telegram API
- `requests` — для API курса валют
- `json` — для хранения заметок

## Установка и запуск

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/shizafal/telegram-bot.git
   ```

2. Перейди в папку:
   ```bash
   cd telegram-bot
   ```

3. Установи зависимости:
   ```bash
   pip install "python-telegram-bot[socks]" requests
   ```

4. Создай `config.py` с токеном:
   ```python
   TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"
   ```

5. Запусти бота:
   ```bash
   python bot.py
   ```

## Использование

| Команда | Что делает |
|---------|------------|
| `/start` | Приветствие |
| `/help` | Список команд |
| `/course USD 100` | Курс валют |
| `/note add <текст>` | Добавить заметку |
| `/note list` | Показать заметки |
| `/note delete <номер>` | Удалить заметку |
| `/game` | Игра «Угадай число» |

### Пример работы

```
> /course USD 100
100.0 USD = 8647.3 RUB

> /note add Купить хлеб
Заметка добавлена: Купить хлеб

> /note list
1. Купить хлеб

> /game
Я загадал число от 1 до 100. Угадай!
```

## Структура проекта

```
telegram-bot/
├── bot.py           # Точка входа, регистрация команд
├── api.py           # Работа с API (курс валют)
├── notes.py         # Заметки (JSON)
├── game_bot.py      # Игра «Угадай число»
├── config.py        # Токен (не в Git)
├── .gitignore       # Исключения
└── README.md        # Этот файл
```

## Автор

Shizafal — [github.com/shizafal](https://github.com/shizafal)