# 🔐 Phishing URL Detector

A Machine Learning web application that detects malicious/phishing URLs with real-time threat scoring.

## 🚀 Live Demo
[Click here to view the app](https://phishing-detector-vanshika.streamlit.app)

## 📌 Features
- 🔍 Real-time URL scanning with threat score (0-100)
- 🤖 3 ML models compared — Random Forest, SVM, Logistic Regression
- 📊 Interactive model performance comparison dashboard
- ⚠️ Risk level detection — High, Medium, Safe

## 🏆 Model Performance
| Model | Accuracy |
|-------|----------|
| Random Forest | 96.92% |
| SVM | 95.12% |
| Logistic Regression | 93.35% |

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Streamlit
- Pandas
- Matplotlib
- Joblib

## 📂 Project Structure
## 📂 Project Structure
phishing-detector/
├── app.py
├── requirements.txt
├── src/
│   ├── feature_extraction.py
│   ├── model.py
│   ├── threat_score.py
│   └── __init__.py
├── models/
└── data/

## ⚙️ Run Locally
git clone https://github.com/vanshika-aggarwal31/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
streamlit run app.py

## 👩‍💻 Author
**Vanshika Aggarwal** — [LinkedIn](https://linkedin.com/in/vanshika-aggarwal31)