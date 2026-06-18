import datetime
import streamlit as st

st.set_page_config(page_title="Sanctuary | Private Wealth Architecture", layout="wide")

# --- CEC THERAPEUTIC DESIGN SYSTEM WITH FLOATING LAYERS MATRIX ---
st.markdown("""
<style>
    /* Global Low-Arousal Calm Canvas Background */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FDFBF7 !important; /* Calming oatmeal sand canvas */
        color: #2D3142 !important; /* Grounded slate typography */
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    
    /* Monochromatic sensory navigation bar row */
    .cec-header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 25px 60px; background: #FDFBF7;
        border-bottom: 1px solid rgba(74, 107, 86, 0.08);
    }
    .cec-logo {
        font-family: 'Playfair Display', serif; font-size: 20px;
        font-weight: 500; color: #3A4F41; letter-spacing: 1px;
    }
    .cec-menu {
        display: flex; gap: 2.5rem; font-size: 13px; color: #6E7570; letter-spacing: 0.5px;
    }
    
    /* THE SIGNATURE CEC TEAL SANCTUARY VIEWPORT CANVAS BLOCK */
    .cec-teal-canvas-container {
        background-color: #2F4A4E !important; /* Premium therapeutic teal blue */
        border-radius: 32px;
        margin: 20px 45px 40px 45px;
        padding: 80px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 20px 50px rgba(47, 74, 78, 0.12);
        position: relative;
        overflow: hidden;
    }
    
    /* Animated Floating Background Cloud Layers Passing Behind */
    .cec-teal-canvas-container::before {
        content: ''; position: absolute; top: 0; left: 0; width: 200%; height: 100%;
        background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 60%);
        animation: slowDriftClouds 25s linear infinite;
        pointer-events: none; z-index: 1;
    }
    @keyframes slowDriftClouds {
        0% { transform: translateX(0%); }
        100% { transform: translateX(-50%); }
    }
    
    .canvas-text-block { position: relative; z-index: 10; max-width: 550px; color: #FFFFFF !important; }
    .cec-hero-tag { font-size: 11px; text-transform: uppercase; letter-spacing: 3px; color: #A3C1AD; margin-bottom: 20px; font-weight: 600; }
    .cec-hero-h1 { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 400; line-height: 1.3; margin-bottom: 25px; letter-spacing: -0.5px; color: #FFFFFF !important; }
    .cec-hero-h1 span { font-style: italic; color: #E8F0EC; }
    .cec-hero-p { font-size: 16px; color: #E8F0EC; line-height: 1.8; opacity: 0.95; }
    
    /* FLOATING SILHOUETTE IMAGE HOLDER CONTAINER */
    .cec-floating-lady-portrait {
        position: relative; z-index: 5; max-width: 420px; width: 100%;
        animation: calmBreathingPulse 6s ease-in-out infinite;
    }
    @keyframes calmBreathingPulse {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-6px); } /* Ambient, organic breathing lift movement */
    }
    
    /* Grid Layout Framework System Blocks */
    .cec-section-title {
        font-family: 'Playfair Display', serif; font-size: 26px; color: #1F2421;
        padding: 40px 60px 15px 60px; font-weight: 500;
    }
    .cec-grid-container {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;
        padding: 10px 60px 40px 60px; max-width: 1400px;
    }
    .cec-sanctuary-card {
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.1);
        border-radius: 24px; padding: 40px 35px;
        box-shadow: 0 10px 40px rgba(74, 107, 86, 0.01);
        transition: all 0.4s ease;
    }
    .cec-sanctuary-card:hover {
        transform: translateY(-3px);
        border-color: rgba(74, 107, 86, 0.25);
        box-shadow: 0 15px 45px rgba(74, 107, 86, 0.04);
    }
    .cec-card-tag { font-size: 10px; text-transform: uppercase; letter-spacing: 2px; color: #A2A7A4; margin-bottom: 12px; }
    .cec-card-title { font-family: 'Playfair Display', serif; font-size: 19px; color: #1F2421; margin-bottom: 12px; font-weight: 600; }
    .cec-card-desc { font-size: 14px; color: #6E7570; line-height: 1.7; }
    
    /* Secure Form Wrapper Panels */
    .form-sanctuary-panel { 
        background: #FFFFFF; border: 1px solid rgba(74, 107, 86, 0.12); 
        border-radius: 24px; padding: 40px; margin-bottom: 25px; 
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.01);
    }
    .form-panel-header { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #4A6B56; letter-spacing: 1.5px; margin-bottom: 25px; display: flex; align-items: center; gap: 8px; }
    .form-panel-dot { width: 7px; height: 7px; background: #4A6B56; border-radius: 50%; }
</style>
""", unsafe_allow_html=True)

# --- HEADER MOUNT ---
st.markdown("""
<div class="cec-header">
    <div class="cec-logo">cec.space</div>
    <div class="cec-menu">
        <span>Philosophy</span>
        <span>Modalities</span>
        <span>The Workspace</span>
    </div>
</div>

<div class="cec-teal-canvas-container">
    <div class="canvas-text-block">
        <div class="cec-hero-tag">Core Philosophy</div>
        <div class="cec-hero-h1">We look past surface numbers to <span>treat your relationship with money.</span></div>
        <div class="cec-hero-p">Wealth management is not a cold, one-off transaction. True financial stability requires patient guidance spanning long before, during, and after planning. We explicitly reject aggressive product sales to support your permanent independence, long-term capital efficiency, and complete peace of mind.</div>
    </div>
    <img class="cec-floating-lady-portrait" src="https://unsplash.com" alt="Sovereign Portrait">
</div>

<div class="cec-section-title">Structural Service Modalities</div>
<div class="cec-grid-container">
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 01</div>
        <div class="cec-card-title">Holistic Portfolio Care</div>
        <div class="cec-card-desc">Complete, high-end financial architecture combining cutting-edge structural mapping parameters with patient, human-centered capital allocation.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 02</div>
        <div class="cec-card-title">The Human Safety Net</div>
        <div class="cec-card-desc">Beyond-the-broker care. If you struggle to meet immediate overheads, our team immediately pivots your profile to crisis budgeting and lifestyle stabilization.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 03</div>
        <div class="cec-card-title">Career Support Synergy</div>
        <div class="cec-card-desc">When income streams stall, we step in directly to optimize your corporate CV, share inside job leads, and actively map out new employment opportunities.</div>
    </div>
</div>
""", unsafe_allow_html=True)
# =========================================================================
# 🧭 PART 2: SOVEREIGN CONDITIONS, JOURNEY ROWS, & SCHEDULER SANCTUARY
# =========================================================================
st.markdown("""
<div class="cec-section-title">Sovereign Conditions Treated</div>
<div class="cec-grid-container">
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Condition Alpha</div>
        <div class="cec-card-title">Financial Paralysis</div>
        <div class="cec-card-desc">Halts the overwhelming anxiety, fear, and hypervigilance that causes people to avoid looking at their bank statements or planning ahead.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Condition Beta</div>
        <div class="cec-card-title">Product Over-Saturation</div>
        <div class="cec-card-desc">We rescue clients stuck in the exhausting loop of being aggressively sold overlapping, high-commission insurance policies by predatory brokers.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Condition Gamma</div>
        <div class="cec-card-title">Income Interruption</div>
        <div class="cec-card-desc">Direct, hand-held protection and liquidity restructuring during sudden job losses, executive career transitions, or macroeconomic shifts.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Condition Delta</div>
        <div class="cec-card-title">Generational Wealth Stress</div>
        <div class="cec-card-desc">Navigating the heavy emotional burdens, complex family dynamics, and legal responsibilities of inheritance management or legacy debt.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Condition Epsilon</div>
        <div class="cec-card-title">Hospitalization Care</div>
        <div class="cec-card-desc">While others just file insurance claims, we visit you personally to manage medical billing cycles and keep your household running smoothly during illness.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Condition Zeta</div>
        <div class="cec-card-title">Investment Confusion</div>
        <div class="cec-card-desc">Demystifying complex market jargon, crypto fads, and aggressive tech-sector volatility into calm, simple, and logical wealth preservation steps.</div>
    </div>
</div>

<div class="cec-section-title">The Treatment Journey</div>
<div class="cec-grid-container">
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Step 01 // Assessment</div>
        <div class="cec-card-title">Honest Evaluation Audit</div>
        <div class="cec-card-desc">Every client relationship begins with a deep corporate P&L balance assessment. If you do not need an asset reallocation, we explicitly tell you.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Step 02 // Action</div>
        <div class="cec-card-title">Supported Execution</div>
        <div class="cec-card-desc">We stand physically by your side during scary financial decisions—signing legal papers, shifting asset structures, and steadying your emotions.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Step 03 // Consistency</div>
        <div class="cec-card-title">Lifelong Integration</div>
        <div class="cec-card-desc">We translate complex global investment strategies into clear, simple, and repeatable habits that blend naturally and effortlessly into your daily life.</div>
    </div>
</div>

<div class="cec-section-title">Sanctuary & Experience Metrics</div>
<div class="cec-grid-container">
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Environment</div>
        <div class="cec-card-title">The Consultation Haven</div>
        <div class="cec-card-desc">Meeting spaces engineered to feel secure and private. No high-pressure sales charts—just coffee, safety, and open conversational dialogue.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Infrastructure</div>
        <div class="cec-card-title">Advanced FinTech Mastery</div>
        <div class="cec-card-desc">Leveraging institutional-grade asset platforms that give you absolute, transparent, real-time visibility into your capital from A to Z.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Trust Mandate</div>
        <div class="cec-card-title">Anti-Commission Guard</div>
        <div class="cec-card-desc">Our strict fiduciary review framework means we prioritize your actual long-term progress over hitting transactional monthly sales quotas.</div>
    </div>
</div>

<div style="background: rgba(74, 107, 86, 0.03); border-top: 1px solid rgba(74, 107, 86, 0.08); border-bottom: 1px solid rgba(74, 107, 86, 0.08); padding: 50px 0; margin-top: 30px; margin-bottom: 50px;">
    <div class="cec-section-title" style="padding-top:0;">Experience & Radical Restraint</div>
    <div style="padding: 0 60px; max-width: 950px; font-size: 16px; color: #5C6479; line-height: 1.8;">
        Built by industry veterans with deep cross-functional experience across the full spectrum of global markets, FinTech innovation, and sovereign wealth preservation. 
        <br><br>
        We operationalize <b>Radical Restraint as a Skill</b>—knowing exactly when to actively allocate capital, when to quietly rebalance behind the scenes, and when to simply leave your portfolio alone to let it heal, compound, and grow naturally.
    </div>
</div>

<div style="text-align:center; padding:10px 45px 15px 45px; max-width:750px; margin:0 auto;">
    <h3 style="font-family:'Playfair Display', serif; font-size:26px; font-weight:400; color:#1F2421; margin-bottom:12px;">Request Entry Into the Sanctuary</h3>
    <p style="font-size:14px; color:#6E7570; margin-bottom:35px; line-height:1.6;">Take a breath. Enter your baseline coordinates below. All fields are processed with complete confidentiality in local secure browser variables with zero public data logging leaks.</p>
</div>
""", unsafe_allow_html=True)

col_form1, col_form2 = st.columns(2, gap="large")

with col_form1:
    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot"></div>1. Allocation Coordinates</div>', unsafe_allow_html=True)
    client_name = st.text_input("Full Professional Name")
    client_contact = st.text_input("WhatsApp Mobile Coordinate")
    client_age = st.slider("Current Age Model", min_value=20, max_value=99, value=38)
    client_salary = st.number_input("Total Monthly Gross Salary ($)", min_value=1000, value=8500, step=500)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot" style="background:#4A6B56; box-shadow:0 0 8px rgba(74,107,86,0.3);"></div>2. Active Reserves Portfolio</div>', unsafe_allow_html=True)
    bal_oa = st.number_input("Total Liquid / Cash Reserves ($)", min_value=0, value=95000, step=5000)
    bal_sa = st.number_input("Sovereign Growth Account Balance ($)", min_value=0, value=70000, step=5000)
    bal_ma = st.number_input("Medical Insulation Balance ($)", min_value=0, value=45000, step=5000)
    st.markdown('</div>', unsafe_allow_html=True)

with col_form2:
    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot" style="background:#8D99AE; box-shadow:0 0 8px rgba(141,153,174,0.3);"></div>3. Housing Asset Outflows</div>', unsafe_allow_html=True)
    using_housing = st.radio("Are you currently utilizing capital reserves to service an active property loan?", ["Yes, actively executing outflows", "No, asset is unencumbered / cash funded"])
    
    if "Yes" in using_housing:
        housing_outflow = st.number_input("Monthly Property Loan Withdrawal Amount ($)", min_value=0, value=2200, step=100)
        housing_years = st.number_input("Remaining Duration of Outstanding Loan (Years)", min_value=1, max_value=35, value=22, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="form-sanctuary-panel"><div class="form-panel-header"><div class="form-panel-dot" style="background:#3A4F41; box-shadow:0 0 8px rgba(58,79,65,0.4);"></div>4. Strategy Space Booking</div>', unsafe_allow_html=True)
    preferred_date = st.date_input("Preferred Strategy Session Date", min_value=datetime.date.today(), value=datetime.date.today() + datetime.timedelta(days=3))
    consult_mode = st.radio("Choose a Consultation Space Style:", [
        "🌐 Low-Key Online Workspace (Zoom / Google Meet)",
        "☕ In-Person Private Boardroom Consultation (With Complimentary Starbucks Coffee)"
    ])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; padding: 10px 0 100px 0;">', unsafe_allow_html=True)
if st.button("Request My Calming Portfolio Review Blueprint", type="primary"):
    if client_name and client_contact:
        st.success(f"✨ Session Sequence Initialized for {client_name}!")
        st.info(f"📌 Status: Your coordinates have been safely locked. Our office will reach out via WhatsApp at {client_contact} within 24 hours to confirm your private {consult_mode.split(' (')[:-1]} sanctuary workspace on {preferred_date.strftime('%B %d, %Y')}.")
    else:
        st.error("🔒 Authentication Fault: Please complete your Name and WhatsApp Coordinate fields to unlock strategy session request logs.")
st.markdown('</div>', unsafe_allow_html=True)
