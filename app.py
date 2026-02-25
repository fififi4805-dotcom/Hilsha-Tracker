import streamlit as st
import datetime

# ১. প্রফেশনাল কনফিগারেশন
st.set_page_config(page_title="ইলিশ কিনি | চাঁদপুর", page_icon="🐟", layout="wide")

# ২. আল্ট্রা-প্রিমিয়াম সিএসএস (iOS 17 & Material Design 3 স্টাইল)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Hind+Siliguri:wght@400;700&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', 'Hind Siliguri', sans-serif; }
    .stApp { background-color: #FFFFFF; color: #101828; }
    
    /* সাইডবার ডিজাইন */
    [data-testid="stSidebar"] {
        background-color: #F9FAFB;
        border-right: 1px solid #EAECF0;
        padding-top: 20px;
    }
    
    /* লোগো ও ব্র্যান্ডিং */
    .nav-brand {
        font-size: 24px; font-weight: 800; color: #004EEB;
        padding: 10px 20px; border-radius: 12px;
        background: #EFF4FF; display: inline-block; margin-bottom: 30px;
    }

    /* মেইন কার্ড - গ্রাসমর্ফিজম টাচ */
    .stat-card {
        background: #FFFFFF; padding: 25px; border-radius: 20px;
        border: 1px solid #F2F4F7; box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        transition: 0.3s;
    }
    .stat-card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.08); }

    /* ইনপুট ফিল্ডস */
    .stSelectbox, .stNumberInput { margin-bottom: 20px; }

    /* প্রিমিয়াম বাটন */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #004EEB 0%, #0035A1 100%);
        color: white !important; border-radius: 12px;
        height: 3.8em; width: 100%; font-weight: 700;
        font-size: 16px; border: none; box-shadow: 0 4px 14px rgba(0, 78, 235, 0.25);
    }
    
    /* ব্যাজ */
    .badge {
        padding: 4px 12px; border-radius: 50px; font-size: 12px; font-weight: 600;
        background: #ECFDF3; color: #027A48; border: 1px solid #ABEFC6;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. ডাইনামিক প্রাইসিং ও সিজন লজিক
month = datetime.datetime.now().month
month_name = datetime.datetime.now().strftime("%B")
is_peak = 8 <= month <= 10  # আগস্ট-অক্টোবর
season_status = "ভরা মৌসুম (দাম কম)" if is_peak else "অফ-সিজন (দাম চড়া)"
price_factor = 1.0 if is_peak else 1.35

# ৪. সাইডবার নেভিগেশন
with st.sidebar:
    st.markdown('<div class="nav-brand">🐟 ইলিশ কিনি</div>', unsafe_allow_html=True)
    menu = st.radio("সরাসরি যান", ["📊 ড্যাশবোর্ড", "🗺️ ঘাট ম্যাপ", "🌍 ইতিহাস ও রপ্তানি", "💊 পুষ্টি ও স্বাস্থ্য", "🚨 হেল্পলাইন"])
    st.markdown("---")
    st.markdown("### 🌐 ভাষা / Language")
    lang = st.radio("সিলেক্ট করুন", ["বাংলা", "English"], horizontal=True)

# ৫. ড্যাশবোর্ড: স্মার্ট ক্যালকুলেটর
if menu == "📊 ড্যাশবোর্ড":
    st.markdown(f'<h1 style="color:#101828;">হ্যালো সাহেব! 👋</h1>', unsafe_allow_html=True)
    st.markdown(f'<span class="badge">📅 {month_name} - {season_status}</span>', unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top:25px;"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.subheader("🔍 বাজার দর যাচাই")
        fish_size = st.selectbox("মাছের সাইজ বেছে নিন", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.৫ কেজি+", "২ কেজি+"])
        
        base_data = {"৫০০-৬০০ গ্রাম": 950, "৭০০-৯০০ গ্রাম": 1150, "১ কেজি সাইজ": 1550, "১.৫ কেজি+": 1900, "২ কেজি+": 2700}
        current_fair_price = int(base_data[fish_size] * price_factor)
        
        user_ask = st.number_input("বিক্রেতা কত দাম চাচ্ছে? (টাকা/কেজি)", min_value=100, value=current_fair_price)
        
        if st.button("রেজাল্ট দেখুন"):
            diff = user_ask - current_fair_price
            if diff > 150:
                st.error(f"🚨 অতিরিক্ত দাম! আপনি প্রতি কেজিতে {diff} টাকা বেশি দিচ্ছেন।")
            elif diff < -50:
                st.success("✅ এটি একটি গোল্ডেন ডিল! আপনি সাশ্রয়ী দামে কিনছেন।")
                st.balloons()
            else:
                st.info("👌 দাম ঠিক আছে। আপনি কিনতে পারেন।")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.subheader("💡 টিপস")
        st.write("• চাঁদপুর ঘাটে ভোরে গেলে সবচেয়ে তাজা মাছ পাওয়া যায়।")
        st.write("• বরফ ছাড়া মাছ কেনার চেষ্টা করুন, স্বাদ বেশি পাবেন।")
        st.write("• লালচে কানকো দেখে কিনবেন।")
        st.markdown('</div>', unsafe_allow_html=True)

# ৬. ম্যাপ ও লোকেশন
elif menu == "🗺️ ঘাট ম্যাপ":
    st.subheader("📍 চাঁদপুর বড় স্টেশন মাছ ঘাট")
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.write("বিশ্বখ্যাত চাঁদপুরের ইলিশের প্রধান আড়ত।")
    st.markdown("""<a href="https://www.google.com/maps/search/Chandpur+Fish+Ghat" target="_blank">
    <button style="background:#004EEB; color:white; border:none; padding:15px 25px; border-radius:10px; cursor:pointer; font-weight:700; width:100%;">
    গুগল ম্যাপে ওপেন করুন</button></a>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৭. ইতিহাস ও অনুবাদ
elif menu == "🌍 ইতিহাস ও অর্থনীতি":
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    if lang == "বাংলা":
        st.subheader("চাঁদপুরের ইলিশের অর্থনীতি")
        st.write("চাঁদপুরকে বলা হয় 'ইলিশের বাড়ি'। মেঘনা-পদ্মার পানির লবণাক্ততা ও প্রবাহের কারণে এখানকার মাছ সবচেয়ে সুস্বাদু। প্রতি বছর বাংলাদেশ প্রায় ৩৫০ মিলিয়ন ডলারের ইলিশ রপ্তানি করে, যার বড় অংশই চাঁদপুরের আড়ত থেকে সংগৃহীত হয়।")
    else:
        st.subheader("Economy of Chandpur Hilsha")
        st.write("Chandpur is hailed as the 'Home of Hilsha'. The unique salinity and flow of the Meghna-Padma estuary make these fish the tastiest. Bangladesh exports approximately $350 million worth of Hilsha annually, with a huge portion sourced from Chandpur's markets.")
    st.markdown('</div>', unsafe_allow_html=True)

# ৮. হেল্পলাইন
elif menu == "🚨 হেল্পলাইন":
    st.markdown('<div style="background:#FEF3F2; padding:40px; border-radius:24px; text-align:center; border:1px solid #FEE4E2;">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#B42318;">ভোক্তা অধিকার চাঁদপুর</h2>', unsafe_allow_html=True)
    st.write("অতিরিক্ত দাম বা ওজনে কারচুপি হলে সরাসরি কল করুন")
    st.markdown('<a href="tel:16121" style="text-decoration:none;"><h1 style="color:#B42318; font-size:64px; margin:20px 0;">16121</h1></a>', unsafe_allow_html=True)
    st.markdown('<span class="badge" style="background:#FEE4E2; color:#B42318;">কল খরচ ফ্রি</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৯. ফুটার
st.markdown("---")
st.markdown("<center><p style='color:#667085; font-size:14px;'>🛡️ <b>ইলিশ কিনি v3.0</b><br>Developed by <b>Sahib</b></p></center>", unsafe_allow_html=True)    
    
