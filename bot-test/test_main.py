from main import get_welcome_message


def test_welcome_message():
    """Тестируем, что функция возвращает правильную строку."""
    message = get_welcome_message()
    assert "Привет!" in message
    assert isinstance(message, str)


def test_token_exists():
    """Тестируем логику работы с токеном."""
    import os

    # Проверяем, что дефолтное значение подставляется, если переменная пустая
    if "TELEGRAM_BOT_TOKEN" not in os.environ:
        from main import TOKEN

        assert TOKEN == "MOCK_TOKEN_FOR_TESTS"
