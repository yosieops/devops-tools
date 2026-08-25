def parse_expense(text: str) -> tuple[float, str]:
    """Парсит строку расхода в формате 'сумма категория'.

    Пример: '350 кофе' -> (350.0, 'кофе')
    """
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:
        raise ValueError("Неверный формат. Используйте: сумма категория")

    try:
        amount = float(parts[0])
    except ValueError as exc:
        raise ValueError("Сумма должна быть числом") from exc

    category = parts[1].strip()
    if amount <= 0:
        raise ValueError("Сумма должна быть больше нуля")

    return amount, category