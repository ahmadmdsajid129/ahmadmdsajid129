<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,20&height=230&section=header&text=MD%20SAJID%20AHMAD&fontSize=54&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Physics%20%C3%97%20Machine%20Learning%20%C3%97%20Markets&descSize=20&descAlignY=60" width="100%" alt="banner" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=900&color=3DDBB0&center=true&vCenter=true&width=760&lines=I+score+transactions+in+under+100+ms.;I+simulate+order+books+and+try+to+break+my+own+alpha.;I+price+exotic+options+with+Monte+Carlo.;I+ship+full-stack+marketplaces+for+real+clients.;Looking+for%3A+AI%2FML+internship+%7C+Quant+Research." alt="typing" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=ahmadmdsajid129&label=PROFILE+VIEWS&color=6C4CF1&style=for-the-badge" alt="views" />
<img src="https://img.shields.io/badge/SVNIT-Integrated%20M.Sc.%20Physics-14123A?style=for-the-badge" alt="svnit" />
<img src="https://img.shields.io/badge/Open%20to-AI%2FML%20Intern%20%7C%20Quant%20Research-3DDBB0?style=for-the-badge&labelColor=14123A" alt="open" />

</div>

---

## `$ python sajid.py --explain`

```python
class MDSajidAhmad:
    """Physics undergrad who treats every system as signal + noise."""

    base      = "SVNIT Surat, Integrated M.Sc. Physics (2024 - 2029)"
    thinks_in = ["probability", "stochastic calculus", "information theory"]
    ships_in  = ["Python", "C++", "TypeScript", "SQL"]

    def proven(self):
        return {
            "ml_in_production_shape": "fraud engine: Kafka, Redis, XGBoost, TreeSHAP, React",
            "quant_models":           "LOB simulator + Monte Carlo exotic options pricer",
            "client_work":            "full-stack marketplace, 11 months, real users' money flows",
        }

    def honesty_policy(self):
        # every number below is labelled: real, simulated, or synthetic
        return "I tell you what the data is. I tell you what the backtest can't prove."

    seeking = ("AI/ML internship", "Quantitative research role")
```

---

## 🎲 Today's market, simulated by my own engine

<sub>This image is regenerated every day by a GitHub Action running pure-Python Monte Carlo (antithetic variates) against the closed-form Black-Scholes price. If you are reading this tomorrow, the paths are different. The pricing error is live.</sub>

<div align="center">
  <img src="gbm.svg" width="100%" alt="Daily simulated GBM paths with Monte Carlo vs Black-Scholes error" />
</div>

---

## 🧪 Flagship projects

<table>
<tr>
<td width="50%" valign="top">

### 🛡️ Real-Time Payment Fraud Engine
`Python` `FastAPI` `XGBoost` `Kafka` `Redis` `PostgreSQL` `TreeSHAP` `React 19`

A streaming risk engine that turns raw card transactions into **APPROVE / REVIEW / BLOCK** decisions, with an explanation for every call.

| | |
|---|---|
| Champion XGBoost PR-AUC | **0.9825** |
| Isotonic calibration ECE | **0.0014** |
| End-to-end p95 latency | **92 ms** (250 live requests) |
| Automated tests | **61 / 61** |
| Commits | **114** |

**[→ Repository](https://github.com/ahmadmdsajid129/real-time-payment-fraud-detection)**

</td>
<td width="50%" valign="top">

### 📉 LOB Simulator & Market-Making Engine
`Python` `Pandas` `NumPy` `XGBoost`

An event-driven limit order book, microstructure features, an XGBoost alpha model, and a backtest that **stress-tests its own edge** with adverse selection.

| | |
|---|---|
| Order handling | O(1) `deque` queues |
| Features | OBI, micro-price, spread |
| Validation | strict chronological split |
| Out-of-sample accuracy | ~**67%** (simulated feed) |
| Key finding | edge dies when crossing the spread |

**[→ Repository](https://github.com/ahmadmdsajid129/lob-alpha-simulator)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧮 Exotic Options Pricing Engine
`Python` `FastAPI` `NumPy` `Next.js` `TypeScript` `Recharts`

Monte Carlo pricer for **European, Asian and barrier** options under GBM, with variance reduction and Greeks, behind a trading-desk-style dashboard.

| | |
|---|---|
| Variance reduction | antithetic + control variates |
| Sanity check | compared with Black-Scholes |
| Greeks | Delta, Vega (finite difference) |
| Interface | live path + risk visualisation |

**[→ Dashboard repo](https://github.com/ahmadmdsajid129/exotic-options-client)**

</td>
<td width="50%" valign="top">

### 🏔️ HimaVogue (client work)
`Next.js 14` `Node.js` `MongoDB` `Redis` `Docker` `eSewa`

A multi-vendor e-commerce platform I built as a freelance developer (Aug 2025 to Jul 2026): JWT + role-based auth, split-order logistics, vendor KYC, **commission and escrow ledger**, a bespoke-tailoring pipeline, and a Redis cache-aside layer.

| | |
|---|---|
| Roles | customer, seller, admin |
| Money flow | order, escrow, settlement, payout |
| Caching | Redis, graceful DB fallback |
| Delivery | 3-stage Docker build |

</td>
</tr>
</table>

<details>
<summary><b>🔬 Under the hood: fraud engine pipeline</b></summary>

```mermaid
flowchart LR
    C[Client] -->|POST /score| API[FastAPI gateway<br/>Pydantic V2 + idempotency]
    API --> R[(Redis<br/>ZSET windows<br/>Welford z-scores)]
    R --> F[30 behavioural features]
    F --> X[XGBoost]
    X --> I[Isotonic calibration]
    F --> IF[Isolation Forest]
    X --> S[TreeSHAP]
    I --> E{Risk engine<br/>0-100 score}
    IF --> E
    S --> E
    E -->|< 30| A[APPROVE]
    E -->|30 to 75| V[REVIEW]
    E -->|>= 75| B[BLOCK]
    E --> K[(Kafka topics<br/>+ DLQ)]
    K --> PG[(PostgreSQL)]
```

Design choices I would defend in an interview:

- **Zero temporal leakage.** Chronological splits, and Redis state is committed only *after* the current transaction is decided.
- **Cost-aware threshold.** Not 0.5. The cutoff minimises `FN x (amount + chargeback) + FP x insult cost`.
- **Explainability on every decision**, with PSI and KS drift monitoring across all 30 features.

</details>

<details>
<summary><b>🔬 Under the hood: what the LOB backtest taught me</b></summary>

A naive mid-price backtest looked great. Then I added the frictions:

1. Cross the spread and pay taker fees: **the edge disappears.**
2. Pivot to passive quoting with simulated **adverse selection**: ~35% fill on winning quotes, 100% fill on losing ones.
3. Use model probability (>60%) only to choose *which side to quote*, a defensive use of alpha.

The lesson was the point of the project: a Sharpe ratio means nothing until you have tried to destroy it.

</details>

---

## ➗ The math I actually use

<table>
<tr>
<td width="50%" valign="top">

**Pricing: Geometric Brownian Motion**

$$dS_t = rS_t\,dt + \sigma S_t\,dW_t$$

$$S_T = S_0\exp\!\Big[\big(r-\tfrac{\sigma^2}{2}\big)T+\sigma\sqrt{T}\,Z\Big]$$

$$\hat C = e^{-rT}\,\frac1N\sum_{i=1}^{N}\tfrac12\Big[(S_T^{+}-K)^+ + (S_T^{-}-K)^+\Big]$$

<sub>Antithetic pairs use $Z$ and $-Z$. Control variate: $\hat C_{cv}=\hat C-\beta(\hat Y-\mathbb E[Y])$.</sub>

$$\Delta \approx \frac{C(S_0+h)-C(S_0-h)}{2h}$$

</td>
<td width="50%" valign="top">

**Microstructure signals**

$$\text{OBI}=\frac{V_b-V_a}{V_b+V_a}\qquad P_{\text{micro}}=\frac{P_bV_a+P_aV_b}{V_a+V_b}$$

**Fraud risk arbitration**

$$S=100\big(0.55\,P_{\text{ML}}+0.15\,S_{\text{anom}}+0.15\,S_{\text{beh}}+0.15\,S_{\text{rules}}\big)$$

**Explainability (TreeSHAP)**

$$f(x)-\mathbb E[f]=\sum_{j=1}^{M}\phi_j(x)$$

</td>
</tr>
</table>

---

## 🧬 In the lab right now: **Oddly** *(codename, in design)*

> **Someone out there is oddly like you.**

A daily five-pick game, the same five questions for everyone on Earth, that finds the one stranger who answered most like you. No chat, no profile, a 30-second ritual with a shareable result. I am designing it as a **web-first PWA**, then native.

The part I am enjoying most is the maths. Matching on a rare answer should count for more than matching on a coin flip, so each answer is weighted by its information content:

$$I(a)=\log_2\frac{1}{p(a)}\qquad S(u,v)=\frac{\sum_q w_q\,s_q}{\sum_q w_q},\quad w_q=\frac{I(a_u)+I(a_v)}{2}$$

And a result I derived and checked by simulation: with $N$ daily players and a question set of entropy $H$ bits, the expected number of exact twins is about

$$\mathbb E[\text{exact twins}]\approx\frac{N}{2^{H}}$$

so the question set has to grow with the crowd, or "your perfect twin" stops meaning anything. *(Status: blueprint and simulations done, build starting. Nothing validated with real users yet, and I say so.)*

---

## 🛠️ Arsenal

<div align="center">

**Quant & ML**

<img src="https://skillicons.dev/icons?i=python,cpp,sklearn,pandas,numpy" />
<img src="https://img.shields.io/badge/XGBoost-337AB7?style=for-the-badge" />
<img src="https://img.shields.io/badge/SHAP-FF6B5E?style=for-the-badge" />
<img src="https://img.shields.io/badge/Monte%20Carlo-6C4CF1?style=for-the-badge" />
<img src="https://img.shields.io/badge/Matplotlib-14123A?style=for-the-badge" />

**Backend & Data**

<img src="https://skillicons.dev/icons?i=fastapi,nodejs,express,mongodb,postgres,redis,kafka,prisma,docker" />

**Frontend**

<img src="https://skillicons.dev/icons?i=nextjs,react,ts,js,tailwind,html,css" />

**Tools**

<img src="https://skillicons.dev/icons?i=git,github,linux,vscode,postman" />

</div>

---

## 📊 Commits, streaks, and the whole history

<div align="center">

<img src="https://streak-stats.demolab.com/?user=ahmadmdsajid129&background=14123A&ring=3DDBB0&fire=FF6B5E&currStreakLabel=3DDBB0&currStreakNum=EEEAFE&sideLabels=EEEAFE&sideNums=EEEAFE&dates=9A97C0&stroke=6C4CF1&border=6C4CF1" width="540" alt="streak" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ahmadmdsajid129/ahmadmdsajid129/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ahmadmdsajid129/ahmadmdsajid129/output/github-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/ahmadmdsajid129/ahmadmdsajid129/output/github-snake.svg" width="98%" />
</picture>

<br/>

<img src="https://img.shields.io/github/commit-activity/t/ahmadmdsajid129/real-time-payment-fraud-detection?label=fraud%20engine%20commits&color=3DDBB0&labelColor=14123A&style=for-the-badge" alt="fraud%20engine%20commits" />
<img src="https://img.shields.io/github/commit-activity/t/ahmadmdsajid129/lob-alpha-simulator?label=LOB%20sim%20commits&color=FF6B5E&labelColor=14123A&style=for-the-badge" alt="LOB%20sim%20commits" />
<img src="https://img.shields.io/github/commit-activity/t/ahmadmdsajid129/exotic-options-client?label=options%20client%20commits&color=6C4CF1&labelColor=14123A&style=for-the-badge" alt="options%20client%20commits" />

<img src="https://img.shields.io/github/languages/top/ahmadmdsajid129/real-time-payment-fraud-detection?label=fraud%20engine&color=6C4CF1&labelColor=14123A&style=for-the-badge" alt="fraud%20engine" />
<img src="https://img.shields.io/github/languages/top/ahmadmdsajid129/lob-alpha-simulator?label=LOB%20sim&color=6C4CF1&labelColor=14123A&style=for-the-badge" alt="LOB%20sim" />
<img src="https://img.shields.io/github/languages/top/ahmadmdsajid129/exotic-options-client?label=options%20client&color=6C4CF1&labelColor=14123A&style=for-the-badge" alt="options%20client" />

<img src="https://img.shields.io/github/followers/ahmadmdsajid129?style=for-the-badge&color=3DDBB0&labelColor=14123A" alt="followers" />

</div>

---

## 🧭 How I work

```mermaid
flowchart LR
    A[Physics lens<br/>signal, noise, limits] --> B[ML systems<br/>XGBoost, SHAP, drift]
    A --> C[Quant models<br/>GBM, LOB, Greeks]
    B --> D[Ship it<br/>FastAPI, Kafka, Redis, React]
    C --> D
    D --> E((AI/ML intern<br/>or Quant Research))
```

- **Label the data.** Synthetic, simulated or real, it is written next to every number.
- **Try to break it first.** Chronological splits, adverse selection, drift checks.
- **Make it explain itself.** SHAP in the fraud engine, error bars in the pricer.
- **Then build the interface**, because a model nobody can use is a notebook.

<details>
<summary><b>🏋️ Off the keyboard</b></summary>
<br/>
Deadlifts and bench press, working on the bulk. Progressive overload and gradient descent turn out to be the same idea.
</details>

---

## 📫 Let's talk

I am looking for an **AI/ML internship** or a **quantitative research** role. If you have a problem with noisy data and a hard latency or risk constraint, send it over.

<div align="center">
  <a href="https://www.linkedin.com/in/md-sajid-ahmad-350a9b32a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:ahmadmdsajid129@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,20&height=120&section=footer" width="100%" alt="footer" />
