import re
import sys

def convert(text):
    text = re.sub(r'^## (.*)', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*)', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(
        r'btn\{(.*?)\}=\[(.*?)\]',
        r'<a href="\2" class="btn">\1</a>',
        text
    )
    text = re.sub(
        r'!!warn\{(.*?)\}',
        r'<div class="warning">\1</div>',
        text
    )
    return text

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    html = convert(content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
