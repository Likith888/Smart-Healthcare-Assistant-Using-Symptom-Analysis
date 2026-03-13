def process_symptoms(text):
    symptoms = [s.strip().lower() for s in text.split(",")]
    return symptoms