import streamlit as st

# ১. গুগল স্ট্যান্ডার্ড পেজ কনফিগ (Shikho/DSAT Style)
st.set_page_config(page_title="Elish Kini Pro", page_icon="🐟", layout="centered")

# ২. আলটিমেট প্রিমিয়াম ডার্ক থিম CSS (৩য় পিকের হুবহু লুক)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&display=swap');
    
    /* মেইন ব্যাকগ্রাউন্ড - Midnight Dark */
    .stApp {
        background-color: #0F172A !important;
        font-family: 'Hind Siliguri', sans-serif !important;
    }

    /* সাইডবার ডার্ক লুক */
    [data-testid="stSidebar"] {
        background-color: #1E293B !important;
        border-right: 1px solid #334155;
    }

    /* ৩য় পিকের মতো ঝকঝকে সাদা ফন্ট */
    h1, h2, h3, p, span, label, b, li {
        color: #F8FAFC !important;
    }

    /* টপ বার (Shikho Style) */
    .top-header {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    /* ডেটা কার্ডস (Shikho Dashboard Style) */
    .data-card {
        background: #1E293B;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #334155;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .data-card:hover { border-color: #6366F1; }

    /* নিওন হাইলাইট কালার */
    .neon-purple { color: #A855F7 !important; font-weight: 700; }
    .neon-orange { color: #F59E0B !important; font-weight: 700; }
    .neon-blue { color: #38BDF8 !important; font-weight: 700; }

    /* বাটন ফিক্স */
    div.stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%) !important;
        color: white !important;
        border-radius: 10px;
        height: 3.5em; width: 100%; border: none; font-weight: 700;
    }

    /* ইনপুট বক্স ডার্ক স্টাইল */
    div[data-baseweb="select"] > div, input {
        background-color: #0F172A !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. কাস্টম টপ বার
st.markdown("""
    <div class="top-header">
        <div style="font-size:20px; font-weight:700; color:#A855F7;">Shikho Elish 🐟</div>
        <div style="color:#94A3B8; font-size:14px;">Senior Dev: Sahib</div>
    </div>
    """, unsafe_allow_html=True)

# ৪. সাইডবার ন্যাভিগেশন
with st.sidebar:
    st.markdown("<h2 class='neon-purple'>Dashboard</h2>", unsafe_allow_html=True)
    menu = st.radio("মেনু সিলেক্ট করুন:", [
        "📊 বাজার ও বাণিজ্য ডেটা", 
        "⚖️ দাম যাচাই মেশিন", 
        "💡 ইলিশ কেনার গোপন টিপস",
        "📞 কমপ্লেন সেন্টার"
    ])

# ৫. কন্টেন্ট এরিয়া
if menu == "📊 বাজার ও বাণিজ্য ডেটা":
    st.markdown("<h2 class='neon-blue'>চাঁদপুর ইলিশ রিপোর্ট ২০২৪-২৫</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="data-card">
            <p style="color:#94A3B8 !important;">মোট রপ্তানি (বছর)</p>
            <h2 class="neon-orange">৫২,০০০+ টন</h2>
            <p style="font-size:12px;">ভারত ও ইউরোপে সর্বাধিক</p>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="data-card">
            <p style="color:#94A3B8 !important;">সরকারি রাজস্ব আয়</p>
            <h2 class="neon-purple">১২৫ কোটি+</h2>
            <p style="font-size:12px;">চাঁদপুর মোহনা জোন থেকে</p>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("<div class='data-card'>", unsafe_allow_html=True)
    st.markdown("<h3 class='neon-blue'>বাণিজ্যিক ইতিহাস</h3>", unsafe_allow_html=True)
    st.write("চাঁদপুর ঘাট থেকে প্রতিদিন গড়ে প্রায় ৮০০-১২০০ মণ ইলিশ দেশের বিভিন্ন প্রান্তে সরবরাহ হয়। বিশেষ করে ইলিশের মৌসুমে এই লেনদেন দৈনিক ১০-১৫ কোটি টাকা ছাড়িয়ে যায়।")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "⚖️ দাম যাচাই মেশিন":
    st.markdown("<div class='data-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='neon-purple'>স্মার্ট প্রাইস ডিটেক্টর</h2>", unsafe_allow_html=True)
    
    size = st.selectbox("মাছের সাইজ:", ["৫০০-৬০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    prices = {"৫০০-৬০০ গ্রাম": 1150, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1950, "২ কেজি+": 2750}
    fair_price = prices[size]
    
    st.write(f"অফিশিয়াল গড় দাম: **{fair_price} ৳**")
    user_p = st.number_input("বিক্রেতার চাওয়া দাম:", value=int(fair_price))
    
    if st.button("রেজাল্ট চেক করুন"):
        if user_p > fair_price + 150:
            st.error(f"🚨 অতিরিক্ত {user_p - fair_price} টাকা বেশি! দরাদরি করুন।")
        else:
            st.success("✅ দাম ঠিক আছে। নিতে পারেন।")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "💡 ইলিশ কেনার গোপন টিপস":
    st.markdown("<h2 class='neon-orange'>রিসার্চ ভিত্তিক সেরা ইলিশ চেনার টিপস</h2>", unsafe_allow_html=True)
    st.markdown("""<div class='data-card'>
        <p><b>১. পেট পরীক্ষা:</b> পেটে চাপ দিলে যদি মুখ দিয়ে ডিম বা মল বের হয়, তবে বুঝবেন মাছটি নরম হয়ে গেছে। শক্ত পেটের মাছ কিনুন।</p>
        <p><b>২. রূপালী আভা:</b> টাটকা ইলিশ আয়নার মতো চকচক করবে। চোখে রক্ত জমে লাল হয়ে থাকলে সেই মাছ এড়িয়ে চলুন।</p>
        <p><b>৩. মোহনার মাছ:</b> চাঁদপুরের মোহনার মাছ চেনার উপায় হলো এটি আকারে কিছুটা গোলগাল (পটকা) হবে এবং লেজের দিকটা সরু হবে।</p>
        <p><b>৪. ফুলকার রঙ:</b> ফুলকা যদি টকটকে লাল হয় তবে সেটি টাটকা। কালচে ফুলকা মানে হিমায়িত বা পুরনো মাছ।</p>
    </div>""", unsafe_allow_html=True)

elif menu == "📞 কমপ্লেন সেন্টার":
    st.markdown("<div class='data-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<h2 class='neon-purple'>ভোক্তা অধিকার হটলাইন</h2>", unsafe_allow_html=True)
    st.write("চাঁদপুর মাছ ঘাটে প্রতারিত হলে সরাসরি ডায়াল করুন:")
    st.markdown("<h1 style='color:#F59E0B !important; font-size:60px;'>16121</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<center><p style='color:#64748B; font-size:12px; margin-top:50px;'>© 2026 Elish Pro | Senior Dev: Sahib | Shikho Inspired UI</p></center>", unsafe_allow_html=True)
