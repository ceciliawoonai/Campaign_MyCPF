import datetime
import streamlit as st

st.set_page_config(page_title="Sanctuary | Private Wealth Architecture", layout="wide")

# --- CEC THERAPEUTIC DESIGN SYSTEM FOR WEALTH ARCHITECTURE ---
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
    
    /* Sanctuary Header Layout Group */
    .cec-hero {
        padding: 80px 60px 40px 60px; max-width: 900px;
    }
    .cec-hero-tag {
        font-size: 11px; text-transform: uppercase; letter-spacing: 3px;
        color: #4A7C59; margin-bottom: 20px; font-weight: 600;
    }
    .cec-hero-h1 {
        font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 400;
        line-height: 1.3; color: #1F2421; margin-bottom: 25px; letter-spacing: -0.5px;
    }
    .cec-hero-h1 span { font-style: italic; color: #4A7C59; }
    .cec-hero-p { font-size: 16px; color: #6E7570; line-height: 1.8; }
    
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

<div class="cec-hero">
    <div class="cec-hero-tag">Core Philosophy</div>
    <div class="cec-hero-h1">We look past surface numbers to <span>treat your relationship with money.</span></div>
    <div class="cec-hero-p">Wealth management is not a cold, one-off transaction. True financial stability requires patient guidance spanning long before, during, and after planning. We explicitly reject aggressive product sales to support your permanent independence, long-term capital efficiency, and complete peace of mind.</div>
</div>
""", unsafe_allow_html=True)
# =========================================================================
# 🧭 PART 2: STRATEGIC MODALITIES, CONDITIONS, JOURNEY, AND RESTRAINT PANEL
# =========================================================================
st.markdown("""
<div class="cec-section-title">Structural Service Modalities</div>
<div class="cec-grid-container">
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 01</div>
        <div class="cec-card-title">Holistic Portfolio Care</div>
        <div class="cec-card-desc">Complete, high-end financial architecture combining cutting-edge FinTech diagnostic tools with patient, human-centered capital allocation.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 02</div>
        <div class="cec-card-title">The Human Safety Net</div>
        <div class="cec-card-desc">Beyond-the-broker care. If you struggle to put food on the table, our team immediately pivots your profile to crisis budgeting and lifestyle stabilization.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 03</div>
        <div class="cec-card-title">Career Support Synergy</div>
        <div class="cec-card-desc">When income streams stall, we step in directly to optimize your corporate CV, share inside job leads, and actively map out new employment opportunities.</div>
    </div>
</div>

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
        <div class="cec-card-title">Honest Clinical Evaluation</div>
        <div class="cec-card-desc">Every client relationship begins with a deep, comprehensive diagnostic audit of your financial life. If you do not need a product, we explicitly tell you.</div>
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
""", unsafe_allow_html=True)
# =========================================================================
# 🧭 PART 2: STRATEGIC MODALITIES, CONDITIONS, JOURNEY, AND RESTRAINT PANEL
# =========================================================================
st.markdown("""
<div class="cec-section-title">Structural Service Modalities</div>
<div class="cec-grid-container">
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 01</div>
        <div class="cec-card-title">Holistic Portfolio Care</div>
        <div class="cec-card-desc">Complete, high-end financial architecture combining cutting-edge FinTech diagnostic tools with patient, human-centered capital allocation.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 02</div>
        <div class="cec-card-title">The Human Safety Net</div>
        <div class="cec-card-desc">Beyond-the-broker care. If you struggle to put food on the table, our team immediately pivots your profile to crisis budgeting and lifestyle stabilization.</div>
    </div>
    <div class="cec-sanctuary-card">
        <div class="cec-card-tag">Modality 03</div>
        <div class="cec-card-title">Career Support Synergy</div>
        <div class="cec-card-desc">When income streams stall, we step in directly to optimize your corporate CV, share inside job leads, and actively map out new employment opportunities.</div>
    </div>
</div>

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
        <div class="cec-card-title">Honest Clinical Evaluation</div>
        <div class="cec-card-desc">Every client relationship begins with a deep, comprehensive diagnostic audit of your financial life. If you do not need a product, we explicitly tell you.</div>
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
""", unsafe_allow_html=True)
