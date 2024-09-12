import difflib
import os


def compare(output_html):
    with open("original.txt", 'r', encoding='utf-8') as f1, open("after.txt", 'r', encoding='utf-8') as f2:
        original_text = f1.read()
        gengai_text = f2.read()
    
    html_content = '''
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                background-color: white;
                text-align: center;
                font-family: Arial, sans-serif;
            }
            .content {
                display: inline-block;
                text-align: left;
                max-width: 80%;
                margin: auto;
                white-space: pre-wrap;
            }
            .added {
                color: green;
            }
            .removed {
                color: orange;
                text-decoration: line-through;
            }
        </style>
    </head>
    <body>
    <div class="content">
    '''
    
    matcher = difflib.SequenceMatcher(None, original_text, gengai_text)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            html_content += original_text[i1:i2].replace("\n", "<br>")
        elif tag == 'insert':
            added_text = gengai_text[j1:j2].replace("\n", "<br>")
            html_content += f'<span class="added">{added_text}</span>'
        elif tag == 'delete':
            removed_text = original_text[i1:i2].replace("\n", "<br>")
            html_content += f'<span class="removed">{removed_text}</span>'
        elif tag == 'replace':
            removed_text = original_text[i1:i2].replace("\n", "<br>")
            added_text = gengai_text[j1:j2].replace("\n", "<br>")
            html_content += f'<span class="removed">{removed_text}</span>'
            html_content += f'<span class="added">{added_text}</span>'
    
    html_content += '''
    </div>
    </body>
    </html>
    '''
    
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    os.system(f"start {output_html}")  # 可选，自动打开输出结果

compare('result.html')
