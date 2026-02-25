import streamlit as st

# ১. প্রফেশনাল পেজ কনফিগ ও থিম ফিক্স
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="centered")

# ২. ডার্ক মোড প্রুফ CSS (Force White Background & Black Text)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');
    
    /* ব্যাকগ্রাউন্ড ও টেক্সট ক্ল্যারিটি */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* সব টেক্সটকে কুচকুচে কালো করা */
    h1, h2, h3, p, span, label, div, li {
        font-family: 'Hind Siliguri', sans-serif !important;
        color: #000000 !important;
    }

    /* টপ ন্যাভিগেশন বার - DSAT Style */
    .top-nav {
        background-color: #6B46C1;
        padding: 15px;
        border-radius: 0 0 15px 15px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .top-nav h1 { color: #FFFFFF !important; margin: 0; font-size: 24px; }

    /* হোয়াইট কার্ড ডিজাইন */
    .info-card {
        background-color: #F8F9FB !important;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }

    /* বাটন ফিক্স (Premium Purple) */
    div.stButton > button {
        background-color: #6B46C1 !important;
        color: white !important;
        border-radius: 10px;
        height: 3.5em;
        width: 100%;
        border: none;
        font-weight: 700;
    }

    /* সাইডবার মেনুবার স্টাইল */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #6B46C1;
    }
    
    .orange-text { color: #FF7A00 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ৩. হেডার
st.markdown('<div class="top-nav"><h1>ইলিশ কিনি</h1></div>', unsafe_allow_html=True)

# ৪. ফাংশনাল মেনুবার (বাম পাশে)
with st.sidebar:
    st.markdown("<h2 style='color:#6B46C1 !important;'>মেনুবার</h2>", unsafe_allow_html=True)
    menu = st.radio("বিভাগ বেছে নিন:", [
        "🏠 হোম - দাম যাচাই", 
        "📜 চাঁদপুরের ইতিহাস", 
        "🧬 পুষ্টি ও গুণাগুণ", 
        "📞 অভিযোগ কেন্দ্র"
    ])
    st.markdown("---")
    st.write("Senior Dev: **Sahib**")

# ৫. কন্টেন্ট এরিয়া
st.markdown('<div class="info-card">', unsafe_allow_html=True)

if menu == "🏠 হোম - দাম যাচাই":
    st.markdown("<h2 style='text-align:center;'>বাজার দর যাচাই</h2>", unsafe_allow_html=True)
    size = st.selectbox("মাছের ওজন নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    
    # প্রাইস ডিকশনারি (AttributeError ফিক্স করা হয়েছে)
    prices = {
        "৫০০-৬০০ গ্রাম": 1150, 
        "১ কেজি সাইজ": 1550, 
        "১.৫ কেজি+": 1950, 
        "২ কেজি+": 2750
    }
    
    fair_price = prices.get(size, 1550)
    st.write(f"সঠিক বাজার দর: **{fair_price} ৳ (প্রতি কেজি)**")
    
    user_p = st.number_input("বিক্রেতা কত দাম চাচ্ছে?", value=int(fair_price))
    
    if st.button("রেজাল্ট দেখুন"):
        if user_p > fair_price + 150:
            st.error(f"🚨 অতিরিক্ত {user_p - fair_price} টাকা বেশি চাচ্ছে!")
        else:
            st.success("✅ দাম একদম সঠিক আছে।")

elif menu == "📜 চাঁদপুরের ইতিহাস":
    st.markdown("<h2 class='orange-text'>ইলিশের রাজধানী চাঁদপুর</h2>", unsafe_allow_html=True)
    st.write("চাঁদপুরের পদ্মা-মেঘনা-ডাকাতিয়া নদীর মোহনায় পানির বিশেষ স্রোত ও লবণাক্ততার কারণে এখানকার ইলিশের স্বাদ বিশ্বসেরা। ব্রিটিশ আমল থেকেই চাঁদপুর বড় স্টেশন মাছ ঘাট ইলিশ বাণিজ্যের প্রধান কেন্দ্র।")

elif menu == "🧬 পুষ্টি ও গুণাগুণ":
    st.markdown("<h2 class='orange-text'>কেন খাবেন ইলিশ?</h2>", unsafe_allow_html=True)
    st.write("""
    * **ওমেগা-৩:** এটি হৃদরোগের ঝুঁকি কমায়।
    * **স্মৃতিশক্তি:** শিশুদের মেধা বিকাশে অত্যন্ত কার্যকর।
    * **ভিটামিন ডি:** হাড় মজবুত ও ক্যালসিয়াম বৃদ্ধি করে।
    """)

elif menu == "📞 অভিযোগ কেন্দ্র":
    st.markdown("<h2 style='color:#6B46C1 !important; text-align:center;'>ভোক্তা অধিকার চাঁদপুর</h2>", unsafe_allow_html=True)
    st.write("অসাধু ব্যবসায়ীরা বেশি দাম চাইলে সরাসরি অভিযোগ করুন:")
    st.markdown("<h1 style='text-align:center; color:#FF7A00 !important; font-size:50px;'>16121</h1>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<center><p style='color:#6B46C1 !important;'>© 2026 | Developed by Sahib</p></center>", unsafe_allow_html=True)
