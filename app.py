import streamlit as st

# 1. Page Config (URL same thakbe)
st.set_page_config(page_title="Elish Kini", page_icon="🐟", layout="centered")

# 2. Premium CSS (Fixing Visibility & DSAT Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');
    
    /* Background & Text Color Fix (Dark Mode Protection) */
    .stApp {
        background-color: #F0F2F5 !important; /* DSAT Greyish White */
    }
    
    /* Force all text to be visible */
    h1, h2, h3, p, span, label, div {
        font-family: 'Hind Siliguri', sans-serif !important;
        color: #1A202C !important; /* Pure Blackish Grey for visibility */
    }

    /* Top Bar Shikho Style */
    .top-header {
        background-color: #6B46C1;
        padding: 20px;
        border-radius: 0 0 20px 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .top-header h1 { color: white !important; margin: 0; font-size: 28px; }

    /* Premium Card DSAT Style */
    .dsat-card {
        background-color: #FFFFFF !important;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        margin-top: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }

    /* Orange Highlight */
    .highlight { color: #FF7A00 !important; font-weight: 700; }

    /* Button Style */
    div.stButton > button {
        background: linear-gradient(90deg, #6B46C1, #805AD5) !important;
        color: white !important;
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        border: none;
        font-weight: 700;
        font-size: 18px;
    }

    /* Sidebar (Menu Bar on Left) */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 3px solid #6B46C1;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Top Header
st.markdown('<div class="top-header"><h1>ইলিশ কিনি</h1></div>', unsafe_allow_html=True)

# 4. Left Sidebar Navigation (Tomar chawa moto Bame)
with st.sidebar:
    st.markdown("<h2 style='color:#6B46C1 !important;'>মেনুবার</h2>", unsafe_allow_html=True)
    menu = st.radio("বিভাগ বেছে নিন:", ["🏠 হোম - দাম যাচাই", "📜 চাঁদপুরের পূর্ণ ইতিহাস", "🧬 পুষ্টি ও বিজ্ঞান", "📍 ঘাট লোকেশন"])
    st.markdown("---")
    st.markdown("Developed by **Sahib**")

# 5. Content Section
st.markdown('<div class="dsat-card">', unsafe_allow_html=True)

if menu == "🏠 হোম - দাম যাচাই":
    st.markdown("<h2 style='text-align:center;'>স্বাগতম আপনাকে</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>সঠিক দামে কিনুন <span class='highlight'>চাঁদপুরের ইলিশ</span></p>", unsafe_allow_html=True)
    
    size = st.selectbox("মাছের ওজন নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    prices = {"৫০০-৬০০ গ্রাম": 1150, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1950, "২ কেজি+": 2750}
    fair_price = prices[size]
    
    st.write(f"আজকের সঠিক বাজার দর: **{fair_price} ৳ (কেজি)**")
    user_p = st.number_input("বিক্রেতা কত দাম চাচ্ছে?", value=fair_price)
    
    if st.button("দাম যাচাই করুন"):
        if user_p > fair_price + 150:
            st.error(f"🚨 অতিরিক্ত {user_p - fair_price} টাকা বেশি চাচ্ছে!")
        else:
            st.success("✅ দাম একদম সঠিক আছে।")

elif menu == "📜 চাঁদপুরের পূর্ণ ইতিহাস":
    st.markdown("<h2 class='highlight'>ইলিশের রাজধানী চাঁদপুরের ইতিহাস</h2>", unsafe_allow_html=True)
    st.write("""
    চাঁদপুরকে বলা হয় 'ইলিশের বাড়ি'। পদ্মা, মেঘনা ও ডাকাতিয়া নদীর মিলনস্থলে লোনা ও মিষ্টি পানির সংমিশ্রণের কারণে এখানকার ইলিশের স্বাদ সারা বিশ্বে অতুলনীয়। 
    ১৮শ শতাব্দী থেকে চাঁদপুর মাছ ঘাট ইলিশ বাণিজ্যের প্রাণকেন্দ্র। প্রতি বছর এখান থেকে কয়েক হাজার টন মাছ সারা বিশ্বে রপ্তানি হয়।
    """)

elif menu == "🧬 পুষ্টি ও বিজ্ঞান":
    st.markdown("<h2 class='highlight'>কেন চাঁদপুরের ইলিশ সেরা?</h2>", unsafe_allow_html=True)
    st.write("""
    ১. **ওমেগা-৩:** এটি হার্টের ব্লকেজ প্রতিরোধ করে।
    ২. **মস্তিষ্কের মেধা:** শিশুদের মেধা বিকাশে অত্যন্ত কার্যকর।
    ৩. **ভিটামিন ডি:** হাড় মজবুত করে ও ক্যালসিয়াম বাড়ায়।
    ৪. **ত্বক ও চোখ:** চোখের জ্যোতি বাড়াতে সাহায্য করে।
    """)

elif menu == "📍 ঘাট লোকেশন":
    st.markdown("<h3 style='color:#6B46C1 !important;'>চাঁদপুর বড় স্টেশন মাছ ঘাট</h3>", unsafe_allow_html=True)
    st.markdown('<a href="https://maps.google.com/?q=Chandpur+Fish+Ghat" target="_blank" style="text-decoration:none;"><div style="background:#FF7A00; color:white; text-align:center; padding:15px; border-radius:12px; font-weight:bold;">গুগল ম্যাপে দেখুন</div></a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. Footer
st.markdown("<br><center><p style='color:#6B46C1 !important;'>© 2026 | Sahib's Project</p></center>", unsafe_allow_html=True) 
    
