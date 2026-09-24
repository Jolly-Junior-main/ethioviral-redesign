import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the boundaries
start_marker = '<!-- SECTION: Every important step stays visible (Screenshot 2) -->'
end_marker = '<!-- SECTION: Grow an audience. Deliver something useful. (Screenshot 3) -->'

if start_marker in html and end_marker in html:
    # Everything before start_marker
    prefix = html.split(start_marker)[0]
    # Everything after end_marker
    suffix = html.split(end_marker)[1]
    
    # New section HTML
    new_section = """<!-- SECTION: Every important step stays visible (Screenshot 2) -->
    <section class="bg-transparent py-24 px-6 lg:px-12 relative overflow-hidden">
        <div class="max-w-7xl mx-auto">
            
            <!-- Section Header -->
            <div class="mb-16">
                <div class="text-white/80 font-bold text-[10px] tracking-widest uppercase mb-3">DESIGNED AROUND REAL ACTIONS</div>
                <h2 class="text-4xl md:text-6xl font-black mb-6 leading-[1.1] tracking-tight text-white">Every important step stays<br>visible.</h2>
                <p class="text-white/60 text-sm max-w-xl leading-relaxed">
                    Explore the information customers use to place, fund, and track an order. These previews follow the same structure as the product, so the experience is easy on desktop and mobile.
                </p>
            </div>

            <!-- Bento Grid Dashboard -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Left Column (Main widgets) -->
                <div class="lg:col-span-8 flex flex-col gap-6">
                    
                    <!-- Activity & Quick Stats row -->
                    <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 flex flex-col md:flex-row gap-6 shadow-xl relative overflow-hidden">
                        <!-- Chart Area -->
                        <div class="flex-1">
                            <div class="flex justify-between items-center mb-6">
                                <h3 class="text-white font-semibold text-lg tracking-tight">My activity</h3>
                                <span class="text-white/80 text-[11px] font-bold cursor-pointer hover:text-white transition">See all ></span>
                            </div>
                            
                            <!-- Simple Bar Chart Mockup -->
                            <div class="flex items-end justify-between h-32 gap-3 mt-4 px-2">
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white/20 rounded-t-md h-12 transition-all hover:bg-white/30 cursor-pointer"></div><span class="text-white/60 font-medium text-[10px]">Mon</span></div>
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white/20 rounded-t-md h-16 transition-all hover:bg-white/30 cursor-pointer"></div><span class="text-white/60 font-medium text-[10px]">Tue</span></div>
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white/20 rounded-t-md h-14 transition-all hover:bg-white/30 cursor-pointer"></div><span class="text-white/60 font-medium text-[10px]">Wed</span></div>
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.5)] rounded-t-md h-28 cursor-pointer relative"><div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-[#4a0bb3] text-white text-[9px] font-bold px-2 py-1 rounded shadow-lg opacity-0 hover:opacity-100 transition-opacity">Peak</div></div><span class="text-white font-bold text-[10px]">Thu</span></div>
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white/20 rounded-t-md h-10 transition-all hover:bg-white/30 cursor-pointer"></div><span class="text-white/60 font-medium text-[10px]">Fri</span></div>
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white/20 rounded-t-md h-20 transition-all hover:bg-white/30 cursor-pointer"></div><span class="text-white/60 font-medium text-[10px]">Sat</span></div>
                                <div class="w-full flex flex-col items-center gap-2"><div class="w-full bg-white/20 rounded-t-md h-16 transition-all hover:bg-white/30 cursor-pointer"></div><span class="text-white/60 font-medium text-[10px]">Sun</span></div>
                            </div>
                        </div>
                        
                        <!-- Side Mini Cards -->
                        <div class="w-full md:w-56 flex flex-col gap-4">
                            <!-- Card 1 -->
                            <div class="bg-white/10 border border-white/20 rounded-2xl p-4 flex flex-col justify-between h-full relative group hover:bg-white/20 transition cursor-pointer">
                                <div class="flex justify-between items-start mb-2">
                                    <span class="bg-white text-[#4a0bb3] text-[10px] font-bold px-3 py-1 rounded-full shadow-sm">10:00</span>
                                    <div class="w-6 h-6 rounded-full bg-[#111] flex items-center justify-center shadow-sm">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                                    </div>
                                </div>
                                <p class="text-white text-sm font-semibold leading-tight">Instagram<br><span class="text-white/70 font-medium text-xs">Likes Added</span></p>
                            </div>
                            <!-- Card 2 -->
                            <div class="bg-white/10 border border-white/20 rounded-2xl p-4 flex flex-col justify-between h-full relative group hover:bg-white/20 transition cursor-pointer">
                                <div class="flex justify-between items-start mb-2">
                                    <span class="bg-[#4a0bb3] text-white text-[10px] font-bold px-3 py-1 rounded-full shadow-sm">12:00</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
                                </div>
                                <p class="text-white text-sm font-semibold leading-tight">TikTok<br><span class="text-white/70 font-medium text-xs">Views Pending!</span></p>
                            </div>
                        </div>
                    </div>

                    <!-- Top Platforms (Avatars) -->
                    <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl relative">
                        <div class="flex justify-between items-center mb-6">
                            <h3 class="text-white font-semibold text-lg tracking-tight">Top Platforms</h3>
                            <span class="text-white/80 text-[11px] font-bold cursor-pointer hover:text-white transition">See all ></span>
                        </div>
                        <div class="flex items-center gap-6 overflow-x-auto pb-2 scrollbar-hide">
                            <!-- Avatar 1 -->
                            <div class="flex flex-col items-center gap-3 group cursor-pointer min-w-[75px]">
                                <div class="relative">
                                    <div class="w-16 h-16 rounded-full bg-gradient-to-tr from-pink-500 to-yellow-500 p-[2px] shadow-lg group-hover:scale-110 transition-transform duration-300"><div class="w-full h-full bg-white rounded-full flex items-center justify-center overflow-hidden"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" class="w-8 h-8"></div></div>
                                    <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-4 h-4 bg-white rounded-full flex items-center justify-center border-2 border-[#4a0bb3]"><div class="w-2 h-2 bg-black rounded-full"></div></div>
                                </div>
                                <span class="text-white text-xs font-semibold">Instagram</span>
                            </div>
                            <!-- Avatar 2 -->
                            <div class="flex flex-col items-center gap-3 group cursor-pointer min-w-[75px]">
                                <div class="relative">
                                    <div class="w-16 h-16 rounded-full bg-[#111] p-[2px] shadow-lg group-hover:scale-110 transition-transform duration-300"><div class="w-full h-full bg-[#111] rounded-full flex items-center justify-center overflow-hidden"><svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.34 2.88 2.88 0 0 1 2.9-3.93c.24 0 .47.03.69.08V9.69a6.23 6.23 0 0 0-4.04-.44 6.32 6.32 0 0 0-4.5 4.9 6.3 6.3 0 0 0 2.22 6.22 6.32 6.32 0 0 0 7.82-.7 6.27 6.27 0 0 0 2-4.57V8.5a8.28 8.28 0 0 0 5.33 1.94v-3.75z"/></svg></div></div>
                                    <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-4 h-4 bg-white rounded-full flex items-center justify-center border-2 border-[#4a0bb3]"><div class="w-2 h-2 bg-black rounded-full"></div></div>
                                </div>
                                <span class="text-white text-xs font-semibold">TikTok</span>
                            </div>
                            <!-- Avatar 3 -->
                            <div class="flex flex-col items-center gap-3 group cursor-pointer min-w-[75px]">
                                <div class="relative">
                                    <div class="w-16 h-16 rounded-full bg-red-600 p-[2px] shadow-lg group-hover:scale-110 transition-transform duration-300"><div class="w-full h-full bg-white rounded-full flex items-center justify-center overflow-hidden"><svg width="28" height="28" viewBox="0 0 24 24" fill="red"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-1.96C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 1.96C1 8.18 1 12 1 12s0 3.82.46 5.58a2.78 2.78 0 0 0 1.94 1.96c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-1.96c.46-1.76.46-5.58.46-5.58s0-3.82-.46-5.58zM9.54 15.19V8.81l6.15 3.19-6.15 3.19z"/></svg></div></div>
                                    <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-4 h-4 bg-white rounded-full flex items-center justify-center border-2 border-[#4a0bb3]"><div class="w-2 h-2 bg-[#ff9900] rounded-full"></div></div>
                                </div>
                                <span class="text-white text-xs font-semibold">YouTube</span>
                            </div>
                            <!-- Avatar 4 -->
                            <div class="flex flex-col items-center gap-3 group cursor-pointer min-w-[75px]">
                                <div class="relative">
                                    <div class="w-16 h-16 rounded-full bg-blue-400 p-[2px] shadow-lg group-hover:scale-110 transition-transform duration-300"><div class="w-full h-full bg-white rounded-full flex items-center justify-center overflow-hidden"><svg width="24" height="24" viewBox="0 0 24 24" fill="#0088cc"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg></div></div>
                                    <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-4 h-4 bg-white rounded-full flex items-center justify-center border-2 border-[#4a0bb3]"><div class="w-2 h-2 bg-black rounded-full"></div></div>
                                </div>
                                <span class="text-white text-xs font-semibold">Telegram</span>
                            </div>
                            
                            <!-- Add Button -->
                            <div class="flex flex-col items-center gap-3 group cursor-pointer min-w-[75px]">
                                <div class="w-16 h-16 rounded-full bg-white/10 border-2 border-dashed border-white/40 flex items-center justify-center shadow-lg group-hover:bg-white group-hover:text-[#4a0bb3] transition-colors text-white">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                                </div>
                                <span class="text-transparent select-none text-xs">Add</span>
                            </div>
                        </div>
                    </div>

                    <!-- Popular Services -->
                    <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl">
                        <div class="flex justify-between items-center mb-6">
                            <h3 class="text-white font-semibold text-lg tracking-tight">Trending Services</h3>
                            <div class="flex gap-2">
                                <button class="w-7 h-7 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/30 text-white/60 hover:text-white transition shadow-sm"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg></button>
                                <button class="w-7 h-7 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/30 text-white/60 hover:text-white transition shadow-sm"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></button>
                            </div>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                            <!-- Card 1 -->
                            <div class="bg-white/10 border border-white/20 rounded-2xl p-5 flex flex-col hover:bg-white/20 transition cursor-pointer relative overflow-hidden">
                                <div class="absolute -right-4 -bottom-4 opacity-20"><svg width="60" height="60" viewBox="0 0 24 24" fill="white"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></div>
                                <span class="bg-white text-[#4a0bb3] text-[10px] font-bold px-3 py-1 rounded-full self-start mb-6 shadow-sm">Instagram</span>
                                <h4 class="text-white text-sm font-bold mt-auto relative z-10 leading-snug">High Quality<br>Likes</h4>
                            </div>
                            <!-- Card 2 -->
                            <div class="bg-gradient-to-br from-[#4a0bb3]/60 to-[#7b27e8]/60 border border-white/30 rounded-2xl p-5 flex flex-col hover:from-[#4a0bb3]/80 hover:to-[#7b27e8]/80 transition cursor-pointer relative overflow-hidden shadow-md">
                                <div class="absolute -right-4 -bottom-4 opacity-20"><svg width="60" height="60" viewBox="0 0 24 24" fill="white"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></div>
                                <span class="bg-white text-[#111] text-[10px] font-bold px-3 py-1 rounded-full self-start mb-6 shadow-sm">TikTok</span>
                                <h4 class="text-white text-sm font-bold mt-auto relative z-10 leading-snug">Viral Views<br>Package</h4>
                            </div>
                            <!-- Card 3 -->
                            <div class="bg-white/10 border border-white/20 rounded-2xl p-5 flex flex-col hover:bg-white/20 transition cursor-pointer relative overflow-hidden">
                                <div class="absolute -right-4 -bottom-4 opacity-20"><svg width="60" height="60" viewBox="0 0 24 24" fill="white"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></div>
                                <span class="bg-white text-[#4a0bb3] text-[10px] font-bold px-3 py-1 rounded-full self-start mb-6 shadow-sm">YouTube</span>
                                <h4 class="text-white text-sm font-bold mt-auto relative z-10 leading-snug">Subscriber<br>Boost</h4>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column (Sidebar) -->
                <div class="lg:col-span-4 flex flex-col gap-6">
                    
                    <!-- Search & Header -->
                    <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-full py-3 px-5 flex items-center justify-between shadow-lg">
                        <div class="flex items-center gap-3 text-white/60 w-full">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                            <input type="text" placeholder="Search..." class="bg-transparent border-none outline-none text-white text-sm w-full placeholder-white/50 font-medium">
                        </div>
                        <div class="flex items-center gap-4 pl-4 border-l border-white/20">
                            <div class="w-2.5 h-2.5 rounded-full bg-white shadow-sm cursor-pointer hover:scale-125 transition-transform"></div>
                            <div class="relative cursor-pointer hover:scale-110 transition-transform">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
                                <div class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-[#4a0bb3]"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Promo Banner -->
                    <div class="bg-gradient-to-tr from-blue-600 to-[#7b27e8] rounded-3xl p-6 shadow-xl relative overflow-hidden flex flex-col justify-center items-start min-h-[140px] group cursor-pointer">
                        <div class="absolute -right-4 -bottom-4 opacity-40 group-hover:scale-110 group-hover:rotate-6 transition-transform duration-500">
                            <!-- Abstract shapes mimicking the reference -->
                            <svg width="120" height="120" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                                <path fill="#FFFFFF" d="M45.7,-76.3C58.9,-69.3,68.8,-55.1,76.5,-40.4C84.2,-25.7,89.7,-10.5,88.2,3.9C86.7,18.3,78.2,31.9,67.8,43.2C57.4,54.5,45.1,63.5,31.3,71.1C17.5,78.7,2.2,84.9,-12.3,83.8C-26.8,82.7,-40.5,74.3,-52.3,64.2C-64.1,54.1,-74,42.3,-79.8,28.7C-85.6,15.1,-87.3,-0.3,-83.4,-14C-79.5,-27.7,-70,-39.7,-58.5,-48.9C-47,-58.1,-33.5,-64.5,-20.1,-69.3C-6.7,-74.1,6.6,-77.3,21.1,-78.9C35.6,-80.5,45.7,-76.3,45.7,-76.3Z" transform="translate(100 100) scale(1.1)" />
                            </svg>
                        </div>
                        <h3 class="text-white font-bold text-[17px] mb-4 relative z-10 leading-tight">Supercharge your<br>Social Media!</h3>
                        <button class="bg-[#111] text-white font-bold text-[11px] px-5 py-2.5 rounded-full relative z-10 shadow-lg group-hover:bg-white group-hover:text-[#111] transition-colors">Deposit Funds</button>
                    </div>

                    <!-- Progress / Stats Card -->
                    <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl flex items-center justify-between">
                        <div>
                            <h4 class="text-white font-bold text-[15px] mb-1">Reseller Tier</h4>
                            <p class="text-white/60 text-[10px] font-medium mb-3">Start date: 04/05/2024</p>
                            <p class="text-white text-xs font-semibold">Tutor: <span class="font-normal text-white/80">Ethioviral Pro</span></p>
                        </div>
                        <div class="relative w-16 h-16 flex items-center justify-center">
                            <!-- Circular Progress SVG -->
                            <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                                <path class="text-white/20" stroke-width="4" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                                <path class="text-[#4a0bb3]" stroke-dasharray="64, 100" stroke-width="4" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                            </svg>
                            <span class="absolute text-white font-bold text-xs">64%</span>
                        </div>
                    </div>

                    <!-- Recent Orders List -->
                    <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl flex-1 flex flex-col">
                        <div class="flex justify-between items-center mb-6">
                            <h3 class="text-white font-semibold text-lg tracking-tight">Recent orders</h3>
                            <span class="text-white/80 text-[11px] font-bold cursor-pointer hover:text-white transition flex items-center gap-1">All platforms <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
                        </div>
                        
                        <div class="flex flex-col gap-5">
                            <!-- List Item 1 -->
                            <div class="flex items-center gap-4 group cursor-pointer border-b border-white/10 pb-4">
                                <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center shadow-sm group-hover:bg-white/30 transition text-[18px]">📸</div>
                                <div class="flex-1">
                                    <h4 class="text-white text-[13px] font-bold mb-1">Instagram Followers</h4>
                                    <p class="text-white/60 text-[10px] font-medium">10K quantity  5K processing</p>
                                </div>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                            </div>
                            
                            <!-- List Item 2 -->
                            <div class="flex items-center gap-4 group cursor-pointer border-b border-white/10 pb-4">
                                <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center shadow-sm group-hover:bg-white/30 transition text-[18px]">🎵</div>
                                <div class="flex-1">
                                    <h4 class="text-white text-[13px] font-bold mb-1">TikTok Views is easy!</h4>
                                    <p class="text-white/60 text-[10px] font-medium">8K quantity  4K processing</p>
                                </div>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                            </div>

                            <!-- List Item 3 -->
                            <div class="flex items-center gap-4 group cursor-pointer border-b border-white/10 pb-4">
                                <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center shadow-sm group-hover:bg-white/30 transition text-[18px]">🌍</div>
                                <div class="flex-1">
                                    <h4 class="text-white text-[13px] font-bold mb-1">Global Targeting</h4>
                                    <p class="text-white/60 text-[10px] font-medium">8 geo  4 regions</p>
                                </div>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                            </div>

                            <!-- List Item 4 -->
                            <div class="flex items-center gap-4 group cursor-pointer">
                                <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center shadow-sm group-hover:bg-white/30 transition text-[18px]">📝</div>
                                <div class="flex-1">
                                    <h4 class="text-white text-[13px] font-bold mb-1">Custom Comments</h4>
                                    <p class="text-white/60 text-[10px] font-medium">24 lines  16 practical</p>
                                </div>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </section>
    \n"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(prefix + new_section + suffix)
        
    print("Section successfully updated to Bento Grid Dashboard!")
else:
    print("Failed to find start or end markers.")
