import streamlit as st

# 1. Google Standard Page Config
st.set_page_config(page_title="Elish Kini Pro", page_icon="🐟", layout="centered")

# 2. Ultra-Premium Dark Theme (Shikho/3rd Pic Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&display=swap');
    
    /* Main Background - Midnight Dark Blue */
    .stApp {
        background-color: #0F172A !important;
        font-family: 'Hind Siliguri', sans-serif !important;
    }

    /* Sidebar Dark Look */
    [data-testid="stSidebar"] {
        background-color: #1E293B !important;
        border-right: 1px solid #334155;
    }

    /* 3rd Pic-er moto Shada Font */
    h1, h2, h3, p, span, label, b, li {
        color: #FFFFFF !important;
    }

    /* Custom Top Header with 3-Dash Menu Icon */
    .custom-nav {
        background: #1E293B;
        padding: 15px 20px;
        border-radius: 15px;
        border: 1px solid #334155;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }
    .brand { font-size: 22px; font-weight: 700; color: #A855F7 !important; }
    .hamburger { font-size: 24px; color: #FFFFFF !important; cursor: pointer; }

    /* Shikho Style Data Cards */
    .shikho-card {
        background: #1E293B;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #334155;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    /* Neon Highlights */
    .neon-purple { color: #A855F7 !important; font-weight: 700; }
    .neon-blue { color: #38BDF8 !important; font-weight: 700; }
    .neon-orange { color: #F59E0B !important; font-weight: 700; }

    /* Button Style */
    div.stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%) !important;
        color: white !important;
        border-radius: 12px;
        height: 3.5em; width: 100%; border: none; font-weight: 700;
        font-size: 16px;
    }

    /* Input Box Dark Mode Protection */
    div[data-baseweb="select"] > div, input {
        background-color: #0F172A !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }

    /* Sidebar text fix */
    .css-17l2qt2 { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Functional Header with 3-Dash Hint
st.markdown("""
    <div class="custom-nav">
        <div class="brand">Shikho Elish 🐟</div>
        <div class="hamburger">☰</div>
    </div>
    """, unsafe_allow_html=True)

# 4. Sidebar Menu
with st.sidebar:
    st.markdown("<h2 class='neon-purple'>Main Menu</h2>", unsafe_allow_html=True)
    menu = st.radio("Choose Section:", [
        "📊 Bazar Report", 
        "⚖️ Price Checker", 
        "💡 Secret Buying Tips",
        "📞 Complain Box"
    ])
    st.markdown("---")
    st.write("Senior Dev: **Sahib**")

# 5. Content Section
if menu == "📊 Bazar Report":
    st.markdown("<h2 class='neon-blue'>Chandpur Elish Report 2026</h2>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="shikho-card">
            <p style="color:#94A3B8 !important; margin:0;">Export (Annual)</p>
            <h2 class="neon-orange" style="margin:5px 0;">52,000+ Ton</h2>
            <p style="font-size:12px; color:#94A3B8 !important;">India & Europe</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="shikho-card">
            <p style="color:#94A3B8 !important; margin:0;">Govt Revenue</p>
            <h2 class="neon-purple" style="margin:5px 0;">125cr+ BDT</h2>
            <p style="font-size:12px; color:#94A3B8 !important;">From Chandpur Zone</p>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("<div class='shikho-card'>", unsafe_allow_html=True)
    st.markdown("<h3 class='neon-blue'>Business Summary</h3>", unsafe_allow_html=True)
    st.write("Chandpur ghat theke protidin pray 800-1200 mon elish nationwide supply hoy. Peak season-e ekhane dainik 10-15 koti takar transaction hoy.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "⚖️ Price Checker":
    st.markdown("<div class='shikho-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='neon-purple'>Smart Price Detector</h2>", unsafe_allow_html=True)
    
    size = st.selectbox("Select Size:", ["500-600g", "1KG Size", "1.5KG+", "2KG+"])
    prices = {"500-600g": 1150, "1KG Size": 1550, "1.5KG+": 1950, "2KG+": 2750}
    fair_price = prices[size]
    
    st.write(f"Official Avg Price: **{fair_price} ৳**")
    user_p = st.number_input("Seller Asking Price:", value=int(fair_price))
    
    if st.button("Check Result"):
        if user_p > fair_price + 150:
            st.error(f"🚨 Too High! Extra {user_p - fair_price} BDT asked.")
        else:
            st.success("✅ Price is fair. You can buy!")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "💡 Secret Buying Tips":
    st.markdown("<h2 class='neon-orange'>How to Identify Fresh Elish</h2>", unsafe_allow_html=True)
    st.markdown("""<div class='shikho-card'>
        <p><b>1. Belly Test:</b> Pet-e chap dile jodi mukh diye dim ber hoy, bujhben mach norom. Shokto pet-er mach kinun.</p>
        <p><b>2. Silver Glow:</b> Fresh elish aynar moto chokchok korbe. Chokh jodi lal hoye thake, oita niben na.</p>
        <p><b>3. Mohonar Garon:</b> Chandpur-er mohonar mach ektu gol-gal (potka) hoy ar lej-er dikta shoru hoy.</p>
        <p><b>4. Gills (Fulkha):</b> Fulkha jodi tok-toke lal hoy tobe oita fresh. Kalche fulkha mane purono mach.</p>
    </div>""", unsafe_allow_html=True)

elif menu == "📞 Complain Box":
    st.markdown("<div class='shikho-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<h2 class='neon-purple'>Consumer Rights Hotline</h2>", unsafe_allow_html=True)
    st.write("Jodi kono seller dhoka dey, call korun:")
    st.markdown("<h1 style='color:#F59E0B !important; font-size:60px; margin:10px 0;'>16121</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Footer
st.markdown("<center><p style='color:#64748B; font-size:12px; margin-top:50px;'>© 2026 Elish Pro | Senior Dev: Sahib</p></center>", unsafe_allow_html=True)        
