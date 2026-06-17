import datetime
import json
import streamlit as st

st.set_page_config(page_title="Cecilia Woon | 2026 CPF Sovereign Review", layout="wide")

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #050507 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif;
    }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    .brand-container { padding: 40px 45px 10px 45px; background: #050507; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
    .brand-text { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.5px; text-transform: uppercase; }
    .brand-text span { color: #E31837; font-size: 11px; font-family: 'Inter', sans-serif; font-weight: bold; letter-spacing: 2px; margin-left: 12px; vertical-align: middle; }
    .story-hero { padding: 45px; background: #050507; margin-bottom: 10px; }
    .story-tag { color: #8A8A93; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 20px; }
    .story-h1 { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 700; line-height: 1.2; margin-bottom: 15px; letter-spacing: -0.5px; }
    .story-h1 span { color: #D4AF37; }
    .story-row { display: flex; border-top: 1px solid rgba(255, 255, 255, 0.08); padding: 45px; background: #050507; }
    .story-left-label { flex: 0.4; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #8A8A93; font-weight: bold; line-height: 1.5; }
    .story-right-content { flex: 1.6; }
    .story-h3 { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 600; margin-bottom: 15px; color: #FFFFFF; }
    .story-p { font-size: 16px; color: #A0A0A5; line-height: 1.7; max-width: 850px; }
    .terminal-panel { background: #0B0B0E; border: 1px solid rgba(255, 255, 255, 0.04); border-radius: 16px; padding: 35px; margin-bottom: 30px; }
    .terminal-header { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #8A8A93; letter-spacing: 1.5px; margin-bottom: 25px; display: flex; align-items: center; gap: 8px; }
    .terminal-dot { width: 6px; height: 6px; background: #D4AF37; border-radius: 50%; box-shadow: 0 0 10px #D4AF37; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-container"><div class="brand-text">CECILIA WOON <span>Sovereign Wealth Architecture</span></div></div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-hero">
    <div class="story-tag">Sovereign Wealth Brief</div>
    <div class="story-h1">The Phased Complexity of <span>2026 CPF Rules</span></div>
</div>
<div class="story-row">
    <div class="story-left-label">Panel 01<br>The Guesswork</div>
    <div class="story-right-content">
        <div class="story-h3">Are You Planning Your Wealth in the Dark?</div>
        <div class="story-p">Manually tracking your CPF allocations across shifting regulatory parameters is a moving target. Public mass-market seminars outline basic statutory principles but fail to diagnose your individual financial blind spots. Without a diagnostic portfolio review, you run the risk of structural capital leakages:
        <br><br>
        • <b>The 2026 Wage Ceiling Shift:</b> Monthly Ordinary Wage (OW) contribution caps are rising to <b>$8,000</b>. Are you optimized to capture this capital expansion?<br>
        • <b>The Interest Drag Gap:</b> Leaving excess reserves sitting in your OA at a flat 2.5% rate while SA/RA accounts compound up to 4% (with tiers up to 6%) creates a persistent drag on your compounding growth track.<br>
        • <b>The Hidden Retirement Sums:</b> The 2026 Full Retirement Sum (FRS) milestone has officially scaled to <b>$220,400</b>. Missing this metric alters your liquidity boundaries at age 55.</div>
    </div>
</div>
<div class="story-row">
    <div class="story-left-label">Panel 02<br>The Clarity</div>
    <div class="story-right-content">
        <div class="story-h3">Your Customized Wealth Blueprint</div>
        <div class="story-p">We turn raw account parameters and un-synthesized statements into a visual, high-fidelity asset roadmap. A personalized blueprint replaces generic advice with corporate-grade ledger clarity:
        <br><br>
        • <b>Consolidated Stream View:</b> Observe your monthly account inflows mapped out side-by-side to understand your exact wealth velocity.<br>
        • <b>Projected Compounding Vectors:</b> We compute your precise annual interest earnings based on the extended statutory 4% floor metrics.<br>
        • <b>The Vanguard Age 55 Strategy:</b> We outline an exact roadmap for how your Retirement Account (RA) will fund while optimizing your withdrawable cash limits.</div>
    </div>
</div>
<div class="story-row">
    <div class="story-left-label">Panel 03<br>The Dream Gap</div>
    <div class="story-right-content">
        <div class="story-h3">Don't Let Your Lifetime Payouts Be an Unexpected Surprise</div>
        <div class="story-p">Most high-earning professionals face a massive, unaddressed <b>"Retirement Lifestyle Shortfall"</b> between automatic statutory CPF LIFE payout limits and the true cash flow required to sustain their current quality of life. 
        <br><br>
        Our diagnostic review maps out your current trajectory against the 2026 Enhanced Retirement Sum (ERS) limit of <b>$440,800</b>—defining exactly how to eliminate the lifestyle gap and scale your future guaranteed monthly payouts to the maximum legal limit.</div>
    </div>
</div>
<div class="story-row">
    <div class="story-left-label">Panel 04<br>The Matrix</div>
    <div class="story-right-content">
        <div class="story-h3">Secure Your Custom Blueprint in 60 Seconds</div>
        <div class="story-p" style="margin-bottom:30px;">Stop guessing. Start growing. Enter your current baseline parameters below. Your calculated metrics remain entirely hidden from this public view and will be presented exclusively as an offline diagnostic report during your review session.</div>
    </div>
</div>
""", unsafe_allow_html=True)
col_form1, col_form2 = st.columns(2, gap="large")

with col_form1:
    st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot"></div>1. Capital & Allocation Metrics</div>', unsafe_allow_html=True)
    client_name = st.text_input("Full Professional Name")
    client_contact = st.text_input("WhatsApp Mobile Coordinate")
    client_age = st.slider("Current Age Model", min_value=20, max_value=99, value=38)
    client_salary = st.number_input("Total Monthly Gross Ordinary Wage ($)", min_value=1000, value=8500, step=500)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot" style="background:#4A90E2; box-shadow:0 0 10px #4A90E2;"></div>2. Active Structural Reserves</div>', unsafe_allow_html=True)
    bal_oa = st.number_input("Ordinary Account (OA) Balance ($)", min_value=0, value=95000, step=5000)
    bal_sa = st.number_input("Special / Retirement Account (SA/RA) Balance ($)", min_value=0, value=70000, step=5000)
    bal_ma = st.number_input("Medisave Account (MA) Balance ($)", min_value=0, value=45000, step=5000)
    st.markdown('</div>', unsafe_allow_html=True)

with col_form2:
    st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot" style="background:#E31837; box-shadow:0 0 10px #E31837;"></div>3. Housing Asset Capital Outflows</div>', unsafe_allow_html=True)
    using_housing = st.radio("Are you currently utilizing CPF to service a property loan?", ["Yes, actively executing outflows", "No, asset is unencumbered / cash funded"])
    
    if "Yes" in using_housing:
        housing_outflow = st.number_input("Monthly CPF Property Loan Withdrawal Amount ($)", min_value=0, value=2200, step=100)
        housing_years = st.number_input("Remaining Duration of Outstanding Loan (Years)", min_value=1, max_value=35, value=22, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot" style="background:#007A5E; box-shadow:0 0 10px #007A5E;"></div>4. Strategic Review Scheduling</div>', unsafe_allow_html=True)
    preferred_date = st.date_input("Preferred Strategy Session Date", min_value=datetime.date.today(), value=datetime.date.today() + datetime.timedelta(days=3))
    consult_mode = st.radio("Preferred Workspace Environment Mode:", [
        "🌐 Immersive Online Video Session (Zoom/Google Meet)",
        "☕ In-Person Private Boardroom Consultation (With Complimentary Starbucks Coffee)"
    ])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="padding: 10px 0 80px 45px;">', unsafe_allow_html=True)
if st.button("Generate My Free 2026 CPF Review Blueprint", type="primary"):
    if client_name and client_contact:
        st.success(f"🎉 Allocation Sequence Initialized for {client_name}!")
        st.info(f"📌 Status: Your asset coordinates have been securely locked. Our office will reach out via WhatsApp at {client_contact} within 24 hours to confirm your private {consult_mode.split(' (')[:-1]} session for {preferred_date.strftime('%B %d, %Y')}. Your custom offline 2026 P&L Blueprint is now compiling.")
    else:
        st.error("🔒 Authentication Fault: Please complete your Name and WhatsApp Coordinate fields to authorize report compilation loops.")
st.markdown('</div>', unsafe_allow_html=True)
