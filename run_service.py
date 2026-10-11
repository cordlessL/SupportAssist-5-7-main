"""
Запуск Telegram-бота без интерактивного меню — для systemd/Docker.

Повторяет ветку «режим 3» из main.py (там выбор режима через input(),
под systemd stdin закрыт, поэтому main.py как сервис не работает).
"""

import os
import sys

from dotenv import load_dotenv

from main import initialize_system
from telegram_bot import TelegramRAGBot


def run():
    embedding_store, rag_assistant, cache, logger = initialize_system()

    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not telegram_token:
        print("❌ Не задан TELEGRAM_BOT_TOKEN в .env")
        sys.exit(1)

    bot = TelegramRAGBot(
        token=telegram_token,
        rag_assistant=rag_assistant,
        cache=cache,
        logger=logger,
    )
    bot.run()


if __name__ == "__main__":
    run()
