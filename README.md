# Titanium Alloy Beta Stability Index Calculator

A professional scientific web application for calculating the **Molybdenum equivalent (Mo_eq)**, **Aluminum equivalent (Al_eq)**, and **Beta Stability Index (SIβ)** of titanium alloys based on composition in weight percent (wt%).

This tool is designed for **materials scientists, metallurgists, and researchers** working on titanium alloy design and phase stability analysis.

---

# Features

## Core Functionality

* Calculate:

  * Molybdenum equivalent (Mo_eq)
  * Aluminum equivalent (Al_eq)
  * Beta Stability Index (SIβ)

* User-friendly web interface

* Real-time calculation

* Scientific visualization

---

## Advanced Features

* Alloy presets (Ti-6Al-4V, Ti-5553, Beta-C, etc.)
* Batch processing via CSV upload
* Export results to CSV
* Interactive plots
* Modular scientific backend

---

# Scientific Background

The beta stability index is defined as:

SIβ = Mo_eq − Al_eq

Where:

Mo_eq =
Mo

* 0.67 V
* 0.44 W
* 0.28 Nb
* 0.22 Ta
* 2.9 Fe
* 1.6 Cr
* 1.25 Ni
* 1.7 (Mn + Co)

Al_eq =
Al

* (1/3) Sn
* (1/6) Zr
* 10 (C + O + 2N)

All values are in weight percent (wt%).

---

# Installation

## Step 1: Clone or download project

```
git clone https://github.com/yourusername/beta-stability-calculator.git

cd beta-stability-calculator
```

or manually download and extract.

---

## Step 2: Create virtual environment (recommended)

Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

Linux / Mac:

```
python3 -m venv .venv
source .venv/bin/activate
```

---

## Step 3: Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

IMPORTANT: Do NOT run using python directly.

Correct command:

```
streamlit run app.py
```

The application will open automatically in your browser:

```
http://localhost:8501
```

---

# Project Structure

```
beta_stability_app/

│── app.py
│── calculator.py
│── presets.py
│── requirements.txt
│── README.md
```

---

# CSV Batch Mode Format

Example CSV file:

```
Al,V,Mo,Cr,Fe
6,4,0,0,0
5,5,5,3,0
3,10,0,0,2
```

Output will include:

```
Mo_eq
Al_eq
SI_beta
```

---

# Example Usage

1. Launch application
2. Enter alloy composition
3. Click "Calculate"
4. View results and plots
5. Export if needed

---

# Requirements

Python 3.9 or newer

Libraries:

* streamlit
* pandas
* matplotlib

---

# Intended Users

* Materials scientists
* Metallurgical researchers
* Titanium alloy designers
* Graduate students
* Research laboratories

---

# Future Planned Features

* Phase classification (α, α+β, β)
* Alloy database
* Composition optimizer
* Machine learning prediction
* PDF report export
* Online deployment support

---

# License

MIT License

---

# Author

Developed for scientific and research use in titanium alloy phase stability analysis.

---

# Citation (if used in research)

If you use this tool in published work, please cite appropriately and reference the beta stability index methodology used in titanium alloy literature.
