import streamlit as st
import datetime

# ১. হাই-এন্ড অ্যাপ কনফিগারেশন
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="wide")

# ২. প্রফেশনাল সিএসএস (১ম পিকের মতো প্রিমিয়াম ডিজাইন)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600;800&family=Hind+Siliguri:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'SF Pro Display', 'Hind Siliguri', sans-serif;
        background-color: #FFFFFF;
        color: #1D1D1F;
    }

    /* সাইডবার প্রিমিয়াম লুক */
    [data-testid="stSidebar"] {
        background-color: #F5F5F7;
        border-right: 1px solid #D2D2D7;
    }
    
    /* বাম পাশের লোগো স্টাইল */
    .brand-logo {
        font-size: 26px; font-weight: 800; color: #000000;
        margin-bottom: 25px; border-left: 5px solid #007AFF; padding-left: 10px;
    }

    /* মেইন কার্ড */
    .premium-card {
        background: #FFFFFF; padding: 30px; border-radius: 20px;
        border: 1px solid #E5E5E7; box-shadow: 0 8px 30px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    /* ডাইনামিক বাটন */
    div.stButton > button:first-child {
        background: #007AFF; color: white !important;
        border-radius: 12px; height: 3.5em; width: 100%;
        font-weight: 700; border: none; transition: all 0.2s;
    }
    div.stButton > button:first-child:hover {
        background: #0051A8; transform: scale(1.01);
    }

    /* হেল্পলাইন বক্স */
    .call-box {
        background: #FFF2F2; padding: 25px; border-radius: 20px;
        border: 1px solid #FFC7C7; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. স্মার্ট প্রাইসিং লজিক (অটোমেটেড সিজনাল ডাটা)
month = datetime.datetime.now().month
is_off_season = month in [2, 3, 4, 5, 6] # এই মাসগুলোতে ইলিশ কম থাকে, দাম বেশি
status_text = "অফ-সিজন (দাম কিছুটা চড়া)" if is_off_season else "ভরা মৌসুম (দাম কম)"
multiplier = 1.35 if is_off_season else 1.0

# ৪. সাইডবার নেভিগেশন (১ম পিকের মতো প্রফেশনাল)
with st.sidebar:
    st.markdown('<div class="brand-logo">ইলিশ কিনি</div>', unsafe_allow_html=True)
    menu = st.radio("মেনু সিলেক্ট করুন", 
                    ["🏠 হোম / দাম চেক", "📍 ঘাট লোকেশন", "📜 ইতিহাস ও অর্থনীতি", "🩺 পুষ্টিগুণ", "📞 অভিযোগ কেন্দ্র"])
    st.markdown("---")
    lang = st.segmented_control("Language", ["বাংলা", "English"], default="বাংলা")

# ৫. হোম সেকশন: দাম যাচাই
if menu == "🏠 হোম / দাম চেক":
    st.markdown('<div class="brand-logo">ইলিশ কিনি</div>', unsafe_allow_html=True)
    
    st.markdown(f'<p style="color:#8E8E93; font-weight:600;">বর্তমান অবস্থা: {status_text}</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        size = st.selectbox("মাছের আকার", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
    
    # রিয়েলিস্টিক ডাটাবেজ
    base_price = {"৫০০-৬০০ গ্রাম": 950, "৭০০-৯০০ গ্রাম": 1100, "১ কেজি সাইজ": 1500, "১.৫ কেজি+": 1850, "২ কেজি+": 2600}
    fair_price = int(base_price[size] * multiplier)
    
    with c2:
        st.metric("সাজেস্টেড বাজার দর", f"{fair_price} ৳")

    user_ask = st.number_input("বিক্রেতা কত দাম চেয়েছে?", min_value=100, value=fair_price)
    
    if st.button("দাম যাচাই করুন"):
        if user_ask > fair_price + 200:
            st.error(f"⚠️ সাবধান! আপনি প্রতি কেজিতে প্রায় {user_ask - fair_price} টাকা বেশি দিচ্ছেন।")
            st.markdown("💡 **পরামর্শ:** চাঁদপুর মাছ ঘাটে গিয়ে যাচাই করুন, সেখানে দাম আরও কম পাবেন।")
        elif user_ask < fair_price - 50:
            st.balloons()
            st.success("✅ চমৎকার ডিল! এটি বর্তমান বাজারের সেরা দাম।")
        else:
            st.info("👌 দাম একদম স্বাভাবিক। আপনি নিশ্চিন্তে কিনতে পারেন।")
    st.markdown('</div>', unsafe_allow_html=True)

# ৬. লোকেশন সেকশন
elif menu == "📍 ঘাট লোকেশন":
    st.subheader("📍 চাঁদপুর বড় স্টেশন মাছ ঘাট")
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("এটি বাংলাদেশের বৃহত্তম ইলিশের পাইকারি বাজার। তাজা ইলিশের জন্য সরাসরি এখানে চলে যান।")
    st.markdown("""<a href="https://maps.app.goo.gl/3f6V4A89uY5N7YVj9" target="_blank">
    <button style="background:#4285F4; color:white; border:none; padding:12px 25px; border-radius:10px; cursor:pointer; font-weight:700;">
    গুগল ম্যাপসে লোকেশন দেখুন</button></a>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৭. ইতিহাস ও অনুবাদ (২য় পিকের ইন্সট্রাকশন অনুযায়ী)
elif menu == "📜 ইতিহাস ও অর্থনীতি":
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    if lang == "বাংলা":
        st.subheader("চাঁদপুর ও ইলিশের গৌরবগাথা")
        st.write("চাঁদপুরকে বলা হয় 'ইলিশের বাড়ি'। এখানকার পদ্মা-মেঘনা মোহনার রুপালি ইলিশ স্বাদে ও গন্ধে অতুলনীয়। ইলিশ রপ্তানি করে বাংলাদেশ প্রতি বছর ৩৫০-৪০০ মিলিয়ন ডলার বৈদেশিক মুদ্রা অর্জন করে। এটি আমাদের সংস্কৃতির এক অবিচ্ছেদ্য অংশ।")
    else:
        st.subheader("Legacy & Economy of Chandpur Hilsha")
        st.write("Chandpur is hailed as the 'Home of Hilsha'. The silver Hilsha from the Padma-Meghna estuary is unparalleled in taste. Exporting Hilsha contributes approximately $350-400 million in foreign exchange annually, making it a vital part of Bangladesh's economy.")
    st.markdown('</div>', unsafe_allow_html=True)

# ৮. পুষ্টিগুণ
elif menu == "🩺 পুষ্টিগুণ":
    st.subheader("🐟 কেন ইলিশ খাবেন?")
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.write("• **ওমেগা-৩ ফ্যাটি অ্যাসিড:** হার্ট ও মস্তিষ্কের জন্য উপকারী।\n• **ভিটামিন বি-১২:** রক্তকণিকা গঠনে সাহায্য করে।\n• **জিঙ্ক ও আয়োডিন:** রোগ প্রতিরোধ ক্ষমতা বাড়ায়।")
    st.markdown('</div>', unsafe_allow_html=True)

# ৯. অভিযোগ কেন্দ্র (সরাসরি কল)
elif menu == "📞 অভিযোগ কেন্দ্র":
    st.markdown('<div class="call-box">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#D32F2F;">ভোক্তা অধিকার সংরক্ষণ</h2>', unsafe_allow_html=True)
    st.write("ওজনে কারচুপি বা অতিরিক্ত দাম চাইলে সরাসরি কল করুন")
    st.markdown('<a href="tel:16121" style="text-decoration:none;"><h1 style="color:#D32F2F; font-size:60px;">16121</h1></a>', unsafe_allow_html=True)
    st.write("চাঁদপুর জেলা কার্যালয়")
    st.markdown('</div>', unsafe_allow_html=True)

# ১০. ফুটার (তোমার নামসহ)
st.markdown("---")
st.markdown("<center><p style='color:#8E8E93;'>🛡️ <b>ইলিশ কিনি</b> - স্বচ্ছ বাজার মুভমেন্ট<br>Developed by <b>Sahib</b></p></center>", unsafe_allow_html=True)
