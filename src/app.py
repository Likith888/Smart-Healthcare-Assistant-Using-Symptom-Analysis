from disease_prediction import train_model, predict_disease

def main():
    print("Smart Healthcare Assistant Using Symptom Analysis")
    print("Enter symptoms separated by commas (example: fever, cough, headache)")
    
    symptoms = input("Symptoms: ")
    
    model = train_model()
    prediction = predict_disease(model, symptoms)
    
    print("\nPredicted Disease:", prediction)
    print("Advice: If symptoms persist, please consult a doctor.")

if __name__ == "__main__":
    main()