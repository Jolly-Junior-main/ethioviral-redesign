import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the layout container to justify-end instead of justify-between
html = html.replace(
    'items-center justify-between pb-12 pt-12 lg:pt-0"',
    'items-center justify-end pb-12 pt-12 lg:pt-0"'
)

# 2. Update the login card comment and size
html = html.replace('<!-- Left Side: Login Card -->', '<!-- Right Side: Login Card -->')
html = html.replace('w-full max-w-[380px] bg-white/20', 'w-full max-w-[420px] bg-white/20')

# 3. Remove the massive ETHIOVIRAL text completely
text_block_pattern = r'<!-- Right Side: The massive text shifted slightly right/center -->\s*<div class="pointer-events-none hidden lg:flex flex-col justify-center items-center w-full mt-24">\s*<div class="text-white/80 text-6xl xl:text-9xl font-light tracking-\[0\.5em\] xl:tracking-\[1em\] ml-\[0\.5em\] xl:ml-\[1em\]">ETHIOVIRAL</div>\s*</div>'

html = re.sub(text_block_pattern, '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
