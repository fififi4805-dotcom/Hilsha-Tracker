import streamlit as st

# ১. গুগল স্ট্যান্ডার্ড পেজ কনফিগ (URL অপরিবর্তিত থাকবে)
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="centered")

# ২. প্রফেশনাল সিএসএস (DSAT Style & High Visibility)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');
    
    /* ব্যাকগ্রাউন্ড ফিক্সড: DSAT গ্রে এবং হোয়াইট কার্ড */
    .stApp {
        background-color: #F8F9FB !important;
        font-family: 'Hind Siliguri', sans-serif !important;
    }

    /* ডার্ক মোড প্রটেকশন: সব টেক্সট কালো থাকবে */
    h1, h2, h3, p, span, label, li, div {
        color: #1A202C !important;
    }

    /* কাস্টম হেডার (Shikho & DSAT Combined) */
    .custom-header {
        background-color: #FFFFFF;
        padding: 15px 25px;
        border-bottom: 3px solid #6B46C1;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky; top: 0; z-index: 1000;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .brand-name { font-size: 24px; font-weight: 700; color: #6B46C1 !important; }
    .nav-icon { font-size: 28px; color: #6B46C1 !important; cursor: pointer; }

    /* প্রিমিয়াম কন্টেন্ট কার্ড */
    .dsat-card {
        background-color: #FFFFFF !important;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        margin-top: 25px;
        box-shadow: 0 10px 25px rgba(107, 70, 193, 0.05);
    }

    /* বাটন ও ইনপুট ফিক্স (নো আকাশী কালার) */
    div.stButton > button {
        background: linear-gradient(90deg, #6B46C1, #805AD5) !important;
        color: white !important;
        border-radius: 12px; height: 3.5em; width: 100%;
        border: none; font-weight: 700; font-size: 18px;
    }
    
    /* হাইলাইট কালার */
    .orange-bold { color: #FF7A00 !important; font-weight: 700; }
    .purple-bold { color: #6B46C1 !important; font-weight: 700; }

    /* সাইডবার প্রফেশনাল লুক */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #6B46C1;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. কাস্টম হেডার ও ৩-ড্যাশ আইকন (টপ বার)
st.markdown("""
    <div class="custom-header">
        <div class="brand-name">ইলিশ কিনি</div>
        <div class="nav-icon">☰</div>
    </div>
    """, unsafe_allow_html=True)

# ৪. ফাংশনাল মেনুবার (বাম পাশে যা ৩-ড্যাশ আইকন দিয়ে কন্ট্রোলড)
with st.sidebar:
    st.markdown("<h2 class='purple-bold'>মেনুবার</h2>", unsafe_allow_html=True)
    menu = st.radio("বিভাগ বেছে নিন:", [
        "🏠 হোম - দাম যাচাই", 
        "📜 চাঁদপুরের পূর্ণ ইতিহাস", 
        "🧬 পুষ্টি ও বিজ্ঞান", 
        "📍 ঘাট লোকেশন", 
        "📞 অভিযোগ কেন্দ্র"
    ])
    st.markdown("---")
    st.write("Senior Developer: **Sahib**")

# ৫. মেইন কন্টেন্ট
st.markdown('<div class="dsat-card">', unsafe_allow_html=True)

if menu == "🏠 হোম - দাম যাচাই":
    st.markdown("<h2 style='text-align:center;' class='purple-bold'>স্বাগতম আপনাকে</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>সঠিক দামে কিনুন <span class='orange-bold'>চাঁদপুরের রুপালী ইলিশ</span></p>", unsafe_allow_html=True)
    
    size = st.selectbox("মাছের ওজন নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    prices = {"৫০০-৬০০ গ্রাম": 1150, "৭০০-৯০০ গ্রাম": 1250, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1950, "২ কেজি+": 2750}
    fair_price = prices[size]
    
    st.markdown(f"আজকের গড় বাজার মূল্য: <b class='orange-bold'>{fair_price} ৳</b>", unsafe_allow_html=True)
    user_p = st.number_input("বিক্রেতা কত দাম চাচ্ছে?", value=fair_price)
