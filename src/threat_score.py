import joblib
from src.feature_extraction import extract_features

def calculate_threat_score(url):
    features = extract_features(url)
    
    score = 0
    
    # URL length penalty
    if features['url_length'] > 75:
        score += 20
    elif features['url_length'] > 50:
        score += 10
    
    # IP address in URL
    if features['has_ip'] == 1:
        score += 25
    
    # No HTTPS
    if features['has_https'] == 0:
        score += 20
    
    # Suspicious words
    if features['has_suspicious_words'] == 1:
        score += 20
    
    # Too many special characters
    if features['special_char_count'] > 5:
        score += 10
    elif features['special_char_count'] > 2:
        score += 5
    
    # Too many dots
    if features['dot_count'] > 4:
        score += 10
    
    # Short domain
    if features['domain_length'] < 5:
        score += 10
    
    # Cap at 100
    score = min(score, 100)
    
    # Threat level
    if score >= 70:
        level = "🔴 High Risk"
        color = "red"
    elif score >= 40:
        level = "🟡 Medium Risk"
        color = "orange"
    else:
        level = "🟢 Safe"
        color = "green"
    
    return {
        'score': score,
        'level': level,
        'color': color,
        'features': features
    }