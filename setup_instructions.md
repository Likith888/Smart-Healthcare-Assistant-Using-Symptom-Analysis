# Setup Instructions

Follow the steps below to run the Smart Healthcare Assistant Using Symptom Analysis project on your system.

## 1. Install Python
Make sure Python 3.8 or higher is installed on your system.

Check the Python version using:

```bash
python --version
```

## 2. Clone the Repository
Clone the project from GitHub to your local machine.

```bash
git clone https://github.com/yourusername/Smart-Healthcare-Assistant.git
```

Navigate to the project directory.

```bash
cd Smart-Healthcare-Assistant
```

## 3. Install Required Libraries
Install all dependencies using the requirements file.

```bash
pip install -r requirements.txt
```

## 4. Run the Application
Run the main Python program.

```bash
python src/app.py
```

## 5. Enter Symptoms
When the program starts, enter symptoms separated by commas.

Example:

```
fever, cough, headache
```

## 6. View Results
The system will analyze the symptoms using the Naïve Bayes Machine Learning model and display:

- Predicted disease
- Basic health advice
- Recommendation to consult a doctor if necessary

## Software Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

## Required Python Libraries
The following libraries are required for this project:

- numpy
- pandas
- scikit-learn
- nltk
- fastapi
- uvicorn
