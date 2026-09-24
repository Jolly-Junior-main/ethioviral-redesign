import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_bg_html = """
        <!-- Background Image Layer -->
        <div class="absolute inset-0 z-0 pointer-events-none" style="-webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%); mask-image: linear-gradient(to bottom, black 60%, transparent 100%);">
            <img src="hero-bg-city.png" alt="City Background" class="w-full h-full object-cover object-center" />
            <!-- Subtle brand tint to unify colors -->
            <div class="absolute inset-0 bg-[#4a0bb3]/20 mix-blend-overlay"></div>
        </div>
"""

header_open_tag = '<header class="relative min-h-screen flex flex-col justify-between items-center overflow-hidden bg-transparent">'

if header_open_tag in html:
    html = html.replace(header_open_tag, header_open_tag + hero_bg_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Could not find header tag")
