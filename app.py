import streamlit as st

# ১. পেজ কনফিগ (আধুনিক ও ক্লিন)
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="centered")

# ২. CSS: Shikho ও DSAT এর সংমিশ্রণে প্রিমিয়াম ডিজাইন
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Hind Siliguri', sans-serif;
        background-color: #FFFFFF !important;
        color: #2D3748;
    }

    /* টপ বার ও ব্র্যান্ডিং (DSAT Style) */
    .top-header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 0px; border-bottom: 2px solid #F0F2F5; margin-bottom: 30px;
    }
    .brand-logo {
        font-size: 30px; font-weight: 700; color: #6B46C1; /* Purple */
    }

    /* টেক্সট কালার (Shikho & DSAT Style) */
    .hero-text { color: #6B46C1; font-weight: 700; font-size: 32px; text-align: center; }
    .highlight-orange { color: #FF7A00 !important; font-weight: 700; }
    
    /* বাটন ও ইনপুট বক্স */
    div.stButton > button:first-child {
        background: #6B46C1; color: white !important;
        border-radius: 12px; height: 3.5em; width: 100%;
        border: none; font-weight: 600; font-size: 16px;
    }
    .stSelectbox, .stNumberInput {
        border-radius: 12px;
    }

    /* কন্টেন্ট কার্ড */
    .info-box {
        background: #FFFFFF; border: 1.5px solid #E2E8F0;
        padding: 25px; border-radius: 18px; margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. প্রফেশনাল রাইট-সাইড মেনুবার (Sidebar)
with st.sidebar:
    st.markdown("<h2 style='color:#6B46C1;'>মেনুবার</h2>", unsafe_allow_html=True)
    menu = st.radio("", ["🏠 দাম চেক করুন", "📍 চাঁদপুর মাছ ঘাট", "📜 ইলিশের ইতিহাস", "🩺 পুষ্টি ও গুণাগুণ", "📞 অভিযোগ কেন্দ্র"])
    st.markdown("---")
    st.markdown("<p style='text-align:center;'>Developed by <b>Sahib</b></p>", unsafe_allow_html=True)

# ৪. মেইন হেডার
st.markdown("""
    <div class="top-header">
        <div class="brand-logo">ইলিশ কিনি</div>
        <div style="font-size: 24px; color: #6B46C1;">☰</div>
    </div>
    """, unsafe_allow_html=True)

# ৫. কন্টেন্ট সেকশন
if menu == "🏠 দাম চেক করুন":
    st.markdown('<div class="hero-text">স্বাগতম আপনাকে</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-size:20px; margin-bottom:20px;">সঠিক দামে কিনুন <span class="highlight-orange">চাঁদপুরের ইলিশ</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    fish_size = st.selectbox("মাছের আকার নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    
    # রিয়েল টাইম প্রাইস ডাটা
    prices = {"৫০০-৬০০ গ্রাম": 1150, "৭০০-৯০০ গ্রাম": 1250, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1950, "২ কেজি+": 2700}
    current_price = prices[fish_size]
    
    st.markdown(f"গড় বাজার মূল্য: <b class='highlight-orange'>{current_price} ৳</b>", unsafe_allow_html=True)
    user_price = st.number_input("বিক্রেতা কত দাম চাচ্ছে?", value=current_price)
    
    if st.button("যাচাই করুন"):
        if user_price > current_price + 150:
            st.error(f"অতিরিক্ত দাম! আপনি প্রতি কেজিতে {user_price - current_price} টাকা বেশি দিচ্ছেন।")
        else:
            st.success("দাম একদম সঠিক আছে। আপনি কিনতে পারেন।")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📍 চাঁদপুর মাছ ঘাট":
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.subheader("📍 চাঁদপুর বড় স্টেশন মাছ ঘাট")
    st.write("বিশ্বের সবচেয়ে বড় ইলিশের বাজার হিসেবে চাঁদপুর মাছ ঘাট পরিচিত। সরাসরি ঘাটের তাজা মাছের লোকেশন নিচে দেওয়া হলো:")
    st.markdown('<a href="https://www.google.com/maps/search/Chandpur+Mash+Ghat" target="_blank" style="text-decoration:none;"><div style="background:#FF7A00; color:white; text-align:center; padding:15px; border-radius:12px; font-weight:bold;">গুগল ম্যাপে লোকেশন দেখুন</div></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📜 ইলিশের ইতিহাস":
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("<h3 class='highlight-orange'>ইলিশের রাজধানী চাঁদপুর</h3>", unsafe_allow_html=True)
    st.write("""
    চাঁদপুরকে ইলিশের বাড়ি বলা হয় কারণ এখানে পদ্মা, মেঘনা ও ডাকাতিয়া নদীর মিলনস্থল। নোনা জল থেকে মিষ্টি জলে আসার সময় ইলিশের শরীরে যে ফ্যাট বা চর্বি জমে, তা-ই এর স্বাদ বহুগুণ বাড়িয়ে দেয়। 
    চাঁদপুর মাছ ঘাট থেকে প্রতিদিন কয়েক হাজার টন মাছ সারা দেশে এবং বিদেশে (বিশেষ করে ভারতে) রপ্তানি হয়।
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🩺 পুষ্টি ও গুণাগুণ":
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("<h3 class='highlight-orange'>কেন খাবেন চাঁদপুরের ইলিশ?</h3>", unsafe_allow_html=True)
    st.write("""
    • **ওমেগা-৩:** এটি হৃদরোগের ঝুঁকি কমায় এবং রক্তচাপ নিয়ন্ত্রণে রাখে।
    • **মস্তিষ্কের বিকাশ:** শিশুদের মেধা বিকাশে অত্যন্ত কার্যকর।
    • **ভিটামিন:** এতে প্রচুর ভিটামিন এ, ডি এবং বি-১২ রয়েছে।
    • **খনিজ:** আয়োডিন ও সেলেনিয়াম সমৃদ্ধ যা থাইরয়েড সুস্থ রাখে।
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📞 অভিযোগ কেন্দ্র":
    st.markdown('<div class="info-box" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#6B46C1;'>ভোক্তা অধিকার চাঁদপুর</h2>", unsafe_allow_html=True)
    st.write("অসাধু ব্যবসায়ীরা বেশি দাম চাইলে কল করুন:")
    st.markdown('<a href="tel:16121" style="text-decoration:none;"><h1 class="highlight-orange" style="font-size:50px;">📞 16121</h1></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<p style='text-align:center; color:#A0AEC0; font-size:14px; margin-top:50px;'>Developed by <b>Sahib</b> | © 2026 Elish Kini</p>", unsafe_allow_html=True)
