import html
from re import compile, match, sub

URL_PATTERN = compile(
    r'(https?://\S+)'
)


def auto_link_urls(text):
    def replacer(matchs):
        url = matchs.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'

    return URL_PATTERN.sub(replacer, text)


def parse_lists(paragraphs):
    html_paragraphs = []
    list_buffer = []
    list_type = None

    def flush_list():
        nonlocal list_buffer, list_type
        if not list_buffer:
            return ''
        tag = list_type or 'ul'
        items = ''.join(f'<li>{item.strip()}</li>' for item in list_buffer)
        list_html = f'<{tag}>{items}</{tag}>'
        list_buffer = []
        list_type = None
        return list_html

    for para in paragraphs:
        lines = para.split('\n')
        normal_lines = []
        for line in lines:
            if match(r'^(\s*[-*]\s+)', line):
                if normal_lines:
                    html_paragraphs.append('<p>' + '<br>'.join(normal_lines) + '</p>')
                    normal_lines = []
                list_type = 'ul'
                list_item = sub(r'^\s*[-*]\s+', '', line)
                list_buffer.append(list_item)
            elif match(r'^\s*\d+\.\s+', line):
                if normal_lines:
                    html_paragraphs.append('<p>' + '<br>'.join(normal_lines) + '</p>')
                    normal_lines = []
                list_type = 'ol'
                list_item = sub(r'^\s*\d+\.\s+', '', line)
                list_buffer.append(list_item)
            else:
                if list_buffer:
                    html_paragraphs.append(flush_list())
                normal_lines.append(line)
        if list_buffer:
            html_paragraphs.append(flush_list())
        if normal_lines:
            html_paragraphs.append('<p>' + '<br>'.join(normal_lines) + '</p>')

    return ''.join(html_paragraphs)


def plain_text_to_advanced_html(text):
    from re import split
    escaped = html.escape(text)
    paragraphs = split(r'\n{2,}', escaped)
    html_with_lists = parse_lists(paragraphs)
    final_html = auto_link_urls(html_with_lists)

    return final_html
