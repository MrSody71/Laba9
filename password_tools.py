import string
import secrets


def generate_password(length: int = 12, use_digits: bool = True, use_special: bool = True) -> str:
    """
    Генерирует безопасный пароль указанной длины с возможностью включения цифр и специальных символов.
    
    :param length: Длина пароля (по умолчанию 12).
    :param use_digits: Включать ли цифры (по умолчанию True).
    :param use_special: Включать ли специальные символы (по умолчанию True).
    :return: Сгенерированный пароль.
    """
    characters = string.ascii_letters  # Буквы верхнего и нижнего регистра
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))


def check_strength(password: str) -> str:
    """
    Проверяет надежность пароля.

    :param password: Пароль для оценки.
    :return: 'Weak', 'Medium' или 'Strong'.
    """
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length < 8 or not (has_digit or has_lower or has_upper or has_special):
        return 'Weak'
    
    if length >= 8 and has_digit and (has_lower or has_upper):
        return 'Medium'
    
    if length >= 12 and has_lower and has_upper and has_digit and has_special:
        return 'Strong'
    
    return 'Medium'
