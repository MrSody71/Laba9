import pytest
from md_converter import convert

def test_headers():
    """Тестирование всех уровней заголовков от h1 до h6."""
    assert convert("# Заголовок 1") == "<h1>Заголовок 1</h1>"
    
    assert convert("## Заголовок 2") == "<h2>Заголовок 2</h2>"
    
    assert convert("### Заголовок 3") == "<h3>Заголовок 3</h3>"
    
    assert convert("#### Заголовок 4") == "<h4>Заголовок 4</h4>"
    
    assert convert("##### Заголовок 5") == "<h5>Заголовок 5</h5>"
    
    assert convert("###### Заголовок 6") == "<h6>Заголовок 6</h6>"
    
    assert convert("####### Слишком много #") == "<p>####### Слишком много #</p>"
    assert convert("#Без пробела") == "<p>#Без пробела</p>"

def test_inline_elements():
    """Тестирование сложных строк с жирным текстом, курсивом и ссылками."""
    assert convert("**Жирный** текст") == "<p><strong>Жирный</strong> текст</p>"
    
    assert convert("*Курсив* текст") == "<p><em>Курсив</em> текст</p>"
    
    assert convert("Текст со [ссылкой](http://example.com)") == "<p>Текст со <a href=\"http://example.com\">ссылкой</a></p>"
    
    assert convert("**Жирный** текст со [ссылкой](http://ex.com)") == "<p><strong>Жирный</strong> текст со <a href=\"http://ex.com\">ссылкой</a></p>"
    
    assert convert("**Жирный** и *Курсив* с [ссылкой](https://test.com) и `код`") == "<p><strong>Жирный</strong> и <em>Курсив</em> с <a href=\"https://test.com\">ссылкой</a> и <code>код</code></p>"

def test_lists():
    """Тестирование ненумерованных списков и корректного закрытия тегов."""
    assert convert("- Элемент списка") == "<ul><li>Элемент списка</li></ul>"
    
    input_text = "- Первый\n- Второй\n- Третий"
    expected = "<ul><li>Первый</li><li>Второй</li><li>Третий</li></ul>"
    assert convert(input_text) == expected
    
    input_text = "- **Жирный** элемент\n- Элемент со [ссылкой](http://list.com)"
    expected = "<ul><li><strong>Жирный</strong> элемент</li><li>Элемент со <a href=\"http://list.com\">ссылкой</a></li></ul>"
    assert convert(input_text) == expected

def test_paragraphs():
    """Тестирование нескольких абзацев текста."""
    assert convert("Простой текст") == "<p>Простой текст</p>"
    
    input_text = "Первый абзац\n\nВторой абзац\n\nТретий абзац"
    expected = "<p>Первый абзац</p>\n<p>Второй абзац</p>\n<p>Третий абзац</p>"
    assert convert(input_text) == expected
    
    input_text = "Первая строка абзаца\nВторая строка абзаца"
    expected = "<p>Первая строка абзаца Вторая строка абзаца</p>"
    assert convert(input_text) == expected
    
    input_text = "# Заголовок\n\nПервый абзац\n\n- Список\n\nВторой абзац"
    expected = "<h1>Заголовок</h1>\n<p>Первый абзац</p>\n<ul><li>Список</li></ul>\n<p>Второй абзац</p>"
    assert convert(input_text) == expected

def test_edge_cases():
    """Тестирование граничных случаев."""
    assert convert("") == ""
    
    assert convert("\n\n\n") == ""
    
    assert convert("   ") == ""
    
    input_text = "Текст\n   \nДругой текст"
    expected = "<p>Текст Другой текст</p>"
    assert convert(input_text) == expected