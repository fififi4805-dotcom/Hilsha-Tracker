import streamlit as st

# ১. পেজ সেটআপ
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="wide")

# ২. DSAT School স্টাইল (White background, Purple border, Orange text)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@700;900&family=Hind+Siliguri:wght@700&display=swap');
html, body, [class*="css"] { font-family: 'Public Sans', 'Hind Siliguri', sans-serif; background-color: #FFFFFF !important; }
.stApp { background-color: #FFFFFF; }

/* টপ বার ব্র্যান্ডিং */
.header-box { display: flex; justify-content: space-between; align-items: center; padding: 15px 5%; border-bottom: 2px solid #6B46C1; }
.logo-title { font-size: 28px; font-weight: 900; color: #6B46C1; }

/* কমলা টেক্সট ও পার্পল বর্ডার কার্ড */
.orange-head { color: #FF7A00 !important; font-weight: 900; text-align: center; }
.purple-card { border: 2px solid #6B46C1; border-radius: 15px; padding: 20px; background: #FFFFFF; margin-bottom: 20px; }

/* বাটন ডিজাইন */
div.stButton > button:first-child { background-color: #6B46C1; color: white !important; border-radius: 50px; border: none; width: 100%; font-weight: 700; height: 3.5em; }
.map-btn { background-color: #FF7A00; color: white; padding: 15px; border-radius: 50px; text-align: center; display: block; text-decoration: none; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# ৩. টপ ব্র্যান্ডিং (DSAT স্টাইল)
st.markdown('<div class="header-box"><div class="logo-title">ইলিশ কিনি</div><div style="font-size:24px; color:#6B46C1;">☰</div></div>', unsafe_allow_html=True)

# ৪. সাইডবার মেনু
with st.sidebar:
    st.markdown("<h2 style='color:#6B46C1;'>📂 মেনুবার</h2>", unsafe_allow_html=True)
    choice = st.selectbox("বেছে নিন:", ["🏠 হোম - বাজার দর", "📍 মাছ ঘাট লোকেশন", "📜 ইতিহাস", "📞 অভিযোগ কেন্দ্র"])
    st.markdown("---")
    st.write("Developed by **Sahib**")

# ৫. মেইন কন্টেন্ট
st.markdown("<br><h1 class='orange-head'>স্বাগতম আপনাকে</h1>", unsafe_allow_html=True)

if choice == "🏠 হোম - বাজার দর":
    st.markdown('<div class="purple-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#FF7A00;'>💰 সঠিক দাম যাচাই করুন</h3>", unsafe_allow_html=True)
    size = st.selectbox("মাছের আকার", ["৫০০-৬০০ গ্রাম", "১ কেজি", "১.৫ কেজি+", "২ কেজি+"])
    prices = {"৫০০-৬০০ গ্রাম": 1150, "১ কেজি": 1500, "১.৫ কেজি+": 1900, "২ কেজি+": 2700}
    fair = prices[size]
    st.write(f"সঠিক বাজার দর: {fair} ৳")
    user_p = st.number_input("বিক্রেতার দাম", value=fair)
    if st.button("চেক করুন"):
        if user_p > fair + 100:
            st.error(f"অতিরিক্ত {user_p - fair} টাকা চাচ্ছে!")
        else:
            st.success("দাম ঠিক আছে।")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

elif choice == "📍 মাছ ঘাট লোকেশন":
    st.markdown('<div class="purple-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#FF7A00;'>📍 চাঁদপুর বড় স্টেশন মাছ ঘাট</h3>", unsafe_allow_html=True)
    st.write("সরাসরি লোকেশন দেখতে নিচের বাটনে ক্লিক করুন:")
    st.markdown('<a href="https://www.google.com/maps/search/Chandpur+Hilsa+Ghat" target="_blank" class="map-btn">গুগল ম্যাপে দেখুন</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif choice == "📜 ইতিহাস":
    st.markdown('<div class="purple-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#FF7A00;'>ইলিশের বাড়ি চাঁদপুর</h3>", unsafe_allow_html=True)
    st.write("চাঁদপুরের পদ্মা-মেঘনার মোহনার ইলিশ পৃথিবীর শ্রেষ্ঠ।")
    st.markdown('</div>', unsafe_allow_html=True)

elif choice == "📞 অভিযোগ কেন্দ্র":
    st.markdown('<div class="purple-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<h2 style='color:#6B46C1;'>ভোক্তা অধিকার</h2>", unsafe_allow_html=True)
    st.markdown("<a href='tel:16121' style='text-decoration:none;'><h1 style='color:#FF7A00; font-size:50px;'>16121</h1></a>", unsafe_allow_html=True)
    st.write("কল করুন (টোল ফ্রি)")
    st.markdown('</div>', unsafe_allow_html=True)

# ৬. ফুটার
st.markdown("<center><p style='color:#6B46C1;'>Developed by <b>Sahib</b></p></center>", unsafe_allow_html=True)          
