  import streamlit as st
import datetime

# ১. DSAT School এর মতো ক্লিন সেটআপ
st.set_page_config(page_title="ইলিশ কিনি", page_icon="🐟", layout="wide")

# ২. আল্ট্রা-প্রিমিয়াম হোয়াইট ও অরেঞ্জ থিম (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;800&family=Hind+Siliguri:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Public Sans', 'Hind Siliguri', sans-serif;
        background-color: #FFFFFF;
        color: #2D3748;
    }
    
    /* ব্যাকগ্রাউন্ড সাদা করা */
    .stApp { background-color: #FFFFFF; }

    /* টপ বার ও লোগো (DSAT School Style) */
    .top-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 5%; border-bottom: 1px solid #EDF2F7;
        background: #FFFFFF; position: sticky; top: 0; z-index: 99;
    }
    .brand-name {
        font-size: 28px; font-weight: 800; color: #1A202C;
    }
    .brand-name span { color: #FF7A00; }

    /* মেইন কার্ড ডিজাইন */
    .content-card {
        background: #FFFFFF; padding: 30px; border-radius: 20px;
        border: 1px solid #F1F5F9; box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        margin-top: 20px;
    }

    /* বাটন ডিজাইন (DSAT এর অরেঞ্জ বাটন) */
    div.stButton > button:first-child {
        background: #FF7A00; color: white !important;
        border-radius: 10px; height: 3.8em; width: 100%;
        font-weight: 700; border: none; font-size: 16px;
        transition: 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background: #E66E00; box-shadow: 0 5px 15px rgba(255,122,0,0.3);
    }

    /* সাইডবার (ডান পাশের মেনু ইফেক্ট) */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF; border-left: 1px solid #EDF2F7;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. মেইন হেডার (DSAT এর মতো লোগো ও মেনু আইকন)
st.markdown(f"""
    <div class="top-nav">
        <div class="brand-name">ইলি<span>শ কিনি</span></div>
        <div style="font-size: 24px; color: #4A5568;">☰</div>
    </div>
    """, unsafe_allow_html=True)

# ৪. ডাইনামিক প্রাইসিং লজিক (অটো আপডেট)
month = datetime.datetime.now().month
is_off_season = month in [2, 3, 4, 5, 6]
season_multiplier = 1.35 if is_off_season else 1.0

# ৫. সাইডবার মেনুবার (১ম পিকের মতো বাম পাশে ৩ ড্যাশ কন্ট্রোল)
with st.sidebar:
    st.markdown("### 📑 মেনুবার")
    menu = st.radio("অপশন বেছে নিন", ["🏠 হোম", "📍 ঘাট ম্যাপ", "📜 ইতিহাস ও রপ্তানি", "🩺 উপকারিতা", "📞 অভিযোগ"])
    st.markdown("---")
    lang = st.segmented_control("Language", ["বাংলা", "English"], default="বাংলা")

# ৬. ড্যাশবোর্ড কন্টেন্ট
if menu == "🏠 হোম":
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("## 💰 আজকের বাজার দর চেক")
    
    fish_size = st.selectbox("মাছের সাইজ নির্বাচন করুন", ["৫০০-৬০০ গ্রাম", "৭০০-৯০০ গ্রাম", "১ কেজি সাইজ", "১.১ - ১.৫ কেজি", "২ কেজি বা বেশি"])
    
    # প্রাইস ডাটাবেজ
    prices = {"৫০০-৬০০ গ্রাম": 1150, "৭০০-৯০০ গ্রাম": 1200, "১ কেজি সাইজ": 1450, "১.১ - ১.৫ কেজি": 1600, "২ কেজি বা বেশি": 1850}
    fair_price = int(prices[fish_size] * season_multiplier)
    
    st.metric("সঠিক বাজার মূল্য (কেজি)", f"{fair_price} ৳", delta="অফ-সিজন" if is_off_season else "ভরা মৌসুম")
    
    user_price = st.number_input("বিক্রেতা কত দাম চাচ্ছে?", min_value=100, value=fair_price)
    
    if st.button("চেক করুন"):
        diff = user_price - fair_price
        if diff > 150:
            st.error(f"🚨 সাবধান! আপনি প্রতি কেজিতে {diff} টাকা বেশি দিচ্ছেন। দরদাম করুন।")
        else:
            st.success("✅ এটি একদম সঠিক দাম। আপনি নিশ্চিন্তে কিনতে পারেন।")
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# ৭. ঘাট ম্যাপ (১০০% কাজ করবে এমন লিঙ্ক)
elif menu == "📍 ঘাট ম্যাপ":
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.subheader("📍 চাঁদপুর বড় স্টেশন মাছ ঘাট")
    st.write("সরাসরি মাছ ঘাট যাওয়ার জন্য নিচের বাটনে ক্লিক করুন:")
    # চাঁদপুর বড় স্টেশন মাছ ঘাটের ডিরেক্ট গুগল ম্যাপস লিঙ্ক
    map_url = "https://www.google.com/maps/dir//Chandpur+Fishery+Ghat,+Chandpur/"
    st.markdown(f"""
        <a href="{map_url}" target="_blank" style="text-decoration:none;">
            <div style="background:#4285F4; color:white; text-align:center; padding:15px; border-radius:10px; font-weight:bold;">
                Google Maps এ লোকেশন দেখুন
            </div>
        </a>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ৮. ইতিহাস ও অর্থনীতি (বাংলা/ইংরেজি অনুবাদ)
elif menu == "📜 ইতিহাস ও রপ্তানি":
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    if lang == "বাংলা":
        st.subheader("চাঁদপুরের ইলিশের ইতিহাস")
        st.write("চাঁদপুর হলো ইলিশের রাজধানী। পদ্মা-মেঘনা-ডাকাতিয়ার মিলনস্থলের ইলিশের স্বাদই আলাদা। প্রতি বছর বাংলাদেশ কয়েক হাজার কোটি টাকার ইলিশ রপ্তানি করে, যার বড় যোগান আসে চাঁদপুর থেকে।")
    else:
        st.subheader("Economy of Chandpur Hilsha")
        st.write("Chandpur is known as the 'Home of Hilsha'. Due to the unique water properties of the Padma-Meghna estuary, these fish are the tastiest. Bangladesh earns massive foreign currency through Hilsha exports.")
    st.markdown('</div>', unsafe_allow_html=True)

# ৯. উপকারিতা
elif menu == "🩺 উপকারিতা":
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.subheader("🐟 কেন ইলিশ খাবেন?")
    st.write("• হার্ট সুস্থ রাখে (Omega-3 fatty acids)।\n• ব্রেইন ডেভেলপমেন্টে সাহায্য করে।\n• প্রচুর আয়োডিন ও সেলেনিয়াম সমৃদ্ধ।")
    st.markdown('</div>', unsafe_allow_html=True)

# ১০. অভিযোগ (Call Function)
elif menu == "📞 অভিযোগ":
    st.markdown('<div style="background:#FFF5F5; padding:40px; border-radius:20px; text-align:center; border:1px solid #FEB2B2; margin-top:20px;">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#C53030;">ভোক্তা অধিকার চাঁদপুর</h2>', unsafe_allow_html=True)
    st.write("অতিরিক্ত দাম চাইলে সরাসরি কল করুন")
    st.markdown('<a href="tel:16121" style="text-decoration:none;"><h1 style="color:#C53030; font-size:60px;">📞 16121</h1></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ১১. ফুটার (Sahib Branding)
st.markdown("---")
st.markdown("<center><p style='color:#A0AEC0; font-size:14px;'>Developed by <b>Sahib</b><br>© 2026 Elish Kini Project</p></center>", unsafe_allow_html=True)  
