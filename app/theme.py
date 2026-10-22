
"""
AgriSafe AI — Shared Theme
Forest green, warm ivory, sage and gold.
"""

import streamlit as st

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Cormorant+Garamond:wght@500;600;700&display=swap');

:root {
    --bg: #F7F5EC;
    --bg-2: #EAEDE1;
    --emerald: #174D35;
    --em2: #347650;
    --gold: #C49A45;
    --gold2: #946C20;
    --cream: #20352A;
    --muted: #56685B;
    --line: #D7DFD0;
    --glass: #FFFFFF;
    --glass2: #F0F2E8;
}

html, body, [data-testid="stApp"],
[data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--cream) !important;
    font-family: 'Inter', sans-serif !important;
    overflow-x: hidden;
}

[data-testid="stAppViewContainer"] {
    background:
    radial-gradient(ellipse at 0% 0%, #DCE9D5 0%, transparent 38%),
    radial-gradient(ellipse at 100% 0%, #F1DFB9 0%, transparent 32%),
    linear-gradient(135deg, #F7F5EC 0%, #EEF1E5 55%, #F8F0E1 100%) !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}
#MainMenu, footer, header {
    visibility: hidden;
}
[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    padding: 1.8rem 2.2rem 3rem !important;
    max-width: 1500px !important;
    position: relative;
}

::-webkit-scrollbar { width: 7px; }
::-webkit-scrollbar-track { background: var(--bg-2); }
::-webkit-scrollbar-thumb {
    background: var(--em2);
    border-radius: 5px;
}

/* Cards */
.glass {
    background: rgba(255,255,255,0.94);
    border: 1px solid var(--line);
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(23,77,53,0.055);
}

/* Hero */
.hero {
    position: relative;
    padding: 1.8rem 2rem;
    margin-bottom: 1.3rem;
    overflow: hidden;
    background: linear-gradient(
    110deg,
    #FFFFFF 0%,
    #E6EFDF 48%,
    #F3E6C9 100%
);
    border: 1px solid #D5E0D0;
    border-top: 4px solid var(--emerald);
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(23,77,53,0.075);
}

.hero::before {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    right: -90px;
    top: -135px;
    border-radius: 50%;
    background: radial-gradient(
        circle, rgba(196,154,69,0.18), transparent 70%
    );
    pointer-events: none;
}

.hero-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.2rem;
    flex-wrap: wrap;
}

.hero-left {
    display: flex;
    align-items: center;
    gap: 1.1rem;
}

.hero-badge {
    width: 60px;
    height: 60px;
    display: grid;
    place-items: center;
    font-size: 1.9rem;
    flex-shrink: 0;
    border-radius: 16px;
    background: linear-gradient(145deg, #E1EBDD, #F8EBD0);
    border: 1px solid #D1DDCC;
}

.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.8rem;
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -0.02em;
    background: linear-gradient(
        100deg, #143D2A 0%, #347650 65%, #A77927 100%
    );
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero-subtitle {
    color: #4F6456;
    font-size: 0.92rem;
    line-height: 1.6;
    margin-top: 0.4rem;
}

.hero-stats {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}

/* Status chips */
.stat-chip {
    background: #FFFFFF;
    border: 1px solid #D6E0D1;
    border-radius: 999px;
    padding: 0.48rem 0.8rem;
    color: var(--emerald);
    font-size: 0.76rem;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}
.stat-chip .dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #328452;
}
.stat-chip.gold {
    background: #FBF4E4;
    border-color: #E5D2A6;
    color: #805A17;
}

/* Contributor byline */
.byline {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    flex-wrap: wrap;
    margin-top: 0.65rem;
    padding: 0.35rem 0.7rem;
    background: rgba(255,255,255,0.8);
    border: 1px solid #DCE4D7;
    border-radius: 9px;
    font-size: 0.7rem;
    color: var(--muted);
}
.byline b { color: var(--emerald); font-weight: 700; }
.byline .sep { color: var(--gold2); margin: 0 0.15rem; }

/* Section headings */
.section-title {
    color: var(--emerald);
    font-size: 0.88rem;
    font-weight: 800;
    letter-spacing: 0.025em;
    margin-bottom: 0.9rem;
    padding-left: 0.75rem;
    border-left: 3px solid var(--gold);
}

/* Section containers */
.section-card {
    padding: 1.35rem 1.5rem;
    margin-bottom: 1rem;
    animation: fadeIn 0.35s ease;
    background: rgba(255,255,255,0.92);
    border: 1px solid var(--line);
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(23,77,53,0.045);
}

/* Navigation cards */
.nav-card {
    padding: 1.45rem 1.5rem;
    min-height: 205px;
    border-top: 3px solid var(--em2);
    cursor: default;
    transition: transform .2s ease, box-shadow .2s ease;
    animation: fadeIn 0.4s ease;
}
.nav-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(23,77,53,0.11);
}
.nav-card .icon {
    font-size: 1.8rem;
    margin-bottom: 0.6rem;
}
.nav-card .title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--emerald);
    margin-bottom: 0.45rem;
}
.nav-card .desc {
    color: #4F6255;
    font-size: 0.86rem;
    line-height: 1.65;
}
.nav-card .arrow {
    color: var(--gold2);
    font-size: 0.78rem;
    font-weight: 700;
    margin-top: 0.9rem;
}

/* Metrics */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #FFFFFF 0%, #F2F5EB 100%) !important;
    border: 1px solid #D8E1D2 !important;
    border-bottom: 3px solid #8AA987 !important;
    border-radius: 15px !important;
    padding: 1.1rem 1.2rem !important;
    box-shadow: 0 5px 16px rgba(23,77,53,0.055);
}
[data-testid="stMetricLabel"] {
    color: #526557 !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Cormorant Garamond', serif !important;
    color: #174D35 !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}
[data-testid="stMetricDelta"] {
    font-size: 0.76rem !important;
}
[data-testid="stMetricDeltaIcon"] {
    display: none !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg, #E8EDE0 0%, #F3F0E5 100%
    ) !important;
    border-right: 1px solid #D1DCCB !important;
}
[data-testid="stSidebar"] * {
    color: var(--cream);
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
    padding-top: 1rem;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] li {
    margin: 0.22rem 0;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
    border-radius: 9px;
    font-weight: 600;
    padding: 0.55rem 0.7rem;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
    background: #DCE7D5;
    color: #174D35 !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
    background: #D4E3CE !important;
    color: #174D35 !important;
    border-left: 3px solid var(--em2);
}
[data-testid="stSidebarHeader"] {
    background: transparent !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.4rem;
    background: transparent;
    border-bottom: 1px solid var(--line);
    margin-bottom: 0.8rem;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--muted) !important;
    border-radius: 9px 9px 0 0 !important;
    padding: 0.6rem 0.9rem !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] {
    color: var(--emerald) !important;
    border-bottom: 3px solid var(--gold) !important;
}

/* Buttons */
.stButton > button,
[data-testid="stDownloadButton"] > button,
[data-testid="stFileUploader"] section button {
    background: linear-gradient(110deg, #174D35, #347650) !important;
    color: #FFFFFF !important;
    border: 1px solid #174D35 !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: all .2s ease !important;
}
.stButton > button:hover,
[data-testid="stDownloadButton"] > button:hover {
    background: linear-gradient(110deg, #103B28, #286441) !important;
    box-shadow: 0 4px 12px rgba(23,77,53,0.2) !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
[data-testid="stFileUploaderDropzone"] {
    background: #FFFFFF !important;
    border: 1.5px dashed #9DB79B !important;
    border-radius: 14px !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--emerald) !important;
    background: #F1F6EC !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div > span,
[data-testid="stFileUploaderDropzoneInstructions"] > div > small {
    color: var(--cream) !important;
}
.uploadedFile {
    background: var(--glass2) !important;
    border-radius: 10px !important;
    border: 1px solid var(--line) !important;
}

/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"],
[data-testid="stDateInput"] input,
[data-testid="stTextArea"] textarea {
    background: #FFFFFF !important;
    color: var(--cream) !important;
    border: 1px solid #C9D7C5 !important;
    border-radius: 9px !important;
}
[data-testid="stRadio"] label,
[data-testid="stCheckbox"] label {
    color: var(--cream) !important;
}

/* Tables */
[data-testid="stDataFrame"] {
    border: 1px solid var(--line) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}
[data-testid="stDataFrame"] thead tr th {
    background: #E8EDE0 !important;
    color: var(--emerald) !important;
    font-size: 0.8rem !important;
}
[data-testid="stDataFrame"] tbody tr td {
    color: var(--cream) !important;
    font-size: 0.84rem !important;
}
[data-testid="stDataFrame"] tbody tr:nth-child(even) td {
    background: #F5F6F0 !important;
}

/* Progress bars */
[data-testid="stProgress"] > div > div {
    background: #E4EADF !important;
    border: 1px solid var(--line) !important;
    border-radius: 999px !important;
}
[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #347650, #C49A45) !important;
    border-radius: 999px !important;
}

/* Alerts */
[data-testid="stInfo"], [data-testid="stSuccess"],
[data-testid="stWarning"], [data-testid="stError"] {
    border-radius: 12px !important;
    font-size: 0.88rem !important;
}

/* Code */
[data-testid="stCode"] pre {
    background: #EDF0E6 !important;
    border: 1px solid var(--line) !important;
    border-radius: 12px !important;
    color: var(--cream) !important;
    font-size: 0.83rem !important;
}

/* Diagnosis components */
.diag-card {
    padding: 1.5rem 1.7rem;
    margin-bottom: 1rem;
    animation: fadeIn 0.35s ease;
    position: relative;
    overflow: hidden;
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(23,77,53,0.055);
}
.diag-card::after {
    content: '';
    position: absolute;
    top: -50px;
    right: -50px;
    width: 150px;
    height: 150px;
    background: radial-gradient(circle, rgba(196,154,69,0.12), transparent 70%);
    pointer-events: none;
}
.diag-label, .treat-title, .pred-title {
    color: var(--emerald);
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.diag-disease {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #B54747;
    margin: 0.4rem 0 0.25rem;
    line-height: 1.1;
}
.diag-disease.healthy { color: var(--em2) !important; }
.diag-sub, .gauge-caption, .gauge-scale span {
    color: var(--muted);
    font-size: 0.86rem;
}
.conf-val {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: var(--emerald);
    margin: 0.2rem 0 0.5rem;
}
.conf-bar-bg, .pred-bar-bg {
    background: #E5EADF;
    border-radius: 99px;
    height: 7px;
    width: 100%;
    overflow: hidden;
    border: 1px solid var(--line);
}
.conf-bar-fill, .pred-bar-fill {
    background: linear-gradient(90deg, #347650, #C49A45);
    border-radius: 99px;
    height: 100%;
    animation: growBar 0.8s ease forwards;
}
.treat-card {
    padding: 1.3rem 1.6rem;
    margin-bottom: 1rem;
}
.treat-text {
    color: var(--cream);
    font-size: 0.9rem;
    line-height: 1.7;
}
.gauge-wrap { margin-top: 1rem; }
.gauge-track {
    position: relative;
    height: 8px;
    border-radius: 999px;
    background: linear-gradient(
        90deg, #7BC58C 0%, #E8C068 38%, #E09A3A 70%, #D86A60 100%
    );
    border: 1px solid var(--line);
}
.gauge-marker {
    position: absolute;
    top: 50%;
    transform: translate(-50%,-50%);
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #FFFFFF;
    box-shadow: 0 1px 6px rgba(37,53,44,0.22);
    border: 2px solid rgba(37,53,44,0.2);
}
.gauge-scale {
    display: flex;
    justify-content: space-between;
    margin-top: 0.4rem;
}
.pred-card { padding: 1.2rem 1.4rem; }
.pred-rank {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #E6EDE0;
    border: 1px solid var(--line);
    display: grid;
    place-items: center;
    color: var(--emerald);
    font-size: 0.8rem;
    font-weight: 700;
}
.pred-name {
    color: var(--cream);
    font-size: 0.86rem;
    font-weight: 600;
    margin-bottom: 0.3rem;
}
.pred-pct {
    color: var(--emerald);
    font-size: 0.83rem;
    font-weight: 700;
    text-align: right;
}

/* Warnings and images */
.warn-banner {
    padding: 0.75rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin: 0.8rem 0;
    border-color: rgba(196,154,69,0.45) !important;
}
.warn-banner span:first-child { color: var(--gold2); }
.warn-banner span:last-child {
    color: var(--muted);
    font-size: 0.84rem;
    line-height: 1.5;
}
.img-frame {
    border: 1px solid var(--line);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 5px 18px rgba(23,77,53,0.08);
}
.img-frame img { width: 100%; display: block; }
.img-label {
    color: var(--emerald);
    font-size: 0.85rem;
    font-weight: 700;
    margin: 0.9rem 0 0.4rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* Timeline */
.timeline-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 0.7rem 0;
    border-bottom: 1px solid var(--line);
}
.timeline-item:last-child { border-bottom: none; }
.timeline-icon { font-size: 1.1rem; width: 28px; flex-shrink: 0; }
.timeline-phase {
    color: var(--emerald);
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    margin-bottom: 0.15rem;
}
.timeline-desc { color: var(--cream); font-size: 0.86rem; }

/* Crops */
.crop-col {
    padding: 1rem 1.2rem;
    background: linear-gradient(145deg, #FFFFFF, #F0F3E9);
    border: 1px solid var(--line);
    border-radius: 14px;
}
.crop-name {
    color: var(--emerald);
    font-weight: 800;
    font-size: 1rem;
    margin-bottom: 0.55rem;
}
.crop-disease-healthy {
    color: #287A4A;
    font-size: 0.83rem;
    margin-bottom: 0.3rem;
}
.crop-disease-sick {
    color: #A43D35;
    font-size: 0.83rem;
    margin-bottom: 0.3rem;
}

/* Empty state and footer */
.empty-state { padding: 3.5rem 2rem; text-align: center; }
.empty-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.7; }
.empty-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.6rem;
    color: var(--cream);
    margin-bottom: 0.4rem;
}
.empty-sub { color: var(--muted); font-size: 0.88rem; }

.app-footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.2rem;
    padding: 1.2rem 1rem;
    margin-top: 2rem;
    border-top: 1px solid var(--line);
}
.footer-item {
    color: var(--muted);
    font-size: 0.76rem;
}
.credits { text-align: center; padding: 1.4rem 1rem 0.5rem; }
.credits-label {
    color: var(--gold2);
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
}
.credits-names { color: var(--cream); font-size: 0.88rem; }
.credits-sep { color: var(--gold); margin: 0 0.4rem; }

.stImage img {
    border-radius: 12px;
    border: 1px solid var(--line);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: none; }
}
@keyframes growBar { from { width: 0; } }

@media (max-width: 768px) {
    .block-container { padding: 1rem !important; }
    .hero { padding: 1.2rem; }
    .hero-title { font-size: 2.2rem; }
    .hero-left { align-items: flex-start; }
    .hero-badge { width: 46px; height: 46px; }
    .section-card { padding: 1rem; }
    .nav-card { min-height: auto; }
}
</style>
"""

_FOOTER_HTML = """
<div class="app-footer">
  <div class="footer-item">✦ ResNet50 + CBAM</div>
  <div class="footer-item">✦ Plant Dataset</div>
  <div class="footer-item">✦ 10 Disease Classes</div>
  <div class="footer-item">✦ ≥94.0% Accuracy</div>
  <div class="footer-item">✦ Deep Learning </div>
</div>
<div class="credits">
  <div class="credits-label">Project Team</div>
  <div class="credits-names">
    Vansh Chaudhary
    <span class="credits-sep">·</span>
    Aarnav Arora
  </div>
</div>
"""


def inject_css() -> None:
    """Inject the shared page styling."""
    st.markdown(_CSS, unsafe_allow_html=True)


def footer() -> None:
    """Render the shared page footer."""
    st.markdown(_FOOTER_HTML, unsafe_allow_html=True)


def hero(
    icon: str,
    title: str,
    subtitle: str,
    chips: list[tuple[str, str]] | None = None,
) -> None:
    """Render the shared hero banner."""
    chips_html = ""
    if chips:
        for label, cls in chips:
            dot = '<span class="dot"></span>' if not cls else ""
            chips_html += (
                f'<span class="stat-chip {cls}">{dot}{label}</span>'
            )

    st.markdown(
        f"""
        <div class="glass hero">
          <div class="hero-row">
            <div class="hero-left">
              <div class="hero-badge">{icon}</div>
              <div>
                <div class="hero-title">{title}</div>
                <div class="hero-subtitle">{subtitle}</div>
                <div class="byline">
                  Project Team:
                  <b>Vansh Chaudhary</b>
                  <span class="sep">·</span>
                  <b>Aarnav Arora</b>
                </div>
              </div>
            </div>
            <div class="hero-stats">{chips_html}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
