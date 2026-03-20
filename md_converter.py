import re

def convert(markdown_text: str) -> str:
    """
    Преобразует Markdown-текст в HTML.
    Поддерживает заголовки, абзацы, списки, жирный текст, курсив, ссылки и код.
    """
    lines = markdown_text.splitlines()
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
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
        
        elif line.strip() == '':
            pass
            
        elif line.strip().startswith('- '):
            list_items = []
            while i < len(lines) and lines[i].strip().startswith('- '):
                item_text = lines[i].strip()[2:]  
                item_text = process_inline_elements(item_text)
                list_items.append(f'<li>{item_text}</li>')
                i += 1
            
            i -= 1
            result.append(f'<ul>{"".join(list_items)}</ul>')
            
        else:
            paragraph = []
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('#') and not lines[i].strip().startswith('- '):
                paragraph.append(lines[i].strip())
                i += 1
            
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
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    text = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    return text