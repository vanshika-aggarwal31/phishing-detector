import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

def load_data():
    df = pd.read_csv('data/phishing.csv')
    return df

def prepare_features(df):
    X = df.drop(['Index', 'class'], axis=1)
    y = df['class']
    return X, y

def train_models(X_train, y_train):
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'SVM': SVC(probability=True, random_state=42)
    }
    
    trained = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained[name] = model
    
    return trained

def evaluate_models(trained_models, X_test, y_test):
    results = {}
    for name, model in trained_models.items():
        preds = model.predict(X_test)
        results[name] = {
            'accuracy': round(accuracy_score(y_test, preds) * 100, 2),
            'precision': round(precision_score(y_test, preds, average='weighted') * 100, 2),
            'recall': round(recall_score(y_test, preds, average='weighted') * 100, 2)
        }
    return results

def save_best_model(trained_models, X_test, y_test):
    best_name = None
    best_acc = 0
    
    for name, model in trained_models.items():
        acc = accuracy_score(y_test, model.predict(X_test))
        if acc > best_acc:
            best_acc = acc
            best_name = name
    
    best_model = trained_models[best_name]
    joblib.dump(best_model, 'models/phishing_model.pkl')
    return best_name, best_acc