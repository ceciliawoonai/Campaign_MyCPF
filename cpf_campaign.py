import datetime
import streamlit as st

st.set_page_config(page_title="Sanctuary | Your 2026 Sovereign Space", layout="wide")

# --- REYOU-INSPIRED INTENTIONAL SANCTUARY CSS FRAMEWORK ---
st.markdown("""
<style>
    /* Global Calm Layer */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FAF6F0 !important; /* Soft sand canvas */
        color: #2D3142 !important; /* Grounded slate text */
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    
    /* Low-Arousal Monochromatic Header */
    .reyou-header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 25px 60px; background: #FAF6F0;
    }
    .reyou-logo {
        font-family: 'Playfair Display', serif; font-size: 20px;
        font-weight: 500; color: #3A4F41; letter-spacing: 1px;
    }
    .reyou-menu {
        display: flex; gap: 2.5rem; font-size: 13px; color: #6E7570; letter-spacing: 0.5px;
    }
    
    /* High-Empathy Minimal Hero Section */
    .reyou-hero {
        text-align: center; padding: 90px 45px 60px 45px; max-width: 800px; margin: 0 auto;
    }
    .reyou-hero-tag {
        font-size: 11px; text-transform: uppercase; letter-spacing: 3px;
        color: #8D99AE; margin-bottom: 25px; font-weight: 600;
    }
    .reyou-hero-h1 {
        font-family: 'Playfair Display', serif; font-size: 42px; font-weight: 400;
        line-height: 1.3; color: #1F2421; margin-bottom: 25px; letter-spacing: -0.5px;
    }
    .reyou-hero-h1 span { font-style: italic; color: #4A6B56; }
    .reyou-hero-p { font-size: 16px; color: #6E7570; line-height: 1.8; margin-bottom: 40px; }
    
    /* Spacious Interactive Story Blocks */
    .reyou-card-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;
        padding: 20px 60px 60px 60px; max-width: 1200px; margin: 0 auto;
    }
    .reyou-sanctuary-card {
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.08);
        border-radius: 24px; padding: 40px 35px;
        box-shadow: 0 10px 40px rgba(74, 107, 86, 0.02);
        transition: all 0.4s ease;
    }
    .reyou-card-tag { font-size: 10px; text-transform: uppercase; letter-spacing: 2px; color: #A2A7A4; margin-bottom: 15px; }
    .reyou-card-title { font-family: 'Playfair Display', serif; font-size: 20px; color: #1F2421; margin-bottom: 15px; }
    .reyou-card-desc { font-size: 14px; color: #6E7570; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)

# --- MOUNT THE BRAND CONSOLE NAVIGATION BAR ---
st.markdown("""
<div class="reyou-header">
    <div class="reyou-logo">reyou.space</div>
    <div class="reyou-menu">
        <span>Sanctuary</span>
        <span>The Blueprint</span>
        <span>The Matrix</span>
    </div>
</div>
""", unsafe_allow_html=True)
# --- MOUNT THE HIGH-EMPATHY HERO & ROADMAP CARDS ---
st.markdown("""
<div class="reyou-hero">
    <div class="reyou-hero-tag">A Space for Intention</div>
    <div class="reyou-hero-h1">Take a breath. Let’s bring clarity to your <span>2026 asset timeline.</span></div>
    <div class="reyou-hero-p">The shifting sovereign landscape doesn’t have to feel overwhelming. By translating complex institutional rules, rising salary caps, and financial thresholds into an intentional, visual roadmap, we replace planning anxiety with total peace of mind.</div>
</div>

<div class="reyou-card-grid">
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 01 // The Fog</div>
        <div class="reyou-card-title">Clear the Moving Targets</div>
        <div class="reyou-card-desc">Tracking the upcoming $8,000 wage ceilings and senior contribution adjustments manually creates unnecessary worry. We clear the fog by mapping these parameters for you quietly.</div>
    </div>
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 02 // The Roadmap</div>
        <div class="reyou-card-title">An Intentional Blueprint</div>
        <div class="reyou-card-desc">We consolidate your raw allocation balances into a clean, easy-to-read ledger panel. No dense tables or complex jargon—just an elegant, accurate summary of your true growth path.</div>
    </div>
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 03 // The Horizon</div>
        <div class="reyou-card-title">Insulate Your Lifestyle</div>
        <div class="reyou-card-desc">We analyze your parameters against the 2026 Enhanced Retirement Sum ($440,800) to safely bridge any monthly gaps, securing your target lifestyle horizons effortlessly.</div>
    </div>
</div>
""", unsafe_allow_html=True)
# --- MOUNT THE SECURE ENCRYPTED DATA ENTRY SPACE ---
st.markdown("""
<div style="text-align:center; padding:40px 45px 10px 45px; max-width:700px; margin:0 auto;">
    <h3 style="font-family:'Playfair Display', serif; font-size:26px; font-weight:400; color:#1F2421;">Secure Your Private Review Space</h3>
    <p style="font-size:14px; color:#6E7570; margin-bottom:30px;">Your entries remain completely protected. We compile your personalized 2026 roadmap entirely offline in our diagnostic engine to share exclusively during your consultation session.</p>
</div>
""", unsafe_allow_html=True)

# Two column pure white field elements
f_col1, f_col2 = st.columns(2, gap="large")

with f_col1:
    st.text_input("Full Professional Name")
    st.text_input("WhatsApp Mobile Coordinate")
    st.slider("Current Age Model", min_value=20, max_value=99, value=38)
    st.number_input("Total Monthly Gross Ordinary Wage ($)", min_value=1000, value=8500, step=500)

with f_col2:
    st.number_input("Ordinary Account (OA) Balance ($)", min_value=0, value=95000, step=5000)
    st.number_input("Special Account (SA) Balance ($)", min_value=0, value=70000, step=5000)
    
    st.markdown('<div style="margin-top:15px;"></div>', unsafe_allow_html=True)
    preferred_date = st.date_input("Select a Preferred Strategy Date", min_value=datetime.date.today(), value=datetime.date.today() + datetime.timedelta(days=3))
    
    consult_mode = st.radio("Choose a Consultation Environment Style:", [
        "🌐 Low-Key Online Session (Zoom / Google Meet)",
        "☕ In-Person Private Boardroom Catch-Up (With Complimentary Starbucks Coffee)"
    ])

st.markdown('<div style="text-align:center; padding: 40px 0 100px 0;">', unsafe_allow_html=True)
if st.button("Request My Calming 2026 Review Blueprint", type="primary"):
    st.success("✨ Your request has been securely compiled. Cecilia's office will connect with you via WhatsApp within 24 hours to confirm your private sanctuary consultation details.")
st.markdown('</div>', unsafe_allow_html=True)
