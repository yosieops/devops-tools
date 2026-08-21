import os
import telebot

# Получаем токен из переменных окружения (лучшая практика для CI/CD)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "MOCK_TOKEN_FOR_TESTS")
bot = telebot.TeleBot(TOKEN)


def get_welcome_message() -> str:
    """Возвращает приветственное сообщение. Вынесено в функцию для тестов."""
    return "Привет! Я бот для проверки твоего CI."


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """Обработчик команды /start."""
    bot.reply_to(message, get_welcome_message())


if __name__ == "__main__":
    # В реальной среде здесь был бы bot.infinity_polling()
    # Но для демонстрации просто выведем статус
    print("Бот успешно инициализирован.")
