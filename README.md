🫧 Kirei Kirei — Mumbai Market Entry Strategy Dashboard

An interactive, data-driven Go-To-Market strategy tool for **Kirei Kirei** (キレイキレイ), LION Corporation's #1 Japanese hand soap brand, exploring its entry into Mumbai's hand hygiene market.

Built as a final year B.Sc. Data Science project, this app turns a real 800-respondent Mumbai consumer survey into an interactive business intelligence dashboard covering consumer segmentation, competitive positioning, marketing strategy generation, and financial simulation.

> 🎓 Final Year Project — B.Sc. Data Science, S. M. Shetty College of Science, Commerce & Management Studies (Autonomous), Mumbai (2025–26)

---

📖 Overview

India's hand hygiene market is growing at a ~9.2% CAGR, with rising incomes and a growing consumer affinity for Japanese brands creating a white-space opportunity for a premium, foam-format, antibacterial hand soap. This project builds a full analytical case for whether — and how — Kirei Kirei should enter this market, with Mumbai as the launch city.

The dashboard combines:
- Consumer segmentation** via a Random Forest Classifier on income and brand-affinity signals
- Competitive intelligence** on incumbent brands (Dettol, Dove, Palmolive, Godrej Protekt, and others)
- A rules-based Go-To-Market strategy generator** covering pricing, marketing, channels, and retention
- An interactive financial simulator** modeling Year 1 profit under different pricing and marketing scenarios

✨ Features

| Page / Tab Description |

| 🏠 Landing Page | Animated brand introduction with product highlights and value proposition |
| 🎯 Market Data | Strategic insight cards, competitive market share (total vs. high-income segment), interactive D3.js competitive intelligence chart |
| 📊 Segmentation | Consumer density heatmap, Random Forest–driven segment classification (Modernist Elite / Aspirational Climber / Value Seeker) |
| 📈 Data-Driven Strategy Engine | Rule-based chatbot answering strategy questions + full downloadable GTM Master Strategy report (Markdown) |
| 💰 Financial Simulator | Adjustable pricing, marketing spend, and profit-goal sliders with a live Year 1 profit gauge and ROI projection |

🧠 Methodology

1. EDA & Competitive Mapping** — distribution analysis, brand usage frequencies, and income-vs-channel cross-tabulation across the survey data.
2. Feature Engineering** — `Income_Norm` and `Bias_Norm` (z-score normalized), combined into a composite `Premium_Score = (Income_Norm × 0.6) + (Bias_Norm × 0.4)`.
3. Segmentation** — a rule-based percentile split on income and Japanese Brand Bias defines three consumer segments, chosen for business-explainability over black-box clustering.
4. Classification** — a `RandomForestClassifier` (100 estimators, `max_depth=2`, `min_samples_leaf=15`, `min_samples_split=20`) is trained on 5 engineered features with a 75/25 stratified split to predict segment membership.
5. Strategy Generation** — segmentation and competitive outputs feed a templated GTM report covering pricing, marketing, channel, and retention strategy.

📊 Dataset

- 800 respondents** across 5 Mumbai micro-markets: South Mumbai, Western Suburbs, Eastern Suburbs, Navi Mumbai, and Thane.
- 9 core variables: age, family size, location, monthly income, current brand, replacement frequency, primary purchase channel, willingness to pay a premium, and Japanese brand affinity.
- The public version of this dataset (`KireiKirei_ConsumerData.csv`) is a **synthetic dataset modeled on the statistical properties of the original survey** — it does not contain the original respondent-level or commercial data. See [Data & Confidentiality Note](#-data--confidentiality-note) below.

🛠️ Tech Stack

- Language:** Python 3.10+
- Web Framework:** Streamlit 1.31
- Data Processing:** Pandas 2.1, NumPy 1.26
- Machine Learning:** scikit-learn 1.3 (Random Forest Classifier)
- Visualization:** Plotly Express & Graph Objects 5.18, D3.js v7.8.5 (embedded via `components.html()`)
- Styling:** Custom CSS injected via `st.markdown()`, Google Fonts (Fredoka One, Nunito)

🚀 Getting Started

  Prerequisites
- Python 3.10 or higher
- pip

### Installation

```bash
git clone https://github.com/<your-username>/kirei-kirei-mumbai-strategy.git
cd kirei-kirei-mumbai-strategy
pip install -r requirements.txt
```

### Running the app

```bash
streamlit run appintro.py
```

The landing page will open at `http://localhost:8501`. Navigate to the dashboard from there to explore the analytics tabs.

## 📁 Project Structure

```
├── appintro.py                    # Landing / brand introduction page
├── pages/
│   └── app.py                     # Main 4-tab analytics dashboard
├── data/
│   └── KireiKirei_ConsumerData.csv  # Synthetic consumer dataset (800 rows)
├── requirements.txt
└── README.md
```

## ⚠️ Limitations

- The financial simulator's assumptions (conversion rates, margins, market sizing) are illustrative scenario outputs, not guaranteed forecasts.
- The Modernist Elite segment's near-universal "willingness to pay a premium" response is partly a function of how the segment itself is defined (income + brand affinity), and should be read with that circularity in mind.
- The D3.js competitive chart runs inside a sandboxed iframe and currently cannot trigger cross-tab filtering elsewhere in the dashboard — a noted direction for future work.
- The dataset reflects a single point-in-time survey (Jan–Feb 2026) and has not been re-validated against more recent market conditions.

## 🔒 Data & Confidentiality Note

This project was developed with guidance from an industry contact involved in importing a Japanese hand soap brand into India, who shared general, non-identifying context on the category and helped validate the survey design. **No proprietary company data — cost, margin, customs, or vendor-specific figures — is published in this repository.** All numbers used in the app are either derived from the public survey dataset or represent generic, illustrative assumptions for demonstration purposes. The CSV included here is a synthetic dataset generated to match the statistical distribution of the original 800-respondent survey.

## 👩‍💻 Author

**Rachel Elaine Soares**
B.Sc. Data Science

## 📄 License

This project is submitted as part of an academic curriculum. please don't submit it as your own work
