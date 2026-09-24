import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<section class="bg-transparent py-24 px-6 lg:px-12">'
end_marker = '<!-- SECTION: Every important step stays visible (Screenshot 2) -->'

# Since there are multiple `<section class="bg-transparent py-24 px-6 lg:px-12">`,
# let's find the one that has "EXPERIENCE THE PLATFORM" right after it.
# We'll split the file based on "EXPERIENCE THE PLATFORM" to accurately locate the exact block.
# Actually, the start of the block is `<section class="bg-transparent py-24 px-6 lg:px-12">\n        <div class="max-w-7xl mx-auto flex flex-col items-center text-center mb-16">\n            <div class="text-blue-600 font-bold text-[10px] tracking-widest uppercase mb-3">EXPERIENCE THE PLATFORM</div>`

# We can use regex to replace everything from that section start to the end_marker.
pattern = re.compile(r'<section class="bg-transparent py-24 px-6 lg:px-12">\s*<div class="max-w-7xl mx-auto flex flex-col items-center text-center mb-16">\s*<div class="text-blue-600 font-bold text-\[10px\] tracking-widest uppercase mb-3">EXPERIENCE THE PLATFORM</div>.*?<!-- SECTION: Every important step stays visible \(Screenshot 2\) -->', re.DOTALL)

new_section = """<section class="bg-transparent py-24 px-6 lg:px-12">
        <div class="max-w-7xl mx-auto flex flex-col items-center text-center mb-16">
            <div class="text-white/80 font-bold text-[10px] tracking-widest uppercase mb-3">EXPERIENCE THE PLATFORM</div>
            <h2 class="text-3xl md:text-5xl font-bold mb-4 text-white tracking-tight">See Ethioviral in Action</h2>
            <p class="text-white/70 text-sm max-w-2xl mx-auto">Watch how simple it is to boost your social media accounts and manage your campaigns.</p>
        </div>

        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-6">
            
            <!-- Left Column -->
            <div class="lg:col-span-4 flex flex-col gap-6">
                
                <!-- Blue Banner Card -->
                <div class="bg-gradient-to-br from-blue-600 to-[#4a0bb3] rounded-3xl p-6 relative overflow-hidden shadow-xl">
                    <!-- Abstract Waves -->
                    <svg class="absolute right-0 top-0 h-full w-full opacity-20 pointer-events-none" viewBox="0 0 100 100" preserveAspectRatio="none">
                        <path d="M0,50 Q25,25 50,50 T100,50 L100,100 L0,100 Z" fill="none" stroke="white" stroke-width="0.5"/>
                        <path d="M0,60 Q25,35 50,60 T100,60 L100,100 L0,100 Z" fill="none" stroke="white" stroke-width="0.5"/>
                        <path d="M0,70 Q25,45 50,70 T100,70 L100,100 L0,100 Z" fill="none" stroke="white" stroke-width="0.5"/>
                    </svg>
                    <h3 class="text-white font-bold text-lg mb-4 relative z-10 tracking-tight">Module 1. Start Campaign</h3>
                    <button class="bg-[#111] text-white font-semibold text-xs px-5 py-2.5 rounded-full relative z-10 hover:bg-white hover:text-[#111] transition shadow-md">New Order</button>
                </div>

                <!-- Circular Progress Card -->
                <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl flex items-center justify-between">
                    <div>
                        <h4 class="text-white font-bold text-[15px] mb-1">Success Rate</h4>
                        <p class="text-white/60 text-[10px] font-medium mb-1">Start date: 01/02/2024</p>
                        <p class="text-white text-xs font-semibold">Tier: <span class="font-normal text-white/80">Ethioviral Pro</span></p>
                    </div>
                    <div class="relative w-16 h-16 flex items-center justify-center">
                        <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                            <path class="text-white/20" stroke-width="4" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                            <path class="text-blue-500" stroke-dasharray="84, 100" stroke-width="4" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                        </svg>
                        <span class="absolute text-white font-bold text-xs">84%</span>
                    </div>
                </div>

                <!-- Vertical List Card -->
                <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl flex-1 flex flex-col">
                    <h3 class="text-white font-semibold text-lg mb-6 tracking-tight">My platforms</h3>
                    <div class="flex flex-col gap-4 flex-1">
                        <!-- Item 1 -->
                        <div class="flex items-center gap-4 group cursor-pointer border-b border-white/10 pb-4">
                            <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-[18px]">📸</div>
                            <div class="flex-1">
                                <h4 class="text-white text-[13px] font-bold">Instagram</h4>
                                <p class="text-white/60 text-[10px] font-medium">12 active • 8 processing</p>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </div>
                        <!-- Item 2 -->
                        <div class="flex items-center gap-4 group cursor-pointer border-b border-white/10 pb-4">
                            <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-[18px]">🎵</div>
                            <div class="flex-1">
                                <h4 class="text-white text-[13px] font-bold">TikTok</h4>
                                <p class="text-white/60 text-[10px] font-medium">4 active • 3 processing</p>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </div>
                        <!-- Item 3 -->
                        <div class="flex items-center gap-4 group cursor-pointer border-b border-white/10 pb-4">
                            <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-[18px]">🦠</div>
                            <div class="flex-1">
                                <h4 class="text-white text-[13px] font-bold">Viral Trends</h4>
                                <p class="text-white/60 text-[10px] font-medium">5 active • 3 processing</p>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </div>
                        <!-- Item 4 -->
                        <div class="flex items-center gap-4 group cursor-pointer">
                            <div class="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-[18px]">▶️</div>
                            <div class="flex-1">
                                <h4 class="text-white text-[13px] font-bold">YouTube</h4>
                                <p class="text-white/60 text-[10px] font-medium">3 active • 2 processing</p>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" class="text-white/30 group-hover:text-white transition"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </div>
                    </div>
                    <button class="w-full bg-[#111] text-white font-semibold text-xs py-3.5 rounded-full mt-6 hover:bg-white hover:text-[#111] transition shadow-lg flex items-center justify-center gap-2">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                        Add new platform
                    </button>
                </div>

            </div>

            <!-- Right Column -->
            <div class="lg:col-span-8 flex flex-col gap-6">
                
                <!-- Main Graphic Card -->
                <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl relative overflow-hidden flex-1 min-h-[420px]">
                    <div class="flex justify-between items-start mb-6">
                        <h3 class="text-white font-semibold text-lg tracking-tight">Network structure</h3>
                        <div class="bg-white text-black font-bold text-[11px] px-3 py-1.5 rounded-full border border-white/20 flex items-center gap-2 cursor-pointer hover:bg-gray-100 transition shadow-sm">
                            Global <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                    </div>

                    <!-- Abstract Grid Background -->
                    <div class="absolute inset-0 top-20 flex items-center justify-center pointer-events-none opacity-10" style="background-image: linear-gradient(rgba(255,255,255,0.2) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.2) 1px, transparent 1px); background-size: 50px 50px;"></div>

                    <!-- CSS Glowing Node (Replacing the 3D Heart) -->
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="relative w-56 h-56 mt-8">
                            <!-- Core -->
                            <div class="absolute inset-0 rounded-full bg-gradient-to-tr from-blue-500 to-[#7b27e8] opacity-60 blur-3xl animate-pulse"></div>
                            <div class="absolute inset-8 rounded-full bg-gradient-to-tr from-[#4a0bb3] to-[#8023e3] shadow-[0_0_60px_rgba(123,39,232,0.8)] border-2 border-white/40 flex items-center justify-center z-10">
                                <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path></svg>
                            </div>

                            <!-- Hotspots / Tooltips -->
                            <div class="absolute top-0 right-4 w-6 h-6 bg-blue-500 text-white text-[10px] font-bold rounded-full flex items-center justify-center border-2 border-white shadow-lg cursor-pointer hover:scale-110 transition z-20">1</div>
                            <div class="absolute top-1/4 -left-4 w-6 h-6 bg-white text-[#4a0bb3] text-[10px] font-bold rounded-full flex items-center justify-center border border-gray-200 shadow-lg cursor-pointer hover:scale-110 transition z-20">2</div>
                            <div class="absolute bottom-4 right-0 w-6 h-6 bg-white text-[#4a0bb3] text-[10px] font-bold rounded-full flex items-center justify-center border border-gray-200 shadow-lg cursor-pointer hover:scale-110 transition z-20">3</div>
                            <div class="absolute bottom-8 -left-6 w-6 h-6 bg-white text-[#4a0bb3] text-[10px] font-bold rounded-full flex items-center justify-center border border-gray-200 shadow-lg cursor-pointer hover:scale-110 transition z-20">4</div>
                            <div class="absolute -bottom-4 left-1/2 w-6 h-6 bg-white text-[#4a0bb3] text-[10px] font-bold rounded-full flex items-center justify-center border border-gray-200 shadow-lg cursor-pointer hover:scale-110 transition z-20">5</div>
                            <div class="absolute bottom-1/4 right-8 w-6 h-6 bg-white text-[#4a0bb3] text-[10px] font-bold rounded-full flex items-center justify-center border border-gray-200 shadow-lg cursor-pointer hover:scale-110 transition z-20">6</div>
                        </div>
                    </div>

                    <!-- Tooltip Card Details (Like "1 Arteries" in the image) -->
                    <div class="absolute top-24 right-8 bg-white/95 backdrop-blur-md rounded-2xl p-5 shadow-2xl max-w-[220px] border border-white/50 z-30">
                        <div class="flex items-center gap-2 mb-3">
                            <div class="w-5 h-5 bg-blue-500 text-white text-[9px] font-bold rounded-full flex items-center justify-center shadow-sm shrink-0">1</div>
                            <h5 class="text-black font-bold text-[13px] leading-tight">Instant Delivery</h5>
                        </div>
                        <p class="text-gray-700 text-[11px] leading-relaxed font-medium">
                            Orders are dispatched instantly to our high-speed global nodes. The exception is manual verification tasks, which go to our dedicated teams.
                        </p>
                    </div>

                    <!-- Zoom Controls -->
                    <div class="absolute bottom-6 right-6 flex items-center gap-2 z-30">
                        <button class="w-8 h-8 bg-white rounded-full flex items-center justify-center text-black font-bold text-lg hover:bg-gray-100 transition shadow-lg">-</button>
                        <button class="w-8 h-8 bg-white rounded-full flex items-center justify-center text-black font-bold text-lg hover:bg-gray-100 transition shadow-lg">+</button>
                        <div class="h-8 px-4 bg-white rounded-full flex items-center justify-center text-black font-bold text-[11px] shadow-lg">100%</div>
                    </div>
                </div>

                <!-- Bottom Timeline Card -->
                <div class="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-6 shadow-xl flex flex-col md:flex-row gap-8 min-h-[220px]">
                    
                    <!-- Date Picker (Left) -->
                    <div class="w-full md:w-1/3 flex flex-col">
                        <div class="flex justify-between items-center mb-8">
                            <h3 class="text-white font-semibold text-lg tracking-tight">May 2024</h3>
                            <button class="bg-white/10 text-white text-[11px] font-bold px-4 py-1.5 rounded-full border border-white/30 hover:bg-white/20 transition shadow-sm">Calendar</button>
                        </div>
                        <div class="flex gap-3 h-[110px]">
                            <!-- Day 1 -->
                            <div class="flex-1 bg-white/5 rounded-2xl border border-white/10 flex flex-col items-center justify-center gap-1 cursor-pointer hover:bg-white/10 transition">
                                <span class="text-white/60 text-[11px] font-medium">April</span>
                                <span class="text-white text-xl font-bold">18</span>
                            </div>
                            <!-- Day 2 (Active) -->
                            <div class="flex-1 bg-[#111] rounded-2xl border-2 border-white/20 flex flex-col items-center justify-center gap-1 cursor-pointer shadow-xl relative transform scale-105">
                                <span class="text-white/70 text-[11px] font-medium">April</span>
                                <span class="text-white text-xl font-bold">19</span>
                                <div class="absolute -bottom-2 w-4 h-4 bg-blue-500 border-4 border-[#111] rounded-full"></div>
                            </div>
                            <!-- Day 3 -->
                            <div class="flex-1 bg-white/5 rounded-2xl border border-white/10 flex flex-col items-center justify-center gap-1 cursor-pointer hover:bg-white/10 transition">
                                <span class="text-white/60 text-[11px] font-medium">April</span>
                                <span class="text-white text-xl font-bold">20</span>
                            </div>
                        </div>
                    </div>

                    <!-- Timeline Gantt (Right) -->
                    <div class="w-full md:w-2/3 md:border-l md:border-white/10 md:pl-8 flex flex-col">
                        <h3 class="text-white font-semibold text-lg mb-8 tracking-tight">Productivity</h3>
                        <div class="relative w-full flex-1">
                            <!-- Time Axis -->
                            <div class="flex justify-between text-white/50 text-[10px] font-bold mb-4">
                                <span>9 AM</span><span>10 AM</span><span>11 AM</span><span>12 AM</span><span>1 PM</span><span>2 PM</span><span>3 PM</span>
                            </div>
                            <!-- Grid Lines -->
                            <div class="absolute inset-0 top-6 flex justify-between pointer-events-none opacity-10">
                                <div class="w-px h-full bg-white"></div><div class="w-px h-full bg-white"></div><div class="w-px h-full bg-white"></div><div class="w-px h-full bg-white"></div><div class="w-px h-full bg-white"></div><div class="w-px h-full bg-white"></div><div class="w-px h-full bg-white"></div>
                            </div>
                            <!-- Gantt Bars -->
                            <div class="relative h-24 mt-2">
                                <div class="absolute top-0 left-[0%] w-[35%] bg-blue-500 text-white text-[10px] font-bold px-3 py-1.5 rounded-md shadow-md overflow-hidden whitespace-nowrap">Instagram</div>
                                <div class="absolute top-8 left-[25%] w-[40%] bg-green-400 text-[#111] text-[10px] font-bold px-3 py-1.5 rounded-md shadow-md overflow-hidden whitespace-nowrap">Global Reach</div>
                                <div class="absolute top-16 left-[60%] w-[35%] bg-pink-500 text-white text-[10px] font-bold px-3 py-1.5 rounded-md shadow-md overflow-hidden whitespace-nowrap">YouTube</div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </section>
<!-- SECTION: Every important step stays visible (Screenshot 2) -->"""

match = pattern.search(html)
if match:
    old_section_text = match.group(0)
    html = html.replace(old_section_text, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success: Replaced section with new bento grid layout")
else:
    print("Could not find the section to replace.")
