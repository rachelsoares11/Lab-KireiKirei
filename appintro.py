import streamlit as st

st.set_page_config(
    page_title="Kirei Kirei — Japan's #1 Handwash",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Fredoka+One&display=swap" rel="stylesheet">

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

.stApp {
    background: linear-gradient(160deg, #B2EEE8 0%, #E0F9F6 35%, #C8F0EC 60%, #B8EAE4 100%) !important;
    font-family: 'Nunito', sans-serif !important;
}

/* hide streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="collapsedControl"] { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── BUBBLE BACKGROUND ── */
.bubble-bg {
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    pointer-events: none; z-index: 0; overflow: hidden;
}
.bubble {
    position: absolute; border-radius: 50%;
    background: rgba(255,255,255,0.18);
    border: 2px solid rgba(255,255,255,0.35);
    animation: floatBubble linear infinite;
}
.bubble:nth-child(1)  { width:80px;  height:80px;  left:8%;   animation-duration:12s; animation-delay:0s;   top:70%; }
.bubble:nth-child(2)  { width:130px; height:130px; left:88%;  animation-duration:16s; animation-delay:2s;   top:60%; }
.bubble:nth-child(3)  { width:55px;  height:55px;  left:22%;  animation-duration:10s; animation-delay:4s;   top:80%; }
.bubble:nth-child(4)  { width:200px; height:200px; left:75%;  animation-duration:20s; animation-delay:1s;   top:50%; }
.bubble:nth-child(5)  { width:40px;  height:40px;  left:50%;  animation-duration:9s;  animation-delay:6s;   top:85%; }
.bubble:nth-child(6)  { width:100px; height:100px; left:35%;  animation-duration:14s; animation-delay:3s;   top:65%; }
.bubble:nth-child(7)  { width:160px; height:160px; left:5%;   animation-duration:18s; animation-delay:5s;   top:40%; }
.bubble:nth-child(8)  { width:70px;  height:70px;  left:65%;  animation-duration:11s; animation-delay:7s;   top:75%; }

@keyframes floatBubble {
    0%   { transform: translateY(0px) scale(1);   opacity: 0.4; }
    50%  { transform: translateY(-40vh) scale(1.05); opacity: 0.6; }
    100% { transform: translateY(-100vh) scale(1); opacity: 0; }
}

/* ── MAIN WRAPPER ── */
.page-wrap {
    position: relative; z-index: 1;
    padding: 0 0 60px 0;
}

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 60px 40px 40px 40px;
    animation: fadeSlideDown 0.9s ease both;
}
@keyframes fadeSlideDown {
    from { opacity:0; transform: translateY(-30px); }
    to   { opacity:1; transform: translateY(0); }
}

.no1-badge {
    display: inline-block;
    background: linear-gradient(135deg, #FF6BAE, #FF3D8A);
    color: white; font-family: 'Fredoka One', cursive;
    font-size: 1rem; padding: 6px 18px;
    border-radius: 40px; margin-bottom: 14px;
    box-shadow: 0 4px 15px rgba(255,60,130,0.35);
    letter-spacing: 0.5px;
}

.brand-name {
    font-family: 'Fredoka One', cursive;
    font-size: 5rem; line-height: 1;
    color: #1565C0;
    text-shadow: 3px 4px 0px rgba(21,101,192,0.15);
    margin-bottom: 4px;
}

.brand-jp {
    font-size: 1.4rem; color: #2196F3; letter-spacing: 6px;
    margin-bottom: 18px; font-weight: 700;
}

.brand-sub {
    display: inline-block;
    background: linear-gradient(135deg, #26C6DA, #00ACC1);
    color: white; font-size: 1.05rem; font-weight: 800;
    padding: 8px 24px; border-radius: 40px;
    letter-spacing: 1px; margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(0,172,193,0.4);
}

.hero-tagline {
    font-family: 'Fredoka One', cursive;
    font-size: 2.6rem; color: #1565C0;
    line-height: 1.15; margin-bottom: 8px;
}
.hero-tagline span { color: #FF3D8A; }

.hero-sub {
    font-size: 1.1rem; color: #00695C; font-weight: 600;
    margin-bottom: 40px;
}

/* ── BADGE ROW ── */
.badge-row {
    display: flex; justify-content: center; gap: 20px;
    flex-wrap: wrap; margin-bottom: 48px;
    animation: fadeSlideDown 1s ease 0.2s both;
}
.badge-pill {
    background: white; border-radius: 50px;
    padding: 12px 22px; display: flex; align-items: center; gap: 10px;
    box-shadow: 0 6px 20px rgba(0,150,136,0.15);
    border: 2px solid rgba(255,255,255,0.9);
    font-size: 0.9rem; font-weight: 800; color: #1565C0;
}
.badge-pill .icon { font-size: 1.4rem; }
.badge-pill .val { font-family: 'Fredoka One', cursive; font-size: 1.3rem; color: #FF3D8A; }

/* ── DIVIDER ── */
.wave-divider {
    text-align: center; font-size: 1.4rem;
    letter-spacing: 4px; color: rgba(21,101,192,0.3);
    margin: 10px 0 40px 0;
}

/* ── SECTION TITLES ── */
.section-title {
    text-align: center; margin: 0 auto 32px auto;
    animation: fadeSlideDown 0.8s ease both;
}
.section-title h2 {
    font-family: 'Fredoka One', cursive;
    font-size: 2.4rem; color: #1565C0; margin-bottom: 6px;
}
.section-title p {
    font-size: 1rem; color: #00796B; font-weight: 600;
    max-width: 600px; margin: 0 auto;
}

/* ── BRAND STORY ── */
.story-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
    max-width: 1000px; margin: 0 auto 60px auto; padding: 0 40px;
}
.story-card {
    background: white; border-radius: 24px; padding: 32px 28px;
    box-shadow: 0 8px 30px rgba(0,150,136,0.1);
    border-top: 5px solid #26C6DA;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    animation: fadeSlideDown 0.9s ease both;
}
.story-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 40px rgba(0,150,136,0.18);
}
.story-card .card-icon { font-size: 2.4rem; margin-bottom: 14px; }
.story-card h3 {
    font-family: 'Fredoka One', cursive; font-size: 1.4rem;
    color: #1565C0; margin-bottom: 10px;
}
.story-card p {
    font-size: 0.92rem; color: #444; line-height: 1.7; font-weight: 600;
}
.story-card .pink { border-top-color: #FF6BAE; }

/* ── PRODUCT CLAIMS ── */
.claims-wrap {
    max-width: 1100px; margin: 0 auto 60px auto; padding: 0 40px;
}
.claims-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px;
}
.claim-card {
    background: white; border-radius: 22px; padding: 26px 20px;
    text-align: center; box-shadow: 0 6px 24px rgba(0,150,136,0.1);
    border-bottom: 5px solid #FF6BAE;
    animation: fadeSlideDown 0.9s ease both;
    transition: transform 0.25s ease;
}
.claim-card:hover { transform: translateY(-6px); }
.claim-card .claim-icon { font-size: 2.8rem; margin-bottom: 12px; }
.claim-card .claim-num {
    font-family: 'Fredoka One', cursive; font-size: 2.2rem;
    color: #FF3D8A; line-height: 1;
}
.claim-card .claim-label {
    font-size: 0.82rem; font-weight: 800; color: #1565C0;
    margin: 6px 0 8px 0; line-height: 1.3;
    text-transform: uppercase; letter-spacing: 0.5px;
}
.claim-card .claim-desc {
    font-size: 0.8rem; color: #555; font-weight: 600; line-height: 1.55;
}

/* ── WHY INDIA ── */
.india-wrap {
    max-width: 1000px; margin: 0 auto 60px auto; padding: 0 40px;
}
.india-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;
}
.india-card {
    background: linear-gradient(135deg, #E0F9F6, #B2EEE8);
    border-radius: 22px; padding: 28px 22px; text-align: center;
    border: 2px solid rgba(255,255,255,0.8);
    box-shadow: 0 6px 22px rgba(0,150,136,0.1);
    animation: fadeSlideDown 0.9s ease both;
    transition: transform 0.25s ease;
}
.india-card:hover { transform: translateY(-5px); }
.india-card .i-icon { font-size: 2.4rem; margin-bottom: 12px; }
.india-card .i-stat {
    font-family: 'Fredoka One', cursive; font-size: 2rem; color: #1565C0;
}
.india-card .i-label {
    font-size: 0.85rem; font-weight: 800; color: #00695C;
    margin: 4px 0 8px 0; text-transform: uppercase; letter-spacing: 0.5px;
}
.india-card .i-desc {
    font-size: 0.82rem; color: #444; font-weight: 600; line-height: 1.6;
}

/* ── GAP SECTION ── */
.gap-wrap {
    max-width: 900px; margin: 0 auto 60px auto; padding: 0 40px;
    background: white; border-radius: 28px;
    box-shadow: 0 10px 40px rgba(0,150,136,0.12);
    padding: 40px 50px;
}
.gap-wrap h3 {
    font-family: 'Fredoka One', cursive; font-size: 1.8rem;
    color: #1565C0; margin-bottom: 20px; text-align: center;
}
.gap-row {
    display: flex; align-items: flex-start; gap: 16px;
    margin-bottom: 18px; padding-bottom: 18px;
    border-bottom: 1px dashed rgba(0,150,136,0.2);
}
.gap-row:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.gap-dot {
    width: 36px; height: 36px; border-radius: 50%; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; margin-top: 2px;
}
.gap-dot.pink  { background: #FFE0EF; }
.gap-dot.teal  { background: #E0F9F6; }
.gap-dot.blue  { background: #E3F2FD; }
.gap-text strong { font-weight: 800; color: #1565C0; font-size: 0.95rem; }
.gap-text p { font-size: 0.87rem; color: #555; font-weight: 600; line-height: 1.6; margin-top: 2px; }

/* ── CTA ── */
.cta-section {
    text-align: center; padding: 20px 40px 20px 40px;
    animation: fadeSlideDown 1s ease 0.3s both;
}
.cta-section h2 {
    font-family: 'Fredoka One', cursive; font-size: 2.4rem;
    color: #1565C0; margin-bottom: 10px;
}
.cta-section p {
    font-size: 1rem; color: #00695C; font-weight: 600; margin-bottom: 30px;
}
.cta-btn-wrap .stButton > button {
    background: linear-gradient(135deg, #FF6BAE, #FF3D8A) !important;
    color: white !important; font-family: 'Fredoka One', cursive !important;
    font-size: 1.3rem !important; padding: 18px 48px !important;
    border-radius: 50px !important; border: none !important;
    box-shadow: 0 8px 28px rgba(255,60,130,0.4) !important;
    letter-spacing: 1px !important;
    transition: all 0.25s ease !important;
}
.cta-btn-wrap .stButton > button:hover {
    transform: translateY(-4px) scale(1.04) !important;
    box-shadow: 0 14px 36px rgba(255,60,130,0.5) !important;
}

/* ── FOOTER ── */
.page-footer {
    text-align: center; padding: 20px;
    font-size: 0.8rem; color: rgba(0,105,92,0.6); font-weight: 600;
}
</style>

<div class="bubble-bg">
  <div class="bubble"></div><div class="bubble"></div><div class="bubble"></div>
  <div class="bubble"></div><div class="bubble"></div><div class="bubble"></div>
  <div class="bubble"></div><div class="bubble"></div>
</div>

<div class="page-wrap">

  <!-- HERO -->
  <div class="hero">
    <div class="no1-badge">🇯🇵 No. 1 Hand Soap in Japan</div>
    <div class="brand-name">Kirei Kirei</div>
    <div class="brand-jp">キレイ キレイ</div>
    <div class="brand-sub">Anti-Bacterial Foaming Hand Soap · by LION Japan</div>
    <div class="hero-tagline">Gentle &amp; Clean<br><span>for the Whole Family</span></div>
    <div class="hero-sub">Japan's most-loved family handwash now ready for India's most discerning households.</div>
  </div>

  <!-- BADGE ROW -->
  <div class="badge-row">
    <div class="badge-pill"><span class="icon">🧼</span><span><span class="val">12x</span> More Foam Volume</span></div>
    <div class="badge-pill"><span class="icon">🚫</span><span><span class="val">13</span> Chemicals Free</span></div>
    <div class="badge-pill"><span class="icon">🦠</span><span><span class="val">99.9%</span> Anti-Bacterial Pump</span></div>
    <div class="badge-pill"><span class="icon">⭐</span><span><span class="val">98%</span> Would Recommend</span></div>
  </div>

  <div class="wave-divider">〜 〜 〜 〜 〜</div>

  <!-- BRAND STORY -->
  <div class="section-title">
    <h2>🌸 The Brand Story</h2>
    <p>Three decades of Japanese family trust distilled into one foam pump.</p>
  </div>

  <div class="story-grid">
    <div class="story-card">
      <div class="card-icon">🏯</div>
      <h3>Born in Japan, Trusted by Millions</h3>
      <p>Kirei Kirei (キレイ キレイ) means "clean clean" in Japanese, a name that says exactly what it does. Launched by LION Corporation, Japan's leading household products company, it became Japan's <b>#1 hand soap series</b> and has been a household staple in East and Southeast Asia for over three decades.</p>
    </div>
    <div class="story-card pink">
      <div class="card-icon">👨‍👩‍👧‍👦</div>
      <h3>Built for Families, Loved by Children</h3>
      <p>Kirei Kirei was designed from the ground up for the whole family, from toddlers to grandparents. Its rich creamy foam requires no lathering, making handwashing effortless and fun for children. The playful foam pump is so satisfying to use that kids actually <b>ask for it by name.</b></p>
    </div>
    <div class="story-card">
      <div class="card-icon">🔬</div>
      <h3>Science Behind the Gentleness</h3>
      <p>The formula is free from <b>13 harsh chemicals</b> including parabens, triclosan, and chloroxylenol, that cause dryness, irritation, and long-term skin sensitivity. This is not just a gentleness claim. It is a rigorous formulation standard that mass-market Indian brands like Dettol and Lifebuoy do not meet.</p>
    </div>
    <div class="story-card pink">
      <div class="card-icon">💡</div>
      <h3>The World's First Anti-Bacterial Foaming Pump</h3>
      <p>Kirei Kirei's new Anti-Bacterial Foaming Pump prevents <b>99.9% germ growth on the pump surface itself</b>, not just the soap. In shared family bathrooms and school washrooms, the dispenser is often the dirtiest touchpoint. Kirei Kirei solves a problem no other brand has even identified.</p>
    </div>
  </div>

  <div class="wave-divider">〜 〜 〜 〜 〜</div>

  <!-- PRODUCT CLAIMS -->
  <div class="section-title">
    <h2>✨ Four Claims No Competitor Owns</h2>
    <p>Each claim is clinically proven. None are matched by any Indian handwash brand today.</p>
  </div>

  <div class="claims-wrap">
    <div class="claims-grid">
      <div class="claim-card">
        <div class="claim-icon">🫧</div>
        <div class="claim-num">12x</div>
        <div class="claim-label">More Volume Than Liquid Handwash</div>
        <div class="claim-desc">Spreads to every fingertip without lathering. Less product per wash, more value per bottle. Makes the refill model obviously economical.</div>
      </div>
      <div class="claim-card">
        <div class="claim-icon">🚫</div>
        <div class="claim-num">13</div>
        <div class="claim-label">Harsh Chemicals Excluded</div>
        <div class="claim-desc">Free from parabens, triclosan, chloroxylenol and 10 more. Reduces skin sensitivity and irritation, critical for children's daily use.</div>
      </div>
      <div class="claim-card">
        <div class="claim-icon">☁️</div>
        <div class="claim-num">Rich</div>
        <div class="claim-label">Creamy Foam, No Lathering</div>
        <div class="claim-desc">Very fine foam removes dirt without rubbing, doesn't fall off with palms facing down, and rinses off instantly. A sensory experience liquid soap cannot replicate.</div>
      </div>
      <div class="claim-card">
        <div class="claim-icon">🦠</div>
        <div class="claim-num">99.9%</div>
        <div class="claim-label">Germ Prevention on Pump Surface</div>
        <div class="claim-desc">The Anti-Bacterial Foaming Pump inhibits bacteria on the pump head. The dispenser itself is clean, a category-first innovation.</div>
      </div>
    </div>
  </div>

  <div class="wave-divider">〜 〜 〜 〜 〜</div>

  <!-- WHY INDIA -->
  <div class="section-title">
    <h2>Why India? Why Now?</h2>
    <p>A Rs.4,200 Cr market, a post-COVID hygiene boom, and a gap that Kirei Kirei was born to fill.</p>
  </div>

  <div class="india-wrap">
    <div class="india-grid">
      <div class="india-card">
        <div class="i-icon">📈</div>
        <div class="i-stat">₹4,200 Cr</div>
        <div class="i-label">Market Size</div>
        <div class="i-desc">India's hand hygiene market growing at 9.2% CAGR. Post-COVID, handwash moved from optional to essential in premium households.</div>
      </div>
      <div class="india-card">
        <div class="i-icon">🏙️</div>
        <div class="i-stat">6.5 Lakh</div>
        <div class="i-label">Premium Mumbai Households</div>
        <div class="i-desc">Mumbai alone has 650,000 high-income households. Our data shows 78%+ Japanese brand affinity in this segment pre-built brand trust.</div>
      </div>
      <div class="india-card">
        <div class="i-icon">🕳️</div>
        <div class="i-stat">Zero</div>
        <div class="i-label">Competitors Own This Space</div>
        <div class="i-desc">No Indian brand offers foam format + antibacterial + 13-Free gentle formula together. Kirei Kirei enters a gap, not a war.</div>
      </div>
      <div class="india-card">
        <div class="i-icon">👶</div>
        <div class="i-stat">₹2,850</div>
        <div class="i-label">Annual LTV per Family</div>
        <div class="i-desc">Pump once, refill monthly. Families with children buy more frequently and churn far less a generational LTV play.</div>
      </div>
      <div class="india-card">
        <div class="i-icon">⚡</div>
        <div class="i-stat">10 Min</div>
        <div class="i-label">Quick Commerce Window</div>
        <div class="i-desc">Blinkit and Zepto now reach high-income Mumbai households in 10 minutes the perfect impulse channel for a premium trial product.</div>
      </div>
      <div class="india-card">
        <div class="i-icon">🌿</div>
        <div class="i-stat">Eco</div>
        <div class="i-label">Refill Model Advantage</div>
        <div class="i-desc">Eco-conscious Mumbai parents actively seek sustainable alternatives. Kirei Kirei's refill model reduces plastic waste a brand value that builds loyalty.</div>
      </div>
    </div>
  </div>

  <div class="wave-divider">〜 〜 〜 〜 〜</div>



</div>
""", unsafe_allow_html=True)

# CTA
st.markdown('<div class="cta-section"><h2>Ready to See the India Strategy?</h2><p>Our data-driven GTM plan — built on 300+ Mumbai consumer responses — shows exactly how Kirei Kirei wins.</p></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    st.markdown('<div class="cta-btn-wrap">', unsafe_allow_html=True)
    if st.button("🚀  Explore the India Market Strategy  →", use_container_width=True):
        st.switch_page("pages/app.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="page-footer">Kirei Kirei India Entry Strategy · Presented by LION Japan · Data: 300+ Mumbai Consumer Responses</div>', unsafe_allow_html=True)