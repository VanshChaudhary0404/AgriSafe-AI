
"""
AgriSafe AI — Home Page
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import inject_css, hero, footer

st.set_page_config(
    page_title="AgriSafe AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# ── Hero ─────────────────────────────────────────────────────────────────────
hero(
    icon="🌿",
    title="AgriSafe AI",
    subtitle=(
        "Smarter Crop Health. A Greener Future. · "
        "Explainable Deep Learning for Crop Protection"
    ),
    chips=[
        ("Model Online", ""),
        ("≥94.0% Accuracy", "gold"),
        ("ResNet50 + CBAM", ""),
        ("10 Classes", "gold"),
    ],
)

# ── Metrics ──────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)

c1.metric("Test Accuracy", "≥ 94.0%", "+30.1 pp vs MLP")
c2.metric("Macro F1-Score", "≥ 0.910", "+0.355 vs MLP")
c3.metric("ROC-AUC", "≥ 0.980", "+0.040 vs MLP")
c4.metric("Potato Healthy F1", "≥ 0.700", "+0.700 via VAE")

# ── About ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="glass section-card" style="margin-top:1.1rem;">
  <div class="section-title">About AgriSafe AI</div>
  <p style="color:var(--cream); font-size:0.94rem; line-height:1.8; margin:0;">
    AgriSafe AI is an AI-powered crop disease analysis system designed to support
    <strong style="color:var(--emerald);">
    disease classification, visual explanations, severity estimation,
    and treatment recommendations</strong> using deep learning.
  </p>
  <p style="color:var(--cream); font-size:0.94rem; line-height:1.8; margin:0.7rem 0 0;">
    <strong style="color:var(--gold2);">Core architecture:</strong>
    ResNet50 with Convolutional Block Attention Modules (CBAM), using the trained
    model to classify supported tomato, potato, pepper, and corn leaf images.
  </p>
</div>
""", unsafe_allow_html=True)


# ── Key Innovations ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title" style="margin-top:0.9rem;">Key Innovations</div>',
            unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
    <div class="glass section-card" style="border-top:3px solid #347650;">
      <div style="color:#174D35;font-weight:700;">🎯 CBAM Attention</div>
      <p style="color:#43594A;font-size:0.84rem;line-height:1.6;">
        Localises disease lesions for Grad-CAM explainability.
      </p>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="glass section-card" style="border-top:3px solid #C49A45;">
      <div style="color:#805A17;font-weight:700;">🔬 VAE Augmentation</div>
      <p style="color:#43594A;font-size:0.84rem;line-height:1.6;">
        Addresses Potato Healthy class imbalance (152 → 664 images, FID=42.7).
      </p>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="glass section-card" style="border-top:3px solid #347650;">
      <div style="color:#174D35;font-weight:700;">⚡ Optuna HPO</div>
      <p style="color:#43594A;font-size:0.84rem;line-height:1.6;">
        30 Bayesian TPE trials identify optimal hyperparameters.
      </p>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="glass section-card" style="border-top:3px solid #C49A45;">
      <div style="color:#805A17;font-weight:700;">🌿 HSV Severity</div>
      <p style="color:#43594A;font-size:0.84rem;line-height:1.6;">
        Quantifies disease extent as a percentage of leaf area.
      </p>
    </div>
    """, unsafe_allow_html=True)


# ── Navigation Cards ─────────────────────────────────────────────────────────
st.markdown("""
<div class="section-title" style="margin-top:1.4rem;">
    Explore the Dashboard
</div>
""", unsafe_allow_html=True)

n1, n2, n3 = st.columns(3)

with n1:
    st.markdown("""
    <div class="glass nav-card">
      <div class="icon">🔬</div>
      <div class="title">Diagnose</div>
      <div class="desc">
        Upload a leaf image to detect disease, visualise Grad-CAM attention,
        estimate severity, and receive a treatment plan.
      </div>
      <div class="arrow">Disease detection and explanations →</div>
    </div>
    """, unsafe_allow_html=True)

with n2:
    st.markdown("""
    <div class="glass nav-card" style="border-top-color:#C49A45;">
      <div class="icon">📊</div>
      <div class="title">Analytics</div>
      <div class="desc">
        Explore the PlantVillage dataset, class distributions, RGB channel
        analysis, PCA/t-SNE feature visualisations, and augmentation demos.
      </div>
      <div class="arrow">Explore dataset insights →</div>
    </div>
    """, unsafe_allow_html=True)

with n3:
    st.markdown("""
    <div class="glass nav-card">
      <div class="icon">📈</div>
      <div class="title">Performance</div>
      <div class="desc">
        Review model performance across phases, per-class F1 scores,
        confusion matrices, ROC curves, and robustness analysis.
      </div>
      <div class="arrow">Review model evaluation →</div>
    </div>
    """, unsafe_allow_html=True)

# ── Supported Diseases ───────────────────────────────────────────────────────
st.markdown("""
<div class="section-title" style="margin-top:1.4rem;">
    Supported Crops &amp; Diseases
</div>
""", unsafe_allow_html=True)

crops = {
    ("🍅", "Tomato"): [
        ("Early Blight", False),
        ("Late Blight", False),
        ("Healthy", True),
    ],
    ("🥔", "Potato"): [
        ("Early Blight", False),
        ("Late Blight", False),
        ("Healthy", True),
    ],
    ("🌶️", "Pepper"): [
        ("Bacterial Spot", False),
        ("Healthy", True),
    ],
    ("🌽", "Corn"): [
        ("Common Rust", False),
        ("Healthy", True),
    ],
}

dcols = st.columns(4)

for col, ((icon2, cname), diseases) in zip(dcols, crops.items()):
    with col:
        rows = "".join(
            f'<div class="{"crop-disease-healthy" if healthy else "crop-disease-sick"}">'
            f'{"●" if healthy else "●"} {disease}</div>'
            for disease, healthy in diseases
        )

        st.markdown(f"""
        <div class="glass crop-col">
          <div class="crop-name">{icon2} {cname}</div>
          {rows}
        </div>
        """, unsafe_allow_html=True)


# ── Development Timeline ─────────────────────────────────────────────────────
st.markdown(
    '<div class="section-title" style="margin-top:1.2rem;">Development Timeline</div>',
    unsafe_allow_html=True,
)

phases = [
    ("✅", "Phase 1", "Project Setup & Literature Review"),
    ("✅", "Phase 2", "EDA, Preprocessing & MLP Baseline (63.88%)"),
    ("✅", "Phase 3", "ResNet50 + CBAM CNN (92.1%)"),
    ("✅", "Phase 4", "Transfer Learning + VAE + HPO (≥94.0%)"),
    ("✅", "Phase 5", "Rigorous Evaluation, Ablations & Robustness"),
    ("🚀", "Phase 6", "Streamlit Dashboard & Final Deployment"),
]

for symbol, phase, description in phases:
    st.markdown(
        f"""
        <div class="glass timeline-item" style="padding:0.85rem 1.1rem;margin-bottom:0.5rem;border-radius:10px;">
            <div class="timeline-icon">{symbol}</div>
            <div>
                <div class="timeline-phase">{phase}</div>
                <div class="timeline-desc">{description}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

footer()
