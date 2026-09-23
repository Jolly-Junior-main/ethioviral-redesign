import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new hero content block
new_hero_content = """
        <div class="relative z-10 flex-grow w-full max-w-[1400px] mx-auto px-4 md:px-12 flex flex-col lg:flex-row items-center justify-between pb-12 pt-12 lg:pt-0">
            <h1 class="sr-only">Ethio Viral</h1>
            
            <!-- Left Side: Login Card -->
            <div class="relative z-20 w-full max-w-[380px] bg-[#2a6db5]/80 backdrop-blur-xl border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.3)] rounded-[2rem] p-8">
                
                <!-- Icon -->
                <div class="w-16 h-16 bg-gradient-to-b from-white to-gray-200 rounded-[1.2rem] shadow-md mx-auto mb-4 flex flex-col items-center justify-center relative overflow-hidden">
                    <div class="w-5 h-5 bg-[#ff4a4a] rounded-full absolute top-3"></div>
                    <div class="w-8 h-6 bg-[#3b7ac8] absolute bottom-2" style="clip-path: polygon(50% 0%, 0% 100%, 100% 100%);"></div>
                </div>

                <h2 class="text-white text-[22px] font-medium text-center mb-8 tracking-tight">Login to your account</h2>

                <form class="space-y-5">
                    <!-- Email -->
                    <div>
                        <label class="text-white/90 text-[13px] font-medium mb-1.5 block">Email Address</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-white/60" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                            </div>
                            <input type="email" value="james@gmail.com" class="w-full bg-[#1b508f]/60 border border-white/10 rounded-2xl pl-11 pr-4 py-3 text-white text-sm focus:outline-none focus:border-white/30 focus:bg-[#1b508f]/80 transition">
                        </div>
                    </div>

                    <!-- Password -->
                    <div>
                        <label class="text-white/90 text-[13px] font-medium mb-1.5 block">Password</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-white/60" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            </div>
                            <input type="password" value="password123" class="w-full bg-[#1b508f]/60 border border-white/10 rounded-2xl pl-11 pr-11 py-3 text-white text-sm font-mono tracking-widest focus:outline-none focus:border-white/30 focus:bg-[#1b508f]/80 transition">
                            <div class="absolute inset-y-0 right-0 pr-4 flex items-center cursor-pointer">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-white/60 hover:text-white transition" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                            </div>
                        </div>
                    </div>

                    <!-- Remember & Forgot -->
                    <div class="flex items-center justify-between pt-1">
                        <label class="flex items-center gap-2 cursor-pointer group">
                            <div class="w-4 h-4 rounded bg-white flex items-center justify-center">
                                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#2a6db5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            </div>
                            <span class="text-white text-[13px]">Keep me logged in</span>
                        </label>
                        <a href="#" class="text-white text-[13px] hover:underline decoration-white/50 underline-offset-4">Forgot password?</a>
                    </div>

                    <!-- Login Button -->
                    <button type="button" class="w-full bg-gradient-to-r from-[#4ec9e9] to-[#2597d9] text-white font-medium text-[15px] py-3.5 rounded-[1.2rem] shadow-[0_8px_20px_rgba(78,201,233,0.3)] hover:shadow-[0_8px_25px_rgba(78,201,233,0.4)] hover:-translate-y-0.5 transition-all mt-2">
                        Login
                    </button>
                </form>

                <!-- Divider -->
                <div class="flex items-center gap-4 my-7">
                    <div class="flex-1 h-px bg-white/20"></div>
                    <span class="text-white/70 text-[11px] font-bold tracking-widest uppercase">OR</span>
                    <div class="flex-1 h-px bg-white/20"></div>
                </div>

                <!-- Socials -->
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
                </div>
            </div>

            <!-- Right Side: The massive text shifted slightly right/center -->
            <div class="pointer-events-none hidden lg:flex flex-col justify-center items-center w-full mt-24">
                <div class="text-[#0F172A]/80 text-6xl xl:text-9xl font-light tracking-[0.5em] xl:tracking-[1em] ml-[0.5em] xl:ml-[1em]">ETHIOVIRAL</div>
            </div>

            <!-- Scroll indicator -->
            <div class="absolute bottom-8 left-1/2 -translate-x-1/2 text-[#0F172A] text-[10px] font-bold tracking-[0.5em] uppercase pointer-events-none opacity-100">
                Scroll Down
            </div>
        </div>
"""

# Replace the block
start_tag = '<div class="relative z-10 flex-grow flex flex-col justify-end items-center pb-12 w-full">'
end_tag = '</div>\n    </header>'

start_idx = html.find(start_tag)
if start_idx != -1:
    end_idx = html.find(end_tag, start_idx) + len('</div>')
    new_html = html[:start_idx] + new_hero_content + html[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Success")
else:
    print("Could not find start tag")
