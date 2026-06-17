import datetime
import json
import streamlit as st

st.set_page_config(page_title="Sanctuary | Your 2026 Sovereign Blueprint", layout="wide")

# =========================================================================
# 🌿 REYOU-INSPIRED HIGH-TRUST SANCTUARY DESIGN STYLES SHEET
# =========================================================================
st.markdown("""
<style>
    /* Global Low-Arousal Calm Canvas */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FAF6F0 !important; /* Soft warm sand canvas backdrop */
        color: #2D3142 !important; /* Grounded slate typography */
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    
    /* Elegant Minimal Navigation Bar Row */
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
    
    /* THE SIGNATURE REYOU TEAL-BLUE HERO GRID CANVAS */
    .reyou-blue-hero-canvas {
        background-color: #2F4A4E !important; /* Premium Reyou therapeutic teal blue */
        padding: 80px;
        margin: 20px 45px 40px 45px;
        border-radius: 32px;
        box-shadow: 0 20px 50px rgba(47, 74, 78, 0.15);
        color: #FFFFFF !important;
    }
    .hero-content-wrapper { max-width: 600px; }
    .reyou-hero-tag {
        font-size: 11px; text-transform: uppercase; letter-spacing: 3px;
        color: #A3C1AD; margin-bottom: 25px; font-weight: 600;
    }
    .reyou-hero-h1 {
        font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 400;
        line-height: 1.3; color: #FFFFFF !important; margin-bottom: 25px; letter-spacing: -0.5px;
    }
    .reyou-hero-p { font-size: 16px; color: #E8F0EC; line-height: 1.8; margin-bottom: 0px; opacity: 0.95; }
    
    /* Spacious Horizontal Story Blocks & Glass Cards Layout */
    .reyou-card-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;
        padding: 20px 45px 60px 45px; max-width: 1300px; margin: 0 auto;
    }
    .reyou-sanctuary-card {
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.08);
        border-radius: 24px; padding: 40px 35px;
        box-shadow: 0 10px 40px rgba(74, 107, 86, 0.02);
        transition: all 0.4s ease;
    }
    .reyou-sanctuary-card:hover {
        transform: translateY(-4px);
        border-color: rgba(74, 107, 86, 0.2);
        box-shadow: 0 15px 45px rgba(74, 107, 86, 0.05);
    }
    .reyou-card-tag { font-size: 10px; text-transform: uppercase; letter-spacing: 2px; color: #A2A7A4; margin-bottom: 15px; }
    .reyou-card-title { font-family: 'Playfair Display', serif; font-size: 20px; color: #1F2421; margin-bottom: 15px; }
    .reyou-card-desc { font-size: 14px; color: #6E7570; line-height: 1.7; }

    /* Pure White Form Sanctuary Card Panels */
    .form-sanctuary-panel { 
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.12); 
        border-radius: 24px; padding: 40px; margin-bottom: 25px; 
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.01);
    }
    .form-panel-header { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #4A6B56; letter-spacing: 1.5px; margin-bottom: 25px; display: flex; align-items: center; gap: 8px; }
    .form-panel-dot { width: 7px; height: 7px; background: #4A6B56; border-radius: 50%; }
</style>
""", unsafe_allow_html=True)

# --- MOUNT THE BRAND TOP NAVIGATION BAR ---
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
# 🏛️ REYOU TEAL-BLUE HERO CANVAS SYSTEM WITH TWO-COLUMN IMAGE SPLIT
# =========================================================================
hero_col1, hero_col2 = st.columns([1.3, 1], gap="large")

with hero_col1:
    st.markdown("""
    <div style="padding-left: 45px; padding-top: 40px;">
        <div class="reyou-hero-tag">A Space for Intention</div>
        <div class="reyou-hero-h1" style="color: #2F4A4E !important; font-size: 46px;">Healing, Delivered<br>With Intention</div>
        <p style="font-size: 16px; color: #6E7570; line-height: 1.8; max-width: 520px;">
        Mass-market seminars treat your retirement like a sterile calculation, leaving you to manage complex policy overhauls alone. By translating shifting 2026 salary caps and interest milestones into a calm, personalized blueprint, we eliminate planning anxiety.
        </p>
    </div>
    """, unsafe_allow_html=True)

with hero_col2:
    # High-utility elegant portrait vector representation matching reyou.life home asset image layouts
    st.markdown('<div style="padding-right: 45px; padding-top: 20px;">', unsafe_allow_html=True)
    st.image("https://unsplash.com", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 📜 NARRATIVE SECTION: THE 3-PANEL SOVEREIGN BRIEF GRID
# =========================================================================
st.markdown("""
<div class="reyou-card-grid">
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 01 // The Guesswork</div>
        <div class="reyou-card-title">Are You Planning in the Dark?</div>
        <div class="reyou-card-desc">Tracking a moving statutory target manually creates hidden friction. Following major changes, you face crucial parameters:<br><br>
        • <b>The $8,000 Ordinary Wage Ceiling:</b> The contribution cap has reached its final step. Are you optimized to capture this expanded inflow pool?<br>
        • <b>The 2026 Retirement Sums:</b> The Full Retirement Sum (FRS) has scaled to <b>$220,400</b>, directly altering your liquidity boundaries.<br>
        • <b>The SA Closure Shock:</b> For members aged 55 and above, the Special Account has officially closed. Excess balances now flow directly into the OA at a lower 2.5% yield unless structurally reallocated.</div>
    </div>
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 02 // The Clarity</div>
        <div class="reyou-card-title">Your CPF Wealth Blueprint</div>
        <div class="reyou-card-desc">We turn raw account parameters and un-synthesized online statements into an elegant, visual roadmap built exclusively for your peace of mind:<br><br>
        • <b>Consolidated Flows:</b> Observe your Ordinary, Special, and Medisave Account streams side-by-side on a clean ledger panel.<br>
        • <b>Compounding Forecasts:</b> We compute your exact annual risk-free returns based on the extended 4% to 4.14% long-term floor rules.<br>
        • <b>Age 55 Vanguard Strategy:</b> A step-by-step map tracking how your Retirement Account (RA) will capitalize while protecting your withdrawable cash.</div>
    </div>
    <div class="reyou-sanctuary-card">
        <div class="reyou-card-tag">Panel 03 // The Dream Gap</div>
        <div class="reyou-card-title">Insulate Your True Horizon</div>
        <div class="reyou-card-desc">Most high-earning individuals face a severe <b>"Monthly Shortfall"</b> between basic, automatic CPF LIFE annuity payouts and their preferred lifestyle standard.<br><br>
        Our diagnostic audit looks directly at your trajectory against the 2026 Enhanced Retirement Sum (ERS) limit of <b>$440,800</b>—showing you exactly how to optimize your positions to lock in the maximum possible lifelong monthly payouts.</div>
    </div>
</div>
""", unsafe_allow_html=True)
# =========================================================================
# ☕ FORM ARCHITECTURE WORKSPACE & STARBUCKS CONSULTATION SCHEDULER
# =========================================================================

# Corrected balanced variables grid split loop
col_form1, col_form2 = st.columns(2, gap="large")

with col_form1:
    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot"></div>1. Allocation Coordinates</div>', unsafe_allow_html=True)
    client_name = st.text_input("Full Professional Name")
    client_contact = st.text_input("WhatsApp Mobile Coordinate")
    client_age = st.slider("Current Age Model", min_value=20, max_value=99, value=38)
    client_salary = st.number_input("Total Monthly Gross Ordinary Wage ($)", min_value=1000, value=8500, step=500)
    st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot" style="background:#4A6B56; box-shadow:0 0 8px rgba(74,107,86,0.3);"></div>2. Active Structural Reserves</div>', unsafe_allow_html=True)
    bal_oa = st.number_input("Ordinary Account (OA) Balance ($)", min_value=0, value=95000, step=5000)
    bal_sa = st.number_input("Special / Retirement Account (SA/RA) Balance ($)", min_value=0, value=70000, step=5000)
    bal_ma = st.number_input("Medisave Account (MA) Balance ($)", min_value=0, value=45000, step=5000)
    st.markdown('</div>', unsafe_allow_html=True)
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
