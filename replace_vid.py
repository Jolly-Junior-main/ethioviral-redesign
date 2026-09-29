import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the img tag with a video tag
old_tag = '<img src="hero-bg-city.png" alt="City Background" class="w-full h-full object-cover object-center" />'
new_tag = '<video autoplay loop muted playsinline class="w-full h-full object-cover object-center">\n                <source src="hero_video.mp4" type="video/mp4">\n            </video>'

if old_tag in html:
    html = html.replace(old_tag, new_tag)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced img with video tag successfully.")
else:
    print("Could not find the exact img tag. Trying regex...")
    # fallback regex
    html, count = re.subn(r'<img src="hero-bg-city[^>]+>', new_tag, html)
    if count > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Replaced img with video tag using regex.")
    else:
        print("Still couldn't find it.")
