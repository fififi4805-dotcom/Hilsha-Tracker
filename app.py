import streamlit as st

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="centered")

# -------------------------------
# CUSTOM CSS (Professional UI)
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');

.stApp {
    background-color: #F8F9FB;
    font-family: 'Hind Siliguri', sans-serif;
}

.custom-header {
    background: white;
    padding: 15px 20px;
    border-bottom: 3px solid #6B46C1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 0 0 15px 15px;
}

.brand {
    font-size: 22px;
    font-weight: 700;
    color: #6B46C1;
}

.menu-icon {
    font-size: 26px;
    cursor: pointer;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    margin-top: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
}

.main-btn button {
    background: linear-gradient(90deg, #FF7A00, #FF9A3C);
    color: white;
    font-weight: 700;
    height: 3.5em;
    border-radius: 12px;
    width: 100%;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<div class="custom-header">
    <div class="brand">🐟 ইলিশ কিনি</div>
    <div class="menu-icon">☰</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR MENU (☰ Menu)
# -------------------------------
with st.sidebar:
    st.header("📋 মেনু")
    page = st.radio("", [
        "🏠 হোম",
        "💰 দাম যাচাই",
        "📍 ইলিশ ঘাট লোকেশন",
        "🧬 ইলিশের উপকারিতা",
        "📞 অভিযোগ করুন"
    ])

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "🏠 হোম":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("স্বাগতম 🐟")
    st.write("সঠিক দামে চাঁদপুরের আসল ইলিশ কিনতে এখন আর ঠকতে হবে না।")

    if st.button("🔎 ইলিশ কিনির যাচাই করুন"):
        st.session_state.page = "💰 দাম যাচাই"
        st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# PRICE CHECKER
# -------------------------------
elif page == "💰 দাম যাচাই":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("💰 ইলিশের দাম যাচাই")

    size = st.selectbox("মাছের সাইজ নির্বাচন করুন", [
        "৫০০-৬০০ গ্রাম",
        "৭০০-৯০০ গ্রাম",
        "১ কেজি",
        "১.৫ কেজি+",
        "২ কেজি+"
    ])

    price_table = {
        "৫০০-৬০০ গ্রাম": 1150,
        "৭০০-৯০০ গ্রাম": 1300,
        "১ কেজি": 1600,
        "১.৫ কেজি+": 2000,
        "২ কেজি+": 2800
    }

    fair_price = price_table[size]
    st.info(f"আজকের গড় বাজার মূল্য: {fair_price} ৳")

    seller_price = st.number_input("বিক্রেতা কত টাকা চাচ্ছে?", value=fair_price)

    if st.button("দাম যাচাই করুন"):
        if seller_price > fair_price + 150:
            st.error("🚨 অতিরিক্ত দাম চাওয়া হচ্ছে!")
        elif seller_price < fair_price - 150:
            st.warning("⚠️ খুব কম দাম — মাছটি আসল নাও হতে পারে!")
        else:
            st.success("✅ দাম মোটামুটি সঠিক")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# LOCATION PAGE
# -------------------------------
elif page == "📍 ইলিশ ঘাট লোকেশন":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📍 চাঁদপুর ইলিশ ঘাট")

    st.write("চাঁদপুর বড় স্টেশন মাছ ঘাট — বাংলাদেশের সবচেয়ে বিখ্যাত ইলিশ বাজার।")

    st.markdown(
        "[📍 গুগল ম্যাপে দেখুন](https://www.google.com/maps/search/Chandpur+Fish+Ghat)",
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# BENEFITS PAGE
# -------------------------------
elif page == "🧬 ইলিশের উপকারিতা":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🧬 ইলিশ মাছের উপকারিতা")

    st.write("""
    ✅ হৃদরোগের ঝুঁকি কমায়  
    ✅ মস্তিষ্কের উন্নতি করে  
    ✅ ত্বক উজ্জ্বল রাখে  
    ✅ ভিটামিন ডি ও ওমেগা-৩ সমৃদ্ধ  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# COMPLAINT PAGE
# -------------------------------
elif page == "📞 অভিযোগ করুন":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📞 অভিযোগ কেন্দ্র")

    st.write("অতিরিক্ত দাম চাইলে অভিযোগ করুন:")

    st.markdown("## ☎️ 16121")

    st.markdown('</div>', unsafe_allow_html=True)
