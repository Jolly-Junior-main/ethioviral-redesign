import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_end = html.find('</header>')
if header_end != -1:
    header_end += len('</header>')
    hero = html[:header_end]
    rest = html[header_end:]
    
    # 1. Remove bg-slate-300
    hero = hero.replace('bg-slate-300', 'bg-transparent')
    
    # 2. Remove the image background
    hero = re.sub(r'<!-- Background Image \(User\'s design\) -->\s*<div class="absolute inset-0 z-0">\s*<img src="hero-bg.jpg"[^>]+>\s*</div>', '', hero)
    
    # 3. Navbar styling
    hero = hero.replace('bg-white/40 backdrop-blur-md border border-white/40', 'bg-white/20 backdrop-blur-xl border border-white/30')
    hero = hero.replace('font-bold text-[#0F172A] tracking-wide', 'font-bold text-white tracking-wide')
    hero = hero.replace('text-[#0F172A] px-6 py-2 rounded-full font-medium text-sm hover:bg-white/30', 'text-white px-6 py-2 rounded-full font-medium text-sm hover:bg-white/30')
    hero = hero.replace('bg-white text-[#0F172A] px-6 py-2', 'bg-white text-[#9ba1d0] px-6 py-2') # The active Home pill
    hero = hero.replace('bg-[#0F172A] text-white px-8 py-3 rounded-full font-medium text-sm hover:bg-black', 'bg-white text-[#9ba1d0] px-8 py-3 rounded-full font-bold text-sm hover:bg-white/90')
    
    # 4. Login Card
    hero = hero.replace('bg-[#2a6db5]/80 backdrop-blur-xl border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.3)]', 'bg-white/20 backdrop-blur-xl border border-white/30 shadow-[0_8px_32px_0_rgba(31,38,135,0.1)]')
    
    # Login inputs
    hero = hero.replace('bg-[#1b508f]/60 border border-white/10', 'bg-white/10 border border-white/20')
    hero = hero.replace('focus:bg-[#1b508f]/80', 'focus:bg-white/20')
    
    # Checkbox stroke
    hero = hero.replace('stroke="#2a6db5"', 'stroke="#9ba1d0"')
    
    # Login button
    hero = hero.replace('bg-gradient-to-r from-[#4ec9e9] to-[#2597d9] text-white font-medium text-[15px] py-3.5 rounded-[1.2rem] shadow-[0_8px_20px_rgba(78,201,233,0.3)] hover:shadow-[0_8px_25px_rgba(78,201,233,0.4)]', 'bg-white text-[#9ba1d0] font-bold text-[15px] py-3.5 rounded-[1.2rem] shadow-[0_8px_32px_0_rgba(31,38,135,0.1)] hover:bg-white/90')
    
    # Social buttons (make them glass too)
    hero = hero.replace('bg-gradient-to-b from-white to-gray-100', 'bg-white/20 backdrop-blur-md border border-white/30')
    hero = hero.replace('fill="black"', 'fill="white"')
    hero = hero.replace('fill="#4285F4"', 'fill="white"')
    hero = hero.replace('fill="#34A853"', 'fill="white"')
    hero = hero.replace('fill="#FBBC05"', 'fill="white"')
    hero = hero.replace('fill="#EA4335"', 'fill="white"')
    
    # 5. Giant Text
    hero = hero.replace('text-[#0F172A]/80', 'text-white/80')
    hero = hero.replace('text-[#0F172A]', 'text-white') # Catches scroll down text
    
    html = hero + rest
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done")
else:
    print("Could not find </header>")
