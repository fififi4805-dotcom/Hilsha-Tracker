import streamlit as st

# ১. পেজ সেটআপ ও Shikho ফন্ট ইম্পোর্ট
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="centered")

# ২. প্রফেশনাল ডিজাইন (DSAT + Shikho Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&display=swap');
    
    /* মূল ব্যাকগ্রাউন্ড - DSAT এর মতো হালকা অফ-হোয়াইট */
    html, body, [class*="css"] {
        font-family: 'Hind Siliguri', sans-serif;
        background-color: #F8F9FB !important;
    }

    /* টপ বার ও ব্র্যান্ডিং (DSAT Style) */
    .header-container {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 0px; background: white; border-bottom: 3px solid #6B46C1;
        margin-bottom: 25px;
    }
    .brand-logo { font-size: 28px; font-weight: 700; color: #6B46C1; }

    /* কার্ড ও কন্টেন্ট (Shikho Style) */
    .shikho-card {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 10px 30px rgba(107, 70, 193, 0.08);
        border: 1px solid #E2E8F0; margin-bottom: 20px;
    }

    /* টেক্সট কালার */
    .purple-text { color: #6B46C1 !important; font-weight: 700; }
    .orange-text { color: #FF7A00 !important; font-weight: 700; }

    /* বাটন ডিজাইন */
    div.stButton > button {
        background: #6B46C1 !important; color: white !important;
        border-radius: 12px; height: 3.5em; width: 100%;
        border: none; font-weight: 700; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. হেডার ও ৩-ড্যাশ আইকন (শুধুমাত্র ভিজ্যুয়াল ব্র্যান্ডিং)
st.markdown("""
    <div class="header-container">
        <div class="brand-logo">ইলিশ কিনি</div>
        <div style="font-size: 26px; color: #6B46C1;">☰</div>
    </div>
    """, unsafe_allow_html=True)

# ৪. ফাংশনাল মেনুবার (বাম পাশের প্যানেল যা ৩-ড্যাশ এর কাজ করে)
with st.sidebar:
    st.markdown("<h2 class='purple-text'>মেনুবার</h2>", unsafe_allow_html=True)
    menu = st.selectbox("বিভাগ বেছে নিন", ["🏠 হোম - দাম চেক", "📜 চাঁদপুরের ইতিহাস", "🧬 পুষ্টি ও গুণাগুণ", "📍 ঘাট লোকেশন", "📞 অভিযোগ কেন্দ্র"])
    st.markdown("---")
    st.markdown("<p style='text-align:center;'>Developed by <b>Sahib</b></p>", unsafe_allow_html=True)

# ৫. কন্টেন্ট এরিয়া
if menu == "🏠 হোম - দাম চেক":
    st.markdown("<h1 style='text-align:center;' class='purple-text'>স্বাগতম আপনাকে</h1>", unsafe_allow_html=True)
    st.markdown('<div class="shikho-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='orange-text'>বাজার দর যাচাই করুন</h3>", unsafe_allow_html=True)
    
    size = st.selectbox("মাছের ওজন নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    prices = {"৫০০-৬০০ গ্রাম": 1150, "৭০০-৯০০ গ্রাম": 1250, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1950, "২ কেজি+": 2700}
    fair_price = prices[size]
    
    st.write(f"সঠিক মূল্য: **{fair_price} ৳ (প্রতি কেজি)**")
    user_price = st.number_input("বিক্রেতা কত চাচ্ছে?", value=fair_price)
    
    if st.button("রেজাল্ট দেখুন"):
        if user_price > fair_price + 150:
            st.error(f"অতিরিক্ত দাম! আপনি {user_price - fair_price} টাকা বেশি দিচ্ছেন।")
        else:
            st.success("দাম একদম সঠিক। আপনি কিনতে পারেন।")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📜 চাঁদপুরের ইতিহাস":
    st.markdown('<div class="shikho-card">', unsafe_allow_html=True)
    st.markdown("<h2 class='orange-text'>ইলিশের রাজধানী চাঁদপুর</h2>", unsafe_allow_html=True)
    st.write("""
    চাঁদপুর হলো ইলিশের আসল বাড়ি। পদ্মা, মেঘনা ও ডাকাতিয়া নদীর মিলনস্থলের কারণে এখানকার পানির বিশেষ লবণাক্ততা ইলিশের স্বাদকে পৃথিবীর সেরা করে তোলে। 
    চাঁদপুর বড় স্টেশন ঘাট থেকে সারা দেশে ইলিশ সরবরাহ হয়। ১৯শ শতাব্দী থেকেই চাঁদপুরের ইলিশের সুখ্যাতি বিশ্বজুড়ে।
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🧬 পুষ্টি ও গুণাগুণ":
    st.markdown('<div class="shikho-card">', unsafe_allow_html=True)
    st.markdown("<h2 class='orange-text'>কেন খাবেন চাঁদপুরের ইলিশ?</h2>", unsafe_allow_html=True)
    st.write("""
    • **হৃদরোগ প্রতিরোধ:** এতে থাকা ওমেগা-৩ ফ্যাটি অ্যাসিড হার্ট সুস্থ রাখে।
    • **স্মৃতিশক্তি বৃদ্ধি:** শিশুদের মস্তিষ্কের মেধা বিকাশে এটি অত্যন্ত উপকারী।
    • **ত্বকের যত্ন:** এটি ত্বক উজ্জ্বল করে এবং চুল পড়া কমায়।
    • **রোগ প্রতিরোধ:** প্রচুর ভিটামিন এ এবং ডি থাকায় শরীর সুস্থ রাখে।
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📍 ঘাট লোকেশন":
    st.markdown('<div class="shikho-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='purple-text'>সরাসরি চাঁদপুর মাছ ঘাট লোকেশন</h3>", unsafe_allow_html=True)
    st.markdown("""
        <a href="https://www.google.com/maps/search/Chandpur+Fish+Ghat" target="_blank" style="text-decoration:none;">
            <div style="background:#FF7A00; color:white; text-align:center; padding:15px; border-radius:12px; font-weight:bold;">গুগল ম্যাপে ঘাট দেখুন</div>
        </a>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📞 অভিযোগ কেন্দ্র":
    st.markdown('<div class="shikho-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<h2 class='purple-text'>ভোক্তা অধিকার চাঁদপুর</h2>", unsafe_allow_html=True)
    st.write("বেশি দাম চাইলে এই নাম্বারে সরাসরি কল করুন:")
    st.markdown("<a href='tel:16121' style='text-decoration:none;'><h1 class='orange-text' style='font-size:60px;'>16121</h1></a>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<br><center><p style='color:#6B46C1;'>Developed by <b>Sahib</b> | © 2026 Elish Kini</p></center>", unsafe_allow_html=True)    
    
