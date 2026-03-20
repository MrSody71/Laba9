def convert(markdown_text: str) -> str:
    """
    Преобразует Markdown-текст в HTML.
    Поддерживает заголовки (# Header -> <h1>Header</h1>) и абзацы.
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
                result.append(f'<h{level}>{header_text}</h{level}>')
            else:
                result.append(f'<p>{line}</p>')
        
        elif line.strip() == '':
            pass
        
        else:
            paragraph = []
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('#'):
                paragraph.append(lines[i].strip())
                i += 1
            
            i -= 1
            result.append(f'<p>{" ".join(paragraph)}</p>')
        
        i += 1
    
    return '\n'.join(result)