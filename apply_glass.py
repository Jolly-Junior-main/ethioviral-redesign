import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_end = html.find('</header>')
if hero_end != -1:
    hero_end += len('</header>')
    hero = html[:hero_end]
    rest = html[hero_end:]
else:
    hero = html
    rest = ""

# 1. Update Body Background
# New background is a pastel gradient: from pastel pink to pastel purple/blue, like the dribbble shot
# We'll put it on the body and make sections transparent.
new_body_style = "body { font-family: 'Plus Jakarta Sans', sans-serif; background: linear-gradient(135deg, #f3d1e1 0%, #b8b1d9 50%, #9ba1d0 100%); background-attachment: fixed; color: white; }"
hero = hero.replace("body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: white; color: #0F172A; }", new_body_style)
hero = hero.replace('<body class="antialiased overflow-x-hidden">', '<body class="antialiased overflow-x-hidden text-white">')

if rest:
    # 2. Strip background colors from sections
    rest = re.sub(r'class="([^"]*)bg-white([^"]*)"', r'class="\1bg-transparent\2"', rest)
    rest = re.sub(r'class="([^"]*)bg-slate-50([^"]*)"', r'class="\1bg-transparent\2"', rest)
    rest = re.sub(r'class="([^"]*)bg-slate-100([^"]*)"', r'class="\1bg-transparent\2"', rest)
    
    # 3. Cards & Borders
    # The current cards have classes like `bg-transparent shadow-sm border border-slate-200`
    # Let's replace the whole string for the common card base.
    rest = rest.replace('bg-transparent shadow-sm border border-slate-200 border border-slate-200', 'bg-white/20 backdrop-blur-xl border border-white/30 shadow-[0_8px_32px_0_rgba(31,38,135,0.1)]')
    rest = rest.replace('bg-transparent shadow-sm border border-slate-200 border border-blue-200', 'bg-white/20 backdrop-blur-xl border border-white/40 shadow-[0_8px_32px_0_rgba(31,38,135,0.1)]')
    rest = rest.replace('bg-transparent shadow-sm border border-slate-200', 'bg-white/20 backdrop-blur-xl border border-white/30 shadow-[0_8px_32px_0_rgba(31,38,135,0.1)]')
    rest = rest.replace('border-slate-200', 'border-white/20')
    rest = rest.replace('border-slate-300', 'border-white/30')
    rest = rest.replace('border-slate-100', 'border-white/10')
    rest = rest.replace('border-[#151F17]', 'border-white/40')
    
    # 4. Text Colors
    rest = rest.replace('text-[#0F172A]', 'text-white')
    rest = rest.replace('text-slate-600', 'text-white/80')
    rest = rest.replace('text-slate-500', 'text-white/70')
    rest = rest.replace('text-slate-400', 'text-white/60')
    rest = rest.replace('text-slate-300', 'text-white/50')
    rest = rest.replace('text-slate-800', 'text-white')
    rest = rest.replace('text-slate-900', 'text-white')
    rest = rest.replace('text-black', 'text-white')
    
    # Buttons
    rest = rest.replace('bg-[#0F172A]', 'bg-white text-[#9ba1d0] font-bold') # For primary black buttons -> white buttons with purple text
    rest = rest.replace('hover:bg-black', 'hover:bg-white/90 hover:text-[#b8b1d9]')
    
    # Filter pill buttons (e.g. YouTube, Telegram)
    rest = rest.replace('bg-white text-white', 'bg-white/30 text-white') # The active one
    rest = rest.replace('hover:bg-white/5', 'hover:bg-white/20')
    
    # Accents & Strokes
    rest = rest.replace('stroke="#0F172A"', 'stroke="white"')
    rest = rest.replace('stroke="#3b82f6"', 'stroke="white"')
    
    # Remove random backgrounds
    rest = rest.replace('bg-[#15101A]', 'bg-white/10 backdrop-blur-md')
    rest = rest.replace('bg-[#E6F4EA]', 'bg-green-400/20')
    rest = rest.replace('bg-[#FEF3C7]', 'bg-yellow-400/20')

    # Remove the grid pattern background from the final section
    rest = rest.replace('bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)]', '')

html = hero + rest

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
