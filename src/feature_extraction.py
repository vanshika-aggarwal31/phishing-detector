import re
from urllib.parse import urlparse

def extract_features(url):
    features = {}
    
    # URL length
    features['url_length'] = len(url)
    
    # Has IP address instead of domain
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0
    
    # Count of dots
    features['dot_count'] = url.count('.')
    
    # Count of special characters
    features['special_char_count'] = len(re.findall(r'[@#$%^&*()+=\[\]{}|\\:;<>?/]', url))
    
    # Has HTTPS
    features['has_https'] = 1 if url.startswith('https') else 0
    
    # URL depth (number of slashes)
    features['url_depth'] = url.count('/')
    
    # Has suspicious words
    suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'banking', 'confirm']
    features['has_suspicious_words'] = 1 if any(word in url.lower() for word in suspicious_words) else 0
    
    # Domain length
    try:
        parsed = urlparse(url)
        features['domain_length'] = len(parsed.netloc)
    except:
        features['domain_length'] = 0
    
    return features