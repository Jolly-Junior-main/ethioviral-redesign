import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the pink/pastel body background with the brand purple gradient
old_bg = "background: linear-gradient(135deg, #f3d1e1 0%, #b8b1d9 50%, #9ba1d0 100%);"
new_bg = "background: linear-gradient(135deg, #270659 0%, #4a0bb3 50%, #7b27e8 100%);"
html = html.replace(old_bg, new_bg)

# Replace the pastel text color in buttons (e.g. #9ba1d0) with the brand purple (#4a0bb3)
html = html.replace('#9ba1d0', '#4a0bb3')

# Replace the other pastel color (#b8b1d9) used for hovers to a slightly lighter brand purple
html = html.replace('#b8b1d9', '#7b27e8')

# The SVG check icon in the login card had a stroke="#9ba1d0" which will now be stroke="#4a0bb3"

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
