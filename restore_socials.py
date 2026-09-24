import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the original socials block
original_socials = """<!-- Socials -->
                <div class="flex gap-3">
                    <button type="button" class="flex-1 bg-gradient-to-b from-white to-gray-100 h-11 rounded-[1.2rem] flex items-center justify-center hover:scale-105 transition-transform shadow-md">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="black"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.04 2.26-.79 3.59-.72 1.54.04 2.76.67 3.51 1.76-3.06 1.78-2.52 6.06.49 7.34-.69 1.63-1.63 3.01-2.67 3.79zm-3.41-14c.48-1.74-1.01-3.6-2.92-3.66-.54 1.84 1.25 3.65 2.92 3.66z"/></svg>
                    </button>
                    <button type="button" class="flex-1 bg-gradient-to-b from-white to-gray-100 h-11 rounded-[1.2rem] flex items-center justify-center hover:scale-105 transition-transform shadow-md">
                        <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
                    </button>
                    <button type="button" class="flex-1 bg-gradient-to-b from-white to-gray-100 h-11 rounded-[1.2rem] flex items-center justify-center hover:scale-105 transition-transform shadow-md">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="black"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </button>
                </div>"""

# Find the start of the socials block
start_idx = html.find('<!-- Socials -->')
# Find the end of the socials block (the closing </div> for the socials)
# We know it ends before <!-- Right Side:
end_idx = html.find('<!-- Right Side:', start_idx)

if start_idx != -1 and end_idx != -1:
    # Just to make sure we don't accidentally cut out the closing div of the card itself,
    # let's only replace the specific div containing the buttons.
    # Actually, the original_socials block is self-contained. 
    # Let's find exactly `</div>\n            </div>\n\n            <!-- Right Side:`
    
    # We will replace from <!-- Socials --> up to `</div>\n            </div>`
    
    # Alternatively, use regex:
    new_html = re.sub(r'<!-- Socials -->.*?</div>\s*</div>', original_socials + '\n            </div>', html, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Success")
else:
    print("Could not find socials block")
