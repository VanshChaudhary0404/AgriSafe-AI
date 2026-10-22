# 🌿 AgriSafe AI

**Explainable deep learning for automated crop disease classification, severity estimation, and treatment recommendations.**

[![CI](https://github.com/noir-scale/AgriSafe-AI/actions/workflows/ci.yml/badge.svg)](https://github.com/noir-scale/AgriSafe-AI/actions)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://python.org)
[![PyTorch 2.1](https://img.shields.io/badge/PyTorch-2.1-orange.svg)](https://pytorch.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red.svg)](https://streamlit.io)

**GitHub:** https://github.com/noir-scale/AgriSafe-AI

---

## Overview

AgriSafe AI is a crop disease analysis application that classifies diseases in tomato, potato, pepper, and corn leaves from an image. It uses Grad-CAM visualizations to help explain predictions, estimates disease severity as a percentage of affected leaf area, and provides treatment recommendations.

The application combines deep learning, model explainability, image analysis, and a Streamlit interface to support crop disease assessment.

## Key Results

| Metric | Phase 2 (MLP) | Phase 3 (CNN) | Phase 4 (Final) |
|---|---:|---:|---:|
| Test Accuracy | 63.88% | 92.1 ± 0.3% | ≥94.0% |
| Macro F1-Score | 0.555 | 0.882 ± 0.003 | ≥0.910 |
| ROC-AUC | 0.940 | 0.973 ± 0.002 | ≥0.980 |
| Potato Healthy F1 | 0.000 | ~0.500 | ≥0.700 (VAE fix) |

*These figures reflect the project's existing reported results and targets. Consult the results documentation for details.*

---

## Features

- **Disease classification:** Predicts a disease class and confidence score.
- **Grad-CAM explainability:** Visualizes image regions influencing a model prediction.
- **Severity estimation:** Estimates the affected leaf area and assigns a severity stage.
- **Treatment recommendations:** Provides treatment options, organic alternatives, and prevention guidance.
- **Analytics dashboard:** Displays dataset and model evaluation information.
- **Performance dashboard:** Presents model performance metrics.

## Supported Diseases (10 Classes)

| Crop | Classes |
|---|---|
| 🍅 Tomato | Early Blight, Late Blight, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🌶️ Pepper | Bacterial Spot, Healthy |
| 🌽 Corn (Maize) | Common Rust, Healthy |

---

## Installation

### Requirements

- Python 3.10 or later
- 4 GB RAM minimum; 8 GB recommended
- GPU optional

### 1. Clone the repository

```bash
git clone https://github.com/noir-scale/AgriSafe-AI.git
cd AgriSafe-AI
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Obtain the model checkpoint

The trained model checkpoint is not included in this Git repository because of its size. The application requires the compatible checkpoint at:

```text
checkpoints/cropguard_resnet50_cbam_phase3.pt
```

Obtain the checkpoint from the project's configured model-hosting source and place it at that path. The model download source must be verified and configured before a fresh installation can run inference.

### 5. Launch the application

```bash
streamlit run app/Home.py
```

Open the local URL displayed in the terminal.

---

## Docker

Build and run the application using the repository's Dockerfile:

```bash
docker build -t agrisafe-ai .
docker run -p 8501:8501 agrisafe-ai
```

Open http://localhost:8501 in your browser.

The compatible model checkpoint must also be available to the container at the configured model path.

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## Repository Structure

```text
AgriSafe-AI/
├── app/
│   ├── Home.py
│   ├── theme.py
│   └── pages/
│       ├── 1_Diagnose.py
│       ├── 2_Analytics.py
│       └── 3_Performance.py
├── checkpoints/
├── data/
│   └── processed/
├── docs/
├── notebooks/
├── notebooks_html/
├── src/
│   ├── model.py
│   ├── train.py
│   ├── gradcam.py
│   ├── severity.py
│   ├── treatment.py
│   └── utils.py
├── tests/
├── .github/
├── Dockerfile
├── requirements.txt
├── CITATION.cff
├── LICENSE
└── README.md
```

---

## Model Architecture

**ResNet50 + dual CBAM attention + three-layer classification head**

The documented architecture includes:

1. A ResNet50 backbone with ImageNet-pretrained weights.
2. CBAM channel and spatial attention modules.
3. Global average pooling and a fully connected classification head.
4. Batch normalization, ReLU activation, and dropout.
5. Grad-CAM-based model explainability.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the architecture documentation.

## Key Techniques

- **CBAM attention:** Supports attention-based feature refinement.
- **VAE augmentation:** Generates synthetic samples to address class imbalance.
- **Differential learning rates:** Uses different learning rates for the backbone and classification head.
- **Hyperparameter optimization:** Uses Optuna for hyperparameter search.
- **HSV-based severity estimation:** Estimates the percentage of leaf area affected.

## Results and Evaluation

See [docs/RESULTS.md](docs/RESULTS.md) for the reported evaluation results and [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for deployment details.

## Project Team

- **Vansh Chaudhary**
- **Aarnav Arora**

## Citation

If you reference this project, use the repository link:

```text
AgriSafe AI. https://github.com/noir-scale/AgriSafe-AI
```

## License

See the [LICENSE](LICENSE) file for licensing terms. Third-party code, model assets, and datasets remain subject to their applicable licences and attribution requirements.

