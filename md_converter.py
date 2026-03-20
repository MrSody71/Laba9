import re

def convert(markdown_text: str) -> str:
    """
    Преобразует Markdown-текст в HTML.
    Использует разделение на блоки по \n\n+.
    """
    markdown_text = markdown_text.strip()
    
    if not markdown_text:
        return ""
        
    blocks = re.split(r'\n\n+', markdown_text)
    
    result = []
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        if block.startswith('#'):
            level = 0
            for char in block:
                if char == '#':
                    level += 1
                else:
                    break
            
            if level <= 6 and level < len(block) and block[level] == ' ':
                header_text = block[level + 1:].strip()
                header_text = process_inline_elements(header_text)
                result.append(f'<h{level}>{header_text}</h{level}>')
            else:
                block_text = process_inline_elements(block)
                result.append(f'<p>{block_text}</p>')
                
        elif block.startswith('-'):
            lines = block.splitlines()
            list_items = []
            for line in lines:
                line = line.strip()
                if line.startswith('- '):
                    item_text = line[2:].strip()
                    item_text = process_inline_elements(item_text)
                    list_items.append(f'<li>{item_text}</li>')
            if list_items:
                result.append(f'<ul>{"".join(list_items)}</ul>')
            
        else:
            lines = block.splitlines()
            paragraph_parts = [line.strip() for line in lines if line.strip()]
            paragraph_text = " ".join(paragraph_parts)
            paragraph_text = process_inline_elements(paragraph_text)
            result.append(f'<p>{paragraph_text}</p>')
    
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