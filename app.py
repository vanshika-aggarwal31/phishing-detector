import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from src.model import load_data, prepare_features, train_models, evaluate_models, save_best_model
from src.threat_score import calculate_threat_score
import joblib
import os

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Phishing URL Detector")
st.markdown("### Detect malicious URLs using Machine Learning")

# ── SIDEBAR ──
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🔍 URL Scanner", "🤖 Train Models", "📊 Model Comparison"])

# ── URL SCANNER ──
if page == "🔍 URL Scanner":
    st.subheader("Enter a URL to scan")
    url = st.text_input("URL", placeholder="https://example.com")
    
    if st.button("Scan URL"):
        if url:
            result = calculate_threat_score(url)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Threat Score", f"{result['score']}/100")
                st.markdown(f"## {result['level']}")
            
            with col2:
                st.subheader("URL Features Detected")
                features = result['features']
                st.write(f"✅ HTTPS: {'Yes' if features['has_https'] else 'No'}")
                st.write(f"📏 URL Length: {features['url_length']}")
                st.write(f"🔴 Has IP Address: {'Yes' if features['has_ip'] else 'No'}")
                st.write(f"⚠️ Suspicious Words: {'Yes' if features['has_suspicious_words'] else 'No'}")
                st.write(f"🔣 Special Characters: {features['special_char_count']}")
        else:
            st.warning("Please enter a URL!")

# ── TRAIN MODELS ──
elif page == "🤖 Train Models":
    st.subheader("Train ML Models on Phishing Dataset")
    
    if st.button("Start Training"):
        with st.spinner("Loading data..."):
            df = load_data()
            st.success(f"Dataset loaded! {len(df)} records found.")
        
        with st.spinner("Extracting features..."):
            X, y = prepare_features(df)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            st.success("Features extracted!")
        
        with st.spinner("Training 3 models..."):
            trained_models = train_models(X_train, y_train)
            st.success("Models trained!")
        
        with st.spinner("Evaluating..."):
            results = evaluate_models(trained_models, X_test, y_test)
            best_name, best_acc = save_best_model(trained_models, X_test, y_test)
            st.success(f"Best model: {best_name} with {round(best_acc*100, 2)}% accuracy!")
        
        st.session_state['results'] = results
        st.session_state['trained'] = True

# ── MODEL COMPARISON ──
elif page == "📊 Model Comparison":
    st.subheader("Model Performance Comparison")
    
    if 'results' not in st.session_state:
        st.warning("Please train models first!")
    else:
        results = st.session_state['results']
        
        models = list(results.keys())
        accuracy = [results[m]['accuracy'] for m in models]
        precision = [results[m]['precision'] for m in models]
        recall = [results[m]['recall'] for m in models]
        
        df_results = pd.DataFrame({
            'Model': models,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall
        })
        
        st.dataframe(df_results)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        x = range(len(models))
        ax.bar([i - 0.2 for i in x], accuracy, width=0.2, label='Accuracy', color='blue')
        ax.bar([i for i in x], precision, width=0.2, label='Precision', color='green')
        ax.bar([i + 0.2 for i in x], recall, width=0.2, label='Recall', color='red')
        ax.set_xticks(x)
        ax.set_xticklabels(models)
        ax.set_ylabel("Score (%)")
        ax.set_title("Model Comparison")
        ax.legend()
        st.pyplot(fig)


        