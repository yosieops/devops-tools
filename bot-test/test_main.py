import os
from main import get_welcome_message, get_ping_response


def test_welcome_message():
    """Тестируем, что функция возвращает правильную строку."""
    message = get_welcome_message()
    assert "Привет!" in message
    assert isinstance(message, str)


def test_ping_response():
    """Тестируем ответ на команду /ping."""
    message = get_ping_response()
    assert "Pong!" in message
    assert isinstance(message, str)


def test_token_exists():
    """Тестируем логику работы с токеном."""
    # Проверяем, что дефолтное значение подставляется, если переменная пустая
    if "TELEGRAM_BOT_TOKEN" not in os.environ:
        from main import TOKEN

        assert TOKEN == "MOCK_TOKEN_FOR_TESTS"