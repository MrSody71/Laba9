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
