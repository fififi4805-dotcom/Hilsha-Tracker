import streamlit as st

# ১. প্রফেশনাল পেজ কনফিগ
st.set_page_config(page_title="Elish Kini Pro", page_icon="🐟", layout="centered")

# ২. ডার্ক মোড কিলার CSS (Force Visibility)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&display=swap');
    
    /* পুরো অ্যাপের ব্যাকগ্রাউন্ড - Midnight Blue */
    .stApp {
        background-color: #0F172A !important;
        font-family: 'Hind Siliguri', sans-serif !important;
    }

    /* ড্রপডাউন ও ইনপুট বক্স ফিক্স (সবচেয়ে জরুরি) */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, input {
        background-color: #E2E8F0 !important; /* হালকা গ্রে ব্যাকগ্রাউন্ড */
        color: #000000 !important; /* কুচকুচে কালো লেখা */
        border: 2px solid #6366F1 !important;
        border-radius: 10px !important;
    }
    
    /* ড্রপডাউন অপশন লিস্ট ফিক্স */
    ul[role="listbox"] {
        background-color: #FFFFFF !important;
    }
    ul[role="listbox"] li {
        color: #000000 !important;
    }

    /* সব সাধারণ টেক্সট এবং লেবেল - ঝকঝকে সাদা */
    h1, h2, h3, p, span, label, b, li, .stMarkdown {
        color: #FFFFFF !important;
    }

    /* ন্যাভিগেশন বক্স */
    .nav-header {
        background: #1E293B;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #334155;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }

    /* মেনুবার গাইড */
    .menu-pointer {
        color: #A855F7;
        font-weight: 700;
        border: 1px dashed #A855F7;
        padding: 5px 10px;
        border-radius: 8px;
    }

    /* স্ট্যাট কার্ড (Shikho Style) */
    .stat-card {
        background: #1E293B;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #334155;
        text-align: center;
        margin-bottom: 15px;
    }
    .neon-text { color: #A855F7 !important; font-size: 24px; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# ৩. কাস্টম হেডার
st.markdown("""
    <div class="nav-header">
        <div style="font-size:20px; font-weight:700; color:#6366F1;">ELISH KINI PRO 🐟</div>
        <div class="menu-pointer">মেনু ← ☰</div>
    </div>
    """, unsafe_allow_html=True)

# ৪. সাইডবার (মেনুবার)
with st.sidebar:
    st.markdown("<h2 style='color:#A855F7 !important;'>Menu Dashboard</h2>", unsafe_allow_html=True)
    menu = st.radio("বিভাগ বেছে নিন:", [
        "📊 বাজার ও রপ্তানি রিপোর্ট", 
        "⚖️ স্মার্ট প্রাইস ডিটেক্টর", 
        "💡 ইলিশ কেনার গোপন টিপস",
        "📞 অভিযোগ কেন্দ্র"
    ])
    st.markdown("---")
    st.markdown("Senior Dev: **Sahib**")

# ৫. কন্টেন্ট লজিক
if menu == "📊 বাজার ও রপ্তানি রিপোর্ট":
    st.markdown("### চাঁদপুরের ইলিশ বাণিজ্য ডেটা")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="stat-card"><p>বার্ষিক রপ্তানি</p><div class="neon-text">৫২,০০০ টন+</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><p>সরকারি লাভ (রাজস্ব)</p><div class="neon-text">১২৫ কোটি+</div></div>', unsafe_allow_html=True)
    st.info("তথ্যসূত্র: মৎস্য অধিদপ্তর ও চাঁদপুর বন্দর কর্তৃপক্ষ (২০২৪-২৫)")

elif menu == "⚖️ স্মার্ট প্রাইস ডিটেক্টর":
    st.markdown("### সঠিক দাম যাচাই করুন")
    # ড্রপডাউন এখন একদম পরিষ্কার দেখা যাবে
    size = st.selectbox("মাছের ওজন নির্বাচন করুন:", ["৫০০-৬০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    prices = {"৫০০-৬০০ গ্রাম": 1150, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1950, "২ কেজি+": 2750}
    fair_price = prices[size]
    
    st.markdown(f"গড় বাজার দর: **{fair_price} ৳**")
    user_p = st.number_input("বিক্রেতা কত চাচ্ছে?", value=int(fair_price))
    
    if st.button("রেজাল্ট দেখুন"):
        if user_p > fair_price + 150:
            st.error(f"🚨 অতিরিক্ত {user_p - fair_price} টাকা বেশি চাচ্ছে!")
        else:
            st.success("✅ দাম একদম সঠিক আছে।")

elif menu == "💡 ইলিশ কেনার গোপন টিপস":
    st.markdown("### সেরা ইলিশ চেনার ৪টি উপায়")
    st.markdown("""
    1. **ফুলকা:** উজ্জ্বল লাল হতে হবে (ধূসর মানেই পুরনো)।
    2. **পেট:** হাত দিয়ে চাপ দিলে যদি শক্ত লাগে তবেই কিনুন।
    3. **চোখ:** স্বচ্ছ ও মণির মতো চকচকে হতে হবে।
    4. **আঁশ:** গায়ের রূপালী আভা একদম আয়নার মতো চকচকে হবে।
    """)

elif menu == "📞 অভিযোগ কেন্দ্র":
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.markdown("## ভোক্তা অধিকার চাঁদপুর")
    st.write("প্রতারিত হলে সরাসরি কল করুন:")
    st.markdown("<h1 style='color:#F59E0B !important; font-size:60px; margin:10px 0;'>16121</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<center><p style='color:#64748B; font-size:12px; margin-top:40px;'>© 2026 | Senior Dev: Sahib</p></center>", unsafe_allow_html=True)
