import re

def convert(markdown_text: str) -> str:
    """
    Преобразует Markdown-текст в HTML.
    Поддерживает заголовки, абзацы, списки, жирный текст, курсив, ссылки и код.
    Строки с пробелами не разделяют абзацы.
    """
    if not markdown_text or not markdown_text.strip():
        return ""
        
    lines = markdown_text.splitlines()
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Обработка заголовков
        if line.startswith('#'):
            level = 0
            for char in line:
                if char == '#':
                    level += 1
                else:
                    break
            
            if level <= 6 and level <= len(line) and line[level] == ' ':
                header_text = line[level + 1:].strip()
                header_text = process_inline_elements(header_text)
                result.append(f'<h{level}>{header_text}</h{level}>')
            else:
                result.append(f'<p>{process_inline_elements(line)}</p>')
        
        # Игнорирование пустых строк и строк с пробелами
        elif not line.strip():
            pass
            
        # Обработка ненумерованных списков
        elif line.strip().startswith('- '):
            list_items = []
            # Собираем все элементы списка
            while i < len(lines) and lines[i].strip().startswith('- '):
                item_text = lines[i].strip()[2:]  # Убираем '- '
                item_text = process_inline_elements(item_text)
                list_items.append(f'<li>{item_text}</li>')
                i += 1
            
            # Продвинули i на один шаг назад, так как цикл while увеличит его
            i -= 1
            result.append(f'<ul>{"".join(list_items)}</ul>')
            
        else:
            # Обычный текст - начинаем собирать абзац
            paragraph = []
            while i < len(lines):
                # Запоминаем текущую позицию
                current_line = lines[i]
                
                # Если строка не пустая и не содержит только пробелы, добавляем к абзацу
                if current_line.strip():
                    # Если встречаем заголовок или список, прерываем сбор абзаца
                    if current_line.startswith('#') or current_line.strip().startswith('- '):
                        break
                    paragraph.append(current_line.strip())
                    i += 1
                else:
                    # Если строка содержит только пробелы, пропускаем, но не прерываем абзац
                    i += 1
                    
            # Продвинули i на один шаг назад только если не в конце файла и текущая строка не пустая
            if i < len(lines) and lines[i].strip():
                i -= 1
                
            paragraph_text = " ".join(paragraph)
            paragraph_text = process_inline_elements(paragraph_text)
            result.append(f'<p>{paragraph_text}</p>')
        
        i += 1
    
    return '\n'.join(result)

def process_inline_elements(text: str) -> str:
    """
    Обрабатывает inline-элементы в тексте с использованием регулярных выражений.
    """
    # Жирный текст: **text** -> <strong>text</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    # Курсив: *text* -> <em>text</em>
    text = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    
    # Ссылки: [link name](url) -> <a href="url">link name</a>
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    # Внутристрочный код: `code` -> <code>code</code>
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    return text