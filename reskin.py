import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

hero_split = content.find('<!-- SECTION: See EthioViral in Action')
hero = content[:hero_split]
rest = content[hero_split:]

# Backgrounds
rest = rest.replace('bg-[#0C0907]', 'bg-white')
rest = rest.replace('bg-[#110D0A]', 'bg-slate-50')
rest = rest.replace('bg-[#15110E]', 'bg-white shadow-sm border border-slate-200')
rest = rest.replace('bg-[#1C1715]', 'bg-white shadow-sm border border-slate-200')
rest = rest.replace('bg-[#1C1310]', 'bg-white shadow-sm border border-slate-200')
rest = rest.replace('bg-[#F8EFE4]', 'bg-slate-50')
rest = rest.replace('bg-[#F3E8D8]', 'bg-slate-100')
rest = rest.replace('bg-[#2A1D18]', 'bg-slate-100')
rest = rest.replace('bg-black/20', 'bg-white/50 border border-slate-200')

# Text Colors
rest = rest.replace('text-white', 'text-[#0F172A]')
rest = rest.replace('text-gray-400', 'text-slate-500')
rest = rest.replace('text-gray-500', 'text-slate-400')
rest = rest.replace('text-gray-600', 'text-slate-400')
rest = rest.replace('text-gray-300', 'text-slate-600')

# Accent Colors -> Blue/Slate
rest = rest.replace('text-[#F97316]', 'text-blue-600')
rest = rest.replace('text-[#4ADE80]', 'text-blue-600')
rest = rest.replace('text-[#10B981]', 'text-blue-600')

# Convert big colored buttons to Dark #0F172A
rest = rest.replace('bg-[#F97316]', 'bg-[#0F172A]')
rest = rest.replace('bg-[#4ADE80]', 'bg-[#0F172A]')
rest = rest.replace('hover:bg-[#22c55e]', 'hover:bg-black')
rest = rest.replace('hover:bg-[#E56514]', 'hover:bg-black')
rest = rest.replace('text-black', 'text-white') # Button text

# Hover texts
rest = rest.replace('hover:text-white', 'hover:text-[#0F172A]')
rest = rest.replace('hover:text-[#4ADE80]', 'hover:text-blue-600')

# Borders
rest = rest.replace('border-white/5', 'border-slate-200')
rest = rest.replace('border-white/10', 'border-slate-200')
rest = rest.replace('border-white/20', 'border-slate-300')
rest = rest.replace('border-white/30', 'border-slate-300')
rest = rest.replace('border-[#F97316]/30', 'border-blue-200')
rest = rest.replace('border-black/5', 'border-slate-200')
rest = rest.replace('border-[#4ADE80]/20', 'border-slate-200')

# Transparent buttons with borders
rest = rest.replace('bg-transparent border border-[#D5C5B5] text-[#1C1715]', 'bg-white border border-slate-300 text-[#0F172A] hover:bg-slate-50')
rest = rest.replace('bg-transparent border border-[#E5D5C5] text-white', 'bg-white border border-slate-300 text-[#0F172A] hover:bg-slate-50')

# Strokes and Fills
rest = rest.replace('stroke="#F97316"', 'stroke="#3b82f6"')
rest = rest.replace('stroke="#4ADE80"', 'stroke="#3b82f6"')
rest = rest.replace('stroke="white"', 'stroke="#0F172A"')
# Note: we shouldn't indiscriminately replace fill="white" because some are inside colored boxes. Let's just leave it, or specific ones.

# Group hovers
rest = rest.replace('group-hover:stroke-white', 'group-hover:stroke-[#0F172A]')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(hero + rest)
