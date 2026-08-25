import pytest

from main import parse_expense


def test_parse_expense_success():
    """Тестируем успешный парсинг корректной строки расхода."""
    amount, category = parse_expense("150.50 продукты")
    assert amount == 150.50
    assert category == "продукты"


def test_parse_expense_invalid_format():
    """Тестируем ошибку при неверном формате (отсутствует категория)."""
    with pytest.raises(ValueError, match="Неверный формат"):
        parse_expense("500")


def test_parse_expense_invalid_amount():
    """Тестируем ошибку, если вместо суммы передана строка."""
    with pytest.raises(ValueError, match="Сумма должна быть числом"):
        parse_expense("abc такси")


def test_parse_expense_negative_amount():
    """Тестируем ошибку при отрицательной или нулевой сумме."""
    with pytest.raises(ValueError, match="Сумма должна быть больше нуля"):
        parse_expense("-50 кофе")