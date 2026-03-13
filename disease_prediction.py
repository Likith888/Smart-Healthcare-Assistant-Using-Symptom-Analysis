from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from symptom_processing import process_symptoms

def load_dataset():
    data = {
        "symptoms":[
            "fever cough headache",
            "fever cough fatigue",
            "headache nausea",
            "sneezing runny nose",
            "cough chest pain"
        ],
        "disease":[
            "Flu",
            "Flu",
            "Migraine",
            "Common Cold",
            "Bronchitis"
        ]
    }
    return pd.DataFrame(data)

def train_model():
    df = load_dataset()
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["symptoms"])
    y = df["disease"]
    
    model = MultinomialNB()
    model.fit(X, y)
    
    model.vectorizer = vectorizer
    return model

def predict_disease(model, symptom_text):
    processed = " ".join(process_symptoms(symptom_text))
    X_test = model.vectorizer.transform([processed])
    prediction = model.predict(X_test)[0]
    return prediction