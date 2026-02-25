      import streamlit as st

# ১. পেজ সেটআপ
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="wide")

# ২. DSAT School স্টাইল CSS (Purple, White, Orange)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;700;900&family=Hind+Siliguri:wght@400;700&display=swap');
    
    /* পুরো বডি সাদা */
    html, body, [class*="css"] {
        font-family: 'Public Sans', 'Hind Siliguri', sans-serif;
        background-color: #FFFFFF !important;
    }

    /* টপ বার (DSAT School এর মতো) */
    .header-container {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 5%; background: white; border-bottom: 1px solid #f0f0f0;
    }
    .brand-logo {
        font-size: 26px; font-weight: 900; color: #6B46C1; /* Purple */
    }

    /* কমলা টেক্সট (১ম পিকের মতো) */
    .orange-text {
        color: #FF7A00 !important; font-weight: 800;
    }

    /* বেগুনি বাটন (Enroll বাটনের মতো) */
    div.stButton > button:first-child {
        background-color: #6B46C1; color: white !important;
        border-radius: 50px; padding: 10px 30px; font-weight: 700;
        border: none; width: 100%; transition: 0.3s;
    }
    
    /* কমলা বাটন (Book a Session এর মতো) */
    .stDownloadButton button {
        background-color: #FF7A00 !important; color: white !important;
        border-radius: 50px; width: 100%; border: none;
    }

    /* ইনফো কার্ড (DSAT স্টাইল) */
    .info-card {
        border: 2px solid #6B46C1; border-radius: 20px;
        padding: 20px; margin-bottom: 20px; background: white;
    }
    
    /* সাইডবার মেনু */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF; border-right: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. টপ হেডার (ব্র্যান্ডিং ও ৩ ড্যাশ মেনু)
st.markdown("""
    <div class="header-container">
        <div class="brand-logo">ইলিশ কিনি</div>
        <div style="font-size: 24px; color: #6B46C1;">☰</div>
    </div>
    """, unsafe_allow_html=True)

# ৪. সাইডবার মেনুবার (আইকন + পরিষ্কার টেক্সট)
with st.sidebar:
    st.markdown("<h2 style='color:#6B46C1;'>মেনুবার</h2>", unsafe_allow_html=True)
    choice = st.radio("ক্যাটাগরি বেছে নিন:", [
        "🏠 হোম - বাজার দর", 
        "📍 মাছ ঘাট লোকেশন", 
        "📜 ইলিশের ইতিহাস", 
        "🩺 স্বাস্থ্য গুণাগুণ", 
        "📞 অভিযোগ কেন্দ্র"
    ])
    st.markdown("---")
    st.write("ডেভেলপার: **সাহিব**")

# ৫. মেইন কন্টেন্ট
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#6B46C1;'>স্বাগতম আপনাকে</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;' class='orange-text'>সঠিক ইলিশ কিনুন সঠিক দামে</h2>", unsafe_allow_html=True)

if "🏠 হোম" in choice:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='orange-text'>আজকের বাজার দর যাচাই</h3>", unsafe_allow_html=True)
    
    size = st.selectbox("মাছের সাইজ নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    
    # প্রাইস ডাটা
    prices = {"৫০০-৬০০ গ্রাম": 1150, "৭০০-৯০০ গ্রাম": 1250, "১ কেজি সাইজ": 1500, "১.৫ কেজি+": 1900, "২ কেজি+": 2700}
    target = prices[size]
    
    st.markdown(f"<p style='color:#6B46C1; font-size:18px;'>সঠিক মূল্য: <b>{target} ৳ (প্রতি কেজি)</b></p>", unsafe_allow_html=True)
    user_p = st.number_input("বিক্রেতা কত দাম চাচ্ছে?", value=target)
    
    if st.button("দাম যাচাই করুন"):
        if user_p > target + 150:
            st.error(f"🚨 সাবধান! আপনি অতিরিক্ত {user_p - target} টাকা দিচ্ছেন।")
        else:
            st.success("✅ দাম একদম ঠিক আছে।")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

elif "📍 মাছ ঘাট" in choice:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='orange-text'>চাঁদপুর বড় স্টেশন মাছ ঘাট</h3>", unsafe_allow_html=True)
    st.write("সেরা ইলিশের জন্য সরাসরি চলে যান চাঁদপুরের মোহনায়।")
    # সলিড গুগল ম্যাপস লিঙ্ক
    map_link = "https://www.google.com/maps/search/Chandpur+Fish+Ghat"
    st.markdown(f"""
        <a href="{map_link}" target="_blank" style="text-decoration:none;">
            <div style="background:#FF7A00; color:white; text-align:center; padding:15px; border-radius:50px; font-weight:bold;">
                গুগল ম্যাপে লোকেশন দেখুন
            </div>
        </a>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif "📜 ইতিহাস" in choice:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='orange-text'>ইলিশের গৌরবগাথা</h3>", unsafe_allow_html=True)
    st.write("চাঁদপুর হলো ইলিশের রাজধানী। এখানকার পদ্মা-মেঘনা মোহনার মাছ পৃথিবীর সেরা।")
    st.markdown('</div>', unsafe_allow_html=True)

elif "📞 অভিযোগ" in choice:
    st.markdown('<div style="background:#FFF5F5; padding:40px; border-radius:20px; text-align:center; border:2px solid #6B46C1;">', unsafe_allow_html=True)
    st.markdown("<h2 class='orange-text'>ভোক্তা অধিকার চাঁদপুর</h2>", unsafe_allow_html=True)
    st.write("অতিরিক্ত দাম চাইলে কল করুন")
    st.markdown('<a href="tel:16121" style="text-decoration:none;"><h1 style="color:#6B46C1; font-size:60px;">📞 16121</h1></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<center><p style='color:#6B46C1;'>Developed by <b>Sahib</b> | © 2026 Elish Kini</p></center>", unsafe_allow_html=True)
