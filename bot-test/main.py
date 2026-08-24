import os
import telebot

# Получаем токен из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "MOCK_TOKEN_FOR_TESTS")
bot = telebot.TeleBot(TOKEN)

def get_welcome_message() -> str:
    """Возвращает приветственное сообщение."""
    return "Привет! Я бот для проверки твоего CI."

def get_ping_response() -> str:
    """Возвращает ответ для проверки доступности."""
    return "Pong! Бот работает отлично 🚀"

@bot.message_handler(commands=["start"])
def send_welcome(message):
    """Обработчик команды /start."""
    bot.reply_to(message, get_welcome_message())

@bot.message_handler(commands=["ping"])
def send_ping(message):
    """Обработчик команды /ping."""
    bot.reply_to(message, get_ping_response())

if __name__ == "__main__":
    print("Бот успешно инициализирован. Запуск новой версии...")