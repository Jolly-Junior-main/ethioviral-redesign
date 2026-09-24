import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the section containing "SMM, WITHOUT THE GUESSING" up to the start of "Check the recipient before and after delivery"
pattern = re.compile(r'<section class="bg-white/20 backdrop-blur-xl border border-white/30 shadow-\[0_8px_32px_0_rgba\(31,38,135,0\.1\)\] py-24 px-6 lg:px-12 border-t border-white/20">\s*<div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-\[1fr_2fr\] gap-16 items-start">.*?<!-- SECTION: Check the recipient before and after delivery \(Screenshot 2\) -->', re.DOTALL)

new_section = """<section class="bg-transparent py-24 px-6 lg:px-12 border-t border-white/10">
          <div class="max-w-7xl mx-auto flex flex-col items-center text-center mb-16">
              <div class="text-white/80 font-bold text-[10px] tracking-widest uppercase mb-3">SMM, WITHOUT THE GUESSING</div>
              <h2 class="text-4xl md:text-5xl font-extrabold text-white mb-6 leading-tight tracking-tight">The service tells you exactly what it needs.</h2>
              <p class="text-white/70 text-sm leading-relaxed max-w-2xl mx-auto">
                  Browse by platform, read the service notes, submit only the public target requested, and keep the order details in one place.
              </p>
          </div>

          <!-- The Dashboard -->
          <div class="max-w-7xl mx-auto bg-white/10 backdrop-blur-2xl border border-white/20 rounded-[2rem] shadow-2xl overflow-hidden flex flex-col lg:flex-row">
              
              <!-- Left Side (Main) -->
              <div class="flex-1 p-8 lg:p-10 flex flex-col gap-8">
                  
                  <!-- Top Header -->
                  <div class="flex justify-between items-center">
                      <div class="flex items-center gap-4">
                          <div class="w-12 h-12 bg-blue-600 rounded-2xl flex items-center justify-center shadow-lg">
                              <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M12 2L2 22h20L12 2zm0 6l5 10H7l5-10z"/></svg>
                          </div>
                          <div>
                              <h3 class="text-white font-bold text-xl">Welcome, Reseller</h3>
                              <p class="text-white/60 text-[11px] font-medium">Your personal SMM dashboard overview</p>
                          </div>
                      </div>
                      <div class="flex items-center gap-4 hidden sm:flex">
                          <div class="bg-white/5 border border-white/10 rounded-full px-4 py-2.5 flex items-center gap-2">
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-white/50" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                              <input type="text" placeholder="Search orders..." class="bg-transparent text-white text-[11px] outline-none w-32 placeholder-white/40">
                          </div>
                          <div class="w-10 h-10 bg-white/10 rounded-full border border-white/20 flex items-center justify-center cursor-pointer hover:bg-white/20 transition">
                              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                          </div>
                      </div>
                  </div>

                  <!-- Middle Row: Cards -->
                  <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                      <!-- Profile/Tier Card -->
                      <div class="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col items-center justify-center relative shadow-lg">
                          <div class="absolute top-4 left-4 text-white/60 text-xs font-bold">Profile</div>
                          <div class="absolute top-4 right-4">
                              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-white/60" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
                          </div>
                          
                          <div class="relative w-24 h-24 mt-4 mb-4">
                              <!-- Circular Progress Segment -->
                              <svg class="absolute inset-0 w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                                  <path class="text-white/10" stroke-width="2" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                                  <path class="text-pink-500" stroke-dasharray="70, 100" stroke-width="2" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                              </svg>
                              <!-- Avatar -->
                              <div class="absolute inset-1 rounded-full bg-[#111] overflow-hidden border-2 border-[#4a0bb3]">
                                  <img src="https://ui-avatars.com/api/?name=Reseller&background=random" class="w-full h-full object-cover opacity-80" alt="Avatar">
                              </div>
                              <div class="absolute bottom-0 right-1 w-6 h-6 bg-[#111] border-2 border-white rounded-full flex items-center justify-center">
                                  <svg width="10" height="10" viewBox="0 0 24 24" fill="white"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                              </div>
                          </div>
                          
                          <h4 class="text-white font-bold text-[15px]">Pro Reseller</h4>
                          <p class="text-white/50 text-[10px] font-medium mb-6">Tier 2 Member</p>
                          
                          <!-- Stats -->
                          <div class="flex gap-4 w-full justify-center">
                              <div class="bg-white/10 rounded-full px-3 py-1 flex items-center gap-1.5 shadow-sm">
                                  <span class="text-orange-400 text-[10px]">👥</span>
                                  <span class="text-white font-bold text-[11px]">2.4k</span>
                              </div>
                              <div class="bg-white/10 rounded-full px-3 py-1 flex items-center gap-1.5 shadow-sm">
                                  <span class="text-blue-400 text-[10px]">📦</span>
                                  <span class="text-white font-bold text-[11px]">892</span>
                              </div>
                          </div>
                      </div>

                      <!-- Gradient Cards Container -->
                      <div class="md:col-span-2 flex flex-col gap-4">
                          <div class="flex gap-4 flex-1">
                              <!-- Completed Orders Card -->
                              <div class="flex-1 rounded-3xl p-6 relative overflow-hidden shadow-lg border border-white/20" style="background: radial-gradient(circle at top right, #F97316 0%, transparent 70%), radial-gradient(circle at bottom left, #ec4899 0%, rgba(255,255,255,0.1) 100%);">
                                  <div class="flex justify-between items-start mb-10 relative z-10">
                                      <h4 class="text-[#111] font-bold text-sm leading-tight max-w-[80px]">Completed<br>Orders</h4>
                                      <div class="w-8 h-8 rounded-full border border-[#111]/20 flex items-center justify-center">
                                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                                      </div>
                                  </div>
                                  <div class="relative z-10">
                                      <h2 class="text-[#111] text-4xl font-extrabold tracking-tight mb-1">83%</h2>
                                      <p class="text-[#111]/70 text-[10px] font-bold uppercase tracking-wider">Avg. Success</p>
                                  </div>
                              </div>

                              <!-- Processing Card -->
                              <div class="flex-1 rounded-3xl p-6 relative overflow-hidden shadow-lg border border-white/20" style="background: radial-gradient(circle at top left, #3b82f6 0%, transparent 70%), radial-gradient(circle at bottom right, #06b6d4 0%, rgba(255,255,255,0.1) 100%);">
                                  <div class="flex justify-between items-start mb-10 relative z-10">
                                      <h4 class="text-[#111] font-bold text-sm leading-tight max-w-[80px]">Processing<br>Tasks</h4>
                                      <div class="w-8 h-8 rounded-full border border-[#111]/20 flex items-center justify-center">
                                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                                      </div>
                                  </div>
                                  <div class="relative z-10">
                                      <h2 class="text-[#111] text-4xl font-extrabold tracking-tight mb-1">56%</h2>
                                      <p class="text-[#111]/70 text-[10px] font-bold uppercase tracking-wider">In Progress</p>
                                  </div>
                              </div>
                          </div>
                          
                          <!-- Connected Platforms Pill -->
                          <div class="bg-white/5 border border-white/10 rounded-2xl p-4 flex items-center justify-between shadow-sm">
                              <div>
                                  <h5 class="text-white font-bold text-sm">Platforms connected</h5>
                                  <p class="text-white/50 text-[10px] font-medium">3 active APIs</p>
                              </div>
                              <div class="flex items-center gap-2">
                                  <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center text-[14px]">📸</div>
                                  <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center text-[14px]">🎵</div>
                                  <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center text-[14px]">▶️</div>
                                  <div class="w-8 h-8 rounded-full border border-white/20 flex items-center justify-center text-white/50 text-[10px] cursor-pointer hover:bg-white/10">...</div>
                              </div>
                          </div>
                      </div>
                  </div>

                  <!-- Bottom Row: Chart -->
                  <div class="mt-4">
                      <div class="flex justify-between items-end mb-6">
                          <div>
                              <h3 class="text-white font-bold text-lg">Growth Analytics</h3>
                              <p class="text-white/50 text-[11px]">Followers & Engagement trends</p>
                          </div>
                          <div class="bg-white/5 border border-white/10 px-3 py-1.5 rounded-md text-white text-[10px] font-bold flex items-center gap-2 cursor-pointer">
                              Range: Last month <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                          </div>
                      </div>
                      
                      <div class="relative w-full h-[180px] mt-8">
                          <!-- Chart Y-axis labels -->
                          <div class="absolute left-0 top-0 bottom-8 flex flex-col justify-between text-white/30 text-[9px] font-bold">
                              <span>↑</span>
                              <span>Aug</span>
                              <span class="bg-blue-600 text-white px-2 py-0.5 rounded-full">Sep</span>
                              <span>Oct</span>
                              <span>Nov</span>
                              <span>↓</span>
                          </div>
                          
                          <!-- SVG Chart Lines -->
                          <div class="absolute left-12 right-4 top-0 bottom-8 border-b border-white/10">
                              <!-- Abstract Grid dotted -->
                              <div class="absolute inset-0" style="background-image: radial-gradient(rgba(255,255,255,0.15) 1px, transparent 1px); background-size: 20px 20px;"></div>
                              
                              <svg class="w-full h-full overflow-visible" preserveAspectRatio="none" viewBox="0 0 1000 200">
                                  <!-- Red Line -->
                                  <path d="M0,150 C100,150 150,130 250,140 C350,150 400,20 500,40 C600,60 650,180 750,160 C850,140 900,100 1000,150" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
                                  
                                  <!-- Blue Line -->
                                  <path d="M0,180 C100,180 150,150 250,160 C350,170 400,90 500,100 C600,110 650,40 750,60 C850,80 900,140 1000,120" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
                                  
                                  <!-- Tooltip Point -->
                                  <circle cx="500" cy="100" r="6" fill="#111" stroke="#3b82f6" stroke-width="3"/>
                              </svg>
                              
                              <!-- Tooltip Box -->
                              <div class="absolute top-[30px] left-[45%] transform -translate-x-1/2 -translate-y-full bg-white text-[#111] px-4 py-2 rounded-2xl shadow-xl text-center before:content-[''] before:absolute before:bottom-[-6px] before:left-1/2 before:-translate-x-1/2 before:border-4 before:border-transparent before:border-t-white">
                                  <div class="font-bold text-[11px]">Week 8</div>
                                  <div class="text-[#111]/60 text-[9px]">Peak Engagement</div>
                              </div>
                          </div>
                          
                          <!-- Chart Legend -->
                          <div class="absolute bottom-0 left-12 flex gap-6">
                              <div class="flex items-center gap-2">
                                  <div class="w-2.5 h-2.5 rounded-sm bg-red-500"></div>
                                  <span class="text-white/60 text-[10px]">Followers gained</span>
                              </div>
                              <div class="flex items-center gap-2">
                                  <div class="w-2.5 h-2.5 rounded-sm bg-blue-500"></div>
                                  <span class="text-white/60 text-[10px]">Engagement rate</span>
                              </div>
                          </div>
                          
                          <!-- Big Stat Bottom Right -->
                          <div class="absolute bottom-0 right-4 text-right">
                              <div class="text-white text-3xl font-extrabold tracking-tight">41%</div>
                              <div class="text-white/50 text-[9px] uppercase font-bold tracking-wider">Avg. Growth</div>
                          </div>
                      </div>
                  </div>
              </div>

              <!-- Right Side (Sidebar) -->
              <div class="w-full lg:w-[35%] bg-white/5 border-l border-white/10 p-8 lg:p-10 flex flex-col gap-10">
                  
                  <!-- Recent Orders List -->
                  <div>
                      <div class="flex justify-between items-center mb-6">
                          <h3 class="text-white font-bold text-lg">Recent orders</h3>
                          <div class="w-8 h-8 rounded-full border border-white/20 flex items-center justify-center cursor-pointer hover:bg-white/10 text-white">
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                          </div>
                      </div>
                      
                      <div class="flex flex-col gap-0">
                          <!-- Order 1 -->
                          <div class="flex justify-between items-center py-4 border-b border-white/10 group cursor-pointer hover:bg-white/5 px-2 -mx-2 rounded-lg transition">
                              <div class="w-20 shrink-0">
                                  <p class="text-white/50 text-[10px] font-bold">Tue, 11 Jul</p>
                                  <p class="text-white font-bold text-[11px]">08:15 am</p>
                              </div>
                              <div class="flex-1 px-4">
                                  <h4 class="text-white font-bold text-[13px] mb-1">1k Instagram Followers</h4>
                                  <div class="flex items-center gap-1.5 text-white/60 text-[10px]">
                                      <span class="w-2 h-2 rounded-full bg-pink-500"></span> IG Premium
                                  </div>
                              </div>
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" class="opacity-30 group-hover:opacity-100 transition"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                          </div>
                          <!-- Order 2 -->
                          <div class="flex justify-between items-center py-4 border-b border-white/10 group cursor-pointer hover:bg-white/5 px-2 -mx-2 rounded-lg transition">
                              <div class="w-20 shrink-0">
                                  <p class="text-white/50 text-[10px] font-bold">Tue, 11 Jul</p>
                                  <p class="text-white font-bold text-[11px]">09:30 pm</p>
                              </div>
                              <div class="flex-1 px-4">
                                  <h4 class="text-white font-bold text-[13px] mb-1">10k TikTok Views</h4>
                                  <div class="flex items-center gap-1.5 text-white/60 text-[10px]">
                                      <span class="w-2 h-2 rounded-full bg-[#111] border border-white/30"></span> TikTok Fast
                                  </div>
                              </div>
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" class="opacity-30 group-hover:opacity-100 transition"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                          </div>
                          <!-- Order 3 -->
                          <div class="flex justify-between items-center py-4 border-b border-white/10 group cursor-pointer hover:bg-white/5 px-2 -mx-2 rounded-lg transition">
                              <div class="w-20 shrink-0">
                                  <p class="text-white/50 text-[10px] font-bold">Tue, 12 Jul</p>
                                  <p class="text-white font-bold text-[11px]">02:30 pm</p>
                              </div>
                              <div class="flex-1 px-4">
                                  <h4 class="text-white font-bold text-[13px] mb-1">YouTube Monetization</h4>
                                  <div class="flex items-center gap-1.5 text-white/60 text-[10px]">
                                      <span class="w-2 h-2 rounded-full bg-red-600"></span> YT Watchtime
                                  </div>
                              </div>
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" class="opacity-30 group-hover:opacity-100 transition"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                          </div>
                      </div>
                      <div class="text-center mt-6">
                          <a href="#" class="text-white/70 text-[11px] font-bold hover:text-white transition flex items-center justify-center gap-1">
                              See all orders <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                          </a>
                      </div>
                  </div>

                  <!-- Platform Distribution -->
                  <div class="flex-1">
                      <div class="mb-6">
                          <h3 class="text-white font-bold text-lg">Top Services</h3>
                          <p class="text-white/50 text-[11px]">Most ordered platforms</p>
                      </div>
                      
                      <div class="flex flex-col gap-5">
                          <!-- Bar 1 -->
                          <div class="flex items-center gap-4">
                              <span class="text-white font-bold text-xs w-24">Instagram</span>
                              <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                                  <div class="h-full bg-blue-500 rounded-full" style="width: 71%"></div>
                              </div>
                              <span class="text-white/60 text-[10px] font-bold w-6">71%</span>
                          </div>
                          <!-- Bar 2 -->
                          <div class="flex items-center gap-4">
                              <span class="text-white font-bold text-xs w-24">TikTok</span>
                              <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                                  <div class="h-full bg-blue-500 rounded-full" style="width: 92%"></div>
                              </div>
                              <span class="text-white/60 text-[10px] font-bold w-6">92%</span>
                          </div>
                          <!-- Bar 3 -->
                          <div class="flex items-center gap-4">
                              <span class="text-white font-bold text-xs w-24">YouTube</span>
                              <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                                  <div class="h-full bg-blue-500 rounded-full" style="width: 33%"></div>
                              </div>
                              <span class="text-white/60 text-[10px] font-bold w-6">33%</span>
                          </div>
                          <!-- Bar 4 -->
                          <div class="flex items-center gap-4">
                              <span class="text-white font-bold text-xs w-24">Telegram</span>
                              <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                                  <div class="h-full bg-blue-500 rounded-full" style="width: 56%"></div>
                              </div>
                              <span class="text-white/60 text-[10px] font-bold w-6">56%</span>
                          </div>
                          <!-- Bar 5 -->
                          <div class="flex items-center gap-4">
                              <span class="text-white font-bold text-xs w-24">Twitter / X</span>
                              <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                                  <div class="h-full bg-blue-500 rounded-full" style="width: 79%"></div>
                              </div>
                              <span class="text-white/60 text-[10px] font-bold w-6">79%</span>
                          </div>
                      </div>
                  </div>

              </div>
          </div>
      </section>
<!-- SECTION: Check the recipient before and after delivery (Screenshot 2) -->"""

match = pattern.search(html)
if match:
    old_section_text = match.group(0)
    html = html.replace(old_section_text, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success: Replaced SMM Guessing section with new bento grid layout")
else:
    print("Could not find the section to replace.")
