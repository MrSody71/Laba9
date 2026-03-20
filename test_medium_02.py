import pytest
from password_tools import generate_password, check_strength
import string

def test_generate_password_length():
    """Проверяет, что длина сгенерированного пароля соответствует заданной."""
    for length in [8, 12, 16]:
        password = generate_password(length)
        assert len(password) == length, f"Длина пароля {len(password)} не соответствует ожидаемой {length}"


def test_generate_password_special_characters():
    """Проверяет, что в пароле есть спецсимволы, если use_special=True."""
    password = generate_password(length=12, use_digits=True, use_special=True)
    assert any(c in string.punctuation for c in password), "В пароле отсутствуют спецсимволы при use_special=True"

    password_no_special = generate_password(length=12, use_digits=True, use_special=False)
    assert not any(c in string.punctuation for c in password_no_special), "В пароле есть спецсимволы при use_special=False"


def test_check_strength_weak():
    """Проверяет, что функция возвращает 'Weak' для слабых паролей."""
    assert check_strength("123") == 'Weak'  
    assert check_strength("abc") == 'Weak' 
    assert check_strength("") == 'Weak'     
    assert check_strength("abcdefgh") == 'Weak'  


def test_check_strength_medium():
    """Проверяет, что функция возвращает 'Medium' для паролей средней надежности."""
    assert check_strength("abcdefgh1") == 'Medium'  
    assert check_strength("ABC123456") == 'Medium'  


def test_check_strength_strong():
    """Проверяет, что функция возвращает 'Strong' для надежных паролей."""
    assert check_strength("Abc123!@#") == 'Strong'  
    assert check_strength("Abcdefg1!@#") == 'Weak'  
    strong_password = "A1b2C3d4!@#$"
    assert len(strong_password) >= 12
    assert check_strength(strong_password) == 'Strong'
