import streamlit as st

# ১. পেজ সেটআপ ও ফন্ট (Shikho/DSAT লুক)
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="centered")

# ২. প্রিমিয়াম থিম ডিটেইলস (Grey + White + Purple + Orange)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');
    
    /* মূল ব্যাকগ্রাউন্ড - DSAT এর মতো হালকা গ্রে/অফ-হোয়াইট */
    html, body, [class*="css"] {
        font-family: 'Hind Siliguri', sans-serif;
        background-color: #F3F4F6 !important;
    }
    .stApp { background-color: #F3F4F6; }

    /* টপ বার (Shikho Style) */
    .top-nav {
        background: #6B46C1; padding: 15px 20px; border-radius: 0 0 25px 25px;
        display: flex; justify-content: space-between; align-items: center;
        color: white; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(107, 70, 193, 0.2);
    }
    .brand { font-size: 24px; font-weight: 700; }

    /* কন্টেন্ট কার্ড (DSAT এর মতো সাদা বক্স) */
    .dsat-card {
        background: #FFFFFF; padding: 25px; border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        border: 1px solid #E5E7EB; margin-bottom: 20px;
    }

    /* টেক্সট কালার গাইড */
    .purple-bold { color: #6B46C1; font-weight: 700; font-size: 26px; }
    .orange-text { color: #FF7A00 !important; font-weight: 700; }
    .gray-desc { color: #4B5563; line-height: 1.7; font-size: 16px; }

    /* প্রিমিয়াম অরেঞ্জ বাটন */
    div.stButton > button {
        background: #FF7A00 !important; color: white !important;
        border-radius: 12px; height: 3.5em; width: 100%;
        border: none; font-weight: 700; font-size: 18px; transition: 0.3s;
    }
    div.stButton > button:hover { transform: scale(1.02); }

    /* সাইডবার (ডান পাশের ন্যাভিগেশন কন্ট্রোল) */
    [data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 2px solid #6B46C1; }
    </style>
    """, unsafe_allow_html=True)

# ৩. টপ বার ব্র্যান্ডিং
st.markdown('<div class="top-nav"><div class="brand">ইলিশ কিনি</div><div style="font-size:24px;">☰</div></div>', unsafe_allow_html=True)

# ৪. ফাংশনাল মেনুবার
with st.sidebar:
    st.markdown("<h2 class='purple-bold'>মেনুবার</h2>", unsafe_allow_html=True)
    menu = st.radio("অপশন বেছে নিন:", ["🏠 হোম - দাম চেক", "📜 চাঁদপুরের ইতিহাস", "🧬 পুষ্টি ও উপকারিতা", "📍 লোকেশন ম্যাপ"])
    st.markdown("---")
    st.markdown("ডেভেলপার: **সাহিব**")

# ৫. মেইন কন্টেন্ট এরিয়া
if menu == "🏠 হোম - দাম চেক":
    st.markdown("<h1 style='text-align:center;' class='purple-bold'>স্বাগতম আপনাকে</h1>", unsafe_allow_html=True)
    st.markdown('<div class="dsat-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='orange-text'>বাজার দর যাচাই করুন</h3>", unsafe_allow_html=True)
    
    size = st.selectbox("মাছের সাইজ", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    # রিয়েল ডাটা
    prices = {"৫০০-৬০০ গ্রাম": 1150, "৭০০-৯০০ গ্রাম": 1250, "১ কেজি সাইজ": 1500, "১.৫ কেজি+": 1950, "২ কেজি+": 2750}
    fair_price = prices[size]
    
    st.write(f"সঠিক গড় বাজার দর: **{fair_price} ৳**")
    user_p = st.number_input("বিক্রেতা কত চাচ্ছে?", value=fair_price)
    
    if st.button("রেজাল্ট দেখুন"):
        if user_p > fair_price + 150:
            st.error(f"🚨 অতিরিক্ত {user_p - fair_price} টাকা চাচ্ছে! দরাদরি করুন।")
        else:
            st.success("✅ দাম একদম সঠিক।")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📜 চাঁদপুরের ইতিহাস":
    st.markdown('<div class="dsat-card">', unsafe_allow_html=True)
    st.markdown("<h2 class='orange-text'>ইলিশের রাজধানী চাঁদপুর</h2>", unsafe_allow_html=True)
    st.markdown("""<div class="gray-desc">
    চাঁদপুরকে কেন ইলিশের বাড়ি বলা হয়? কারণ পদ্মা, মেঘনা ও ডাকাতিয়া নদীর মিলনস্থল বা মোহনায় ইলিশের বিচরণ সবচেয়ে বেশি। সমুদ্রে থাকলেও প্রজননের জন্য ইলিশ যখন মিষ্টি জলে আসে, তখন চাঁদপুরের মোহনায় তারা বিশেষ স্বাদ ও চর্বি লাভ করে। <br><br>
    চাঁদপুর বড় স্টেশন মাছ ঘাট হলো দেশের অন্যতম প্রাচীন এবং বৃহত্তম মাছের আড়ত। এখান থেকেই সারা বাংলাদেশ এবং ভারতে ইলিশ সরবরাহ করা হয়। চাঁদপুরের ইলিশ মানেই ঐতিহ্যের স্বাদ।
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🧬 পুষ্টি ও উপকারিতা":
    st.markdown('<div class="dsat-card">', unsafe_allow_html=True)
    st.markdown("<h2 class='orange-text'>কেন ইলিশ খাবেন?</h2>", unsafe_allow_html=True)
    st.markdown("""<div class="gray-desc">
    ১. <b>হার্ট সুস্থ রাখে:</b> এতে প্রচুর ওমেগা-৩ ফ্যাটি এসিড রয়েছে যা হার্ট ব্লক প্রতিরোধ করে।<br>
    ২. <b>স্মৃতিশক্তি বাড়ায়:</b> মস্তিষ্কের কার্যক্ষমতা এবং শিশুদের মেধা বিকাশে এটি অতুলনীয়।<br>
    ৩. <b>ভিটামিন ও খনিজ:</b> প্রচুর আয়োডিন, ফসফরাস এবং ভিটামিন এ, ডি সমৃদ্ধ।<br>
    ৪. <b>রক্তশূন্যতা দূর করে:</b> আয়রন এবং ভিটামিন বি-১২ এর চমৎকার উৎস।
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📍 লোকেশন ম্যাপ":
    st.markdown('<div class="dsat-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='purple-bold'>চাঁদপুর বড় স্টেশন ঘাট</h3>", unsafe_allow_html=True)
    st.write("বিশ্বখ্যাত মাছের আড়তের সঠিক ম্যাপ নিচে দেওয়া হলো:")
    st.markdown('<a href="https://maps.google.com/?q=Chandpur+Mach+Ghat" target="_blank" style="text-decoration:none;"><div style="background:#6B46C1; color:white; text-align:center; padding:15px; border-radius:12px; font-weight:bold;">গুগল ম্যাপে দেখুন</div></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ফুটার
st.markdown("<center><p style='color:#6B46C1; margin-top:30px;'>Developed by <b>Sahib</b></p></center>", unsafe_allow_html=True)        
