
# 💰 Personal Finance Analyzer

A simple Streamlit app that helps you analyze your personal M-Pesa or bank transactions using **clustering** and **data science techniques**.

---

## 📦 Features

- 📤 Upload **CSV** or **PDF** bank/M-Pesa statements  
- 🔍 Automatically preprocess and cluster your expenses into categories (e.g., Food, Transport, Utilities) using **K-Means**
- 📊 View spending patterns via interactive charts
- ⬇️ Download cleaned and clustered data as CSV
- 🧠 Built with **pandas**, **scikit-learn**, **matplotlib**, and **Streamlit**

---

## 🚀 Getting Started

```bash
git clone https://github.com/deuce01/personal-finance-analyzer.git
cd personal-finance-analyzer
pip install -r requirements.txt
streamlit run app.py
````

---

## 📁 Folder Structure

```
personal_finance_analyzer/
├── app.py                 # Main Streamlit app logic
├── cluster_model.py       # K-Means clustering logic
├── data/
│   └── sample_mpesadata.csv
├── utils.py               # Preprocessing, plotting
├── requirements.txt       # Dependencies
└── README.md              # Project description
```

---

## ⚠️ Notes

* ✅ Works best with **CSV** files from M-Pesa or bank exports
* 🔒 **Encrypted PDFs** are not yet supported (I’m still figuring out how to handle them)

---

## 📚 Learning Objectives

This project was built for hands-on learning with:

* 🔹 Clustering algorithms (K-Means)
* 🔹 Exploratory Data Analysis (EDA)
* 🔹 Real-world data cleaning & visualization
* 🔹 Streamlit app building

---

## 📬 Feedback or Suggestions?

Feel free to open an issue or contribute!

```

---

Would you like me to push this to your repo or help you style it further (e.g., badges, screenshots)?
```
