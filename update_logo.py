import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all "Ethio Viral" to "Ethioviral"
content = content.replace('Ethio Viral', 'Ethioviral')
content = content.replace('EthioViral', 'Ethioviral')

# Navbar Logo
nav_logo_pattern = r'<svg width="24" height="24" viewBox="0 0 24 24" fill="none".*?</svg>\s*RESADEX'
new_nav_logo = '<img src="logo.png" alt="Ethioviral Logo" class="w-8 h-8 rounded-lg shadow-sm">\n                    Ethioviral'
content = re.sub(nav_logo_pattern, new_nav_logo, content, flags=re.DOTALL)

# Footer Logo
footer_logo_pattern = r'<div class="w-8 h-8 bg-\[#15101A\].*?</div>\s*Ethioviral'
new_footer_logo = '<img src="logo.png" alt="Ethioviral Logo" class="w-8 h-8 rounded-lg shadow-sm">\n                    Ethioviral'
content = re.sub(footer_logo_pattern, new_footer_logo, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
