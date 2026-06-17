import datetime
import json
import streamlit as st

st.set_page_config(page_title="Sanctuary | Your 2026 Sovereign Blueprint", layout="wide")

# =========================================================================
# 🌿 PART 1: HIGH-TRUST REYOU-INSPIRED DESIGN SYSTEM & DESIGN STYLES
# =========================================================================
st.markdown("""
<style>
    /* Global Low-Arousal Backdrop */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FAF6F0 !important; /* Soft warm sand baseline canvas */
        color: #2D3142 !important; /* Grounded Slate Text */
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    
    /* Low-Key Monochromatic Top Navigation Bar */
    .reyou-header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 25px 60px; background: #FAF6F0;
        border-bottom: 1px solid rgba(74, 107, 86, 0.05);
    }
    .reyou-logo {
        font-family: 'Playfair Display', serif; font-size: 20px;
        font-weight: 500; color: #3A4F41; letter-spacing: 1px;
    }
    .reyou-menu {
        display: flex; gap: 2.5rem; font-size: 13px; color: #6E7570; letter-spacing: 0.5px;
    }
    
    /* THE SIGNATURE REYOU TEAL-BLUE HERO VIEWPORT PANEL */
    .reyou-blue-hero-canvas {
        background-color: #3C5A5E !important; /* Premium Reyou therapeutic teal blue */
        background-image: url('https://unsplash.com'); /* Soft minimal silhouette portrait representation of a thoughtful lady */
        background-repeat: no-repeat;
        background-position: right 10% center;
        background-size: contain;
        padding: 100px 80px;
        margin: 20px 45px 40px 45px;
        border-radius: 32px;
        box-shadow: 0 20px 50px rgba(60, 90, 94, 0.15);
        color: #FFFFFF !important;
        position: relative;
        overflow: hidden;
    }
    /* Ambient glass overlay to smooth out photo edges */
    .reyou-blue-hero-canvas::after {
        content: ''; position: absolute; top:0; left:0; width:100%; height:100%;
        background: linear-gradient(90deg, #3C5A5E 40%, rgba(60, 90, 94, 0.2) 100%);
        z-index: 1; pointer-events: none;
    }
    .hero-content-wrapper { position: relative; z-index: 10; max-width: 580px; }
    .reyou-hero-tag {
        font-size: 11px; text-transform: uppercase; letter-spacing: 3px;
        color: #A3C1AD; margin-bottom: 25px; font-weight: 600;
    }
    .reyou-hero-h1 {
        font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 400;
        line-height: 1.3; color: #FFFFFF !important; margin-bottom: 25px; letter-spacing: -0.5px;
    }
    .reyou-hero-h1 span { font-style: italic; color: #E8F0EC; }
    .reyou-hero-p { font-size: 16px; color: #E8F0EC; line-height: 1.8; margin-bottom: 0px; opacity: 0.95; }
    
    /* Spacious Horizontal Story Blocks & Glass Cards */
    .reyou-card-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;
        padding: 20px 45px 60px 45px; max-width: 1300px; margin: 0 auto;
    }
    .reyou-sanctuary-card {
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.08);
        border-radius: 24px; padding: 40px 35px;
        box-shadow: 0 10px 40px rgba(74, 107, 86, 0.02);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .reyou-sanctuary-card:hover {
        transform: translateY(-4px);
        border-color: rgba(74, 107, 86, 0.2);
        box-shadow: 0 15px 45px rgba(74, 107, 86, 0.05);
    }
    .reyou-card-tag { font-size: 10px; text-transform: uppercase; letter-spacing: 2px; color: #A2A7A4; margin-bottom: 15px; }
    .reyou-card-title { font-family: 'Playfair Display', serif; font-size: 20px; color: #1F2421; margin-bottom: 15px; }
    .reyou-card-desc { font-size: 14px; color: #6E7570; line-height: 1.7; }
    .reyou-card-desc b { color: #1F2421; }

    /* Pure White Form Sanctuary Cards */
    .form-sanctuary-panel { 
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.12); 
        border-radius: 24px; padding: 40px; margin-bottom: 25px; 
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.01);
    }
    .form-panel-header { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #4A6B56; letter-spacing: 1.5px; margin-bottom: 25px; display: flex; align-items: center; gap: 8px; }
    .form-panel-dot { width: 7px; height: 7px; background: #4A6B56; border-radius: 50%; }
</style>
""", unsafe_allow_html=True)

# --- MOUNT SENSORY NAVIGATION HEAD ---
st.markdown("""
<div class="reyou-header">
    <div class="reyou-logo">reyou.space</div>
    <div class="reyou-menu">
        <span>Sanctuary</span>
        <span>The Narrative</span>
        <span>The Matrix</span>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================================
# 🧭 PART 2: THE SIGNATURE BLUE CANVAS HERO & 4-PANEL STORYBOARD
# =========================================================================
st.markdown("""
<div class="reyou-blue-hero-canvas">
    <div class="hero-content-wrapper">
        <div class="reyou-hero-tag">A Space for Intention</div>
        <div class="reyou-hero-h1">Take a breath. Let’s bring absolute clarity to your <span>2026 asset timeline.</span></div>
        <div class="reyou-hero-p">Mass-market seminars treat your retirement like a sterile calculation, leaving you to manage complex policy overhauls on your own. By translating shifting salary caps, interest tiers, and hidden rules into an intentional, personalized blueprint, we eliminate planning anxiety.</div>
    </div>
</div>

<div class="reyou-card-grid">
    <!-- PANEL 1 -->
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 01 // The Guesswork</div>
        <div class="reyou-card-title">Are You Planning in the Dark?</div>
        <div class="reyou-card-desc">Tracking a moving statutory target manually creates hidden friction. Following major changes, you face crucial parameters:<br><br>
        • <b>The $8,000 Ordinary Wage Ceiling:</b> The contribution cap has reached its final step. Are you optimized to capture this expanded inflow pool?<br>
        • <b>The 2026 Retirement Sums:</b> The Full Retirement Sum (FRS) has scaled to <b>$220,400</b>, directly altering your liquidity boundaries.<br>
        • <b>The SA Closure Shock:</b> For members aged 55 and above, the Special Account has officially closed. Excess balances now flow directly into the OA at a lower 2.5% yield unless structurally reallocated.</div>
    </div>
    <!-- PANEL 2 -->
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 02 // The Clarity</div>
        <div class="reyou-card-title">Your CPF Wealth Blueprint</div>
        <div class="reyou-card-desc">We turn raw account parameters and un-synthesized online statements into an elegant, visual roadmap built exclusively for your peace of mind:<br><br>
        • <b>Consolidated Flows:</b> Observe your Ordinary, Special, and Medisave Account streams side-by-side on a clean ledger panel.<br>
        • <b>Compounding Forecasts:</b> We compute your exact annual risk-free returns based on the extended 4% to 4.14% long-term floor rules.<br>
        • <b>Age 55 Vanguard Strategy:</b> A step-by-step map tracking how your Retirement Account (RA) will capitalize while protecting your withdrawable cash.</div>
    </div>
    <!-- PANEL 3 -->
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 03 // The Dream Gap</div>
        <div class="reyou-card-title">Insulate Your True Horizon</div>
        <div class="reyou-card-desc">Most high-earning individuals face a severe <b>"Monthly Shortfall"</b> between basic, automatic CPF LIFE annuity payouts and their preferred lifestyle standard.<br><br>
        Our diagnostic audit looks directly at your trajectory against the 2026 Enhanced Retirement Sum (ERS) limit of <b>$440,800</b>—showing you exactly how to optimize your positions to lock in the maximum possible lifelong monthly payouts.</div>
    </div>
</div>
""", unsafe_allow_html=True)
with col_form2:
    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot" style="background:#8D99AE; box-shadow:0 0 8px rgba(141,153,174,0.3);"></div>3. Housing Asset Outflows</div>', unsafe_allow_html=True)
    using_housing = st.radio("Are you currently utilizing CPF capital to service an active property loan?", ["Yes, actively executing outflows", "No, asset is unencumbered / cash funded"])
    
    if "Yes" in using_housing:
        housing_outflow = st.number_input("Monthly CPF Property Loan Withdrawal Amount ($)", min_value=0, value=2200, step=100)
        housing_years = st.number_input("Remaining Duration of Outstanding Loan (Years)", min_value=1, max_value=35, value=22, step=1)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot" style="background:#3A4F41; box-shadow:0 0 8px rgba(58,79,65,0.4);"></div>4. Consultation Environment</div>', unsafe_allow_html=True)
    preferred_date = st.date_input("Preferred Strategy Session Date", min_value=datetime.date.today(), value=datetime.date.today() + datetime.timedelta(days=3))
    consult_mode = st.radio("Choose a Consultation Space Style:", [
        "🌐 Low-Key Online Workspace (Zoom / Google Meet)",
        "☕ In-Person Private Boardroom Consultation (With Complimentary Starbucks Coffee)"
    ])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; padding: 10px 0 100px 0;">', unsafe_allow_html=True)
if st.button("Request My Calming 2026 Review Blueprint", type="primary"):
    if client_name and client_contact:
        st.success(f"✨ Allocation Sequence Initialized for {client_name}!")
        st.info(f"📌 Status: Your asset coordinates have been securely locked. Our office will reach out via WhatsApp at {client_contact} within 24 hours to confirm your private session for {preferred_date.strftime('%B %d, %Y')}. Your custom offline 2026 P&L Blueprint is now compiling.")
    else:
        st.error("🔒 Authentication Fault: Please complete your Name and WhatsApp Coordinate fields to authorize report compilation loops.")
st.markdown('</div>', unsafe_allow_html=True)
