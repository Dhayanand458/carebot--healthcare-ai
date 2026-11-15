
import json
from pathlib import Path

import pandas as pd


# Locate the project data folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_symptoms_data():
    """Load the healthcare symptoms CSV dataset."""

    file_path = DATA_DIR / "aiml_healthcare_symptoms.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_csv(file_path)


def clean_symptoms_data(df):
    """Validate and prepare the healthcare symptoms dataset."""

    required_columns = [
        "Patient_ID",
        "Age",
        "Gender",
        "Fever",
        "Cough",
        "Fatigue",
        "Breathlessness",
        "Chest_Pain",
        "Nausea",
        "Headache",
        "BMI",
        "BP_Systolic",
        "BP_Diastolic",
        "SpO2",
        "Glucose_mg_dL",
        "HbA1c",
        "Diagnosis"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Remove duplicate records
    df = df.drop_duplicates().copy()

    # Remove unnecessary spaces from text columns
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].str.strip()

    return df


def load_chatbot_samples():
    """Load labelled chatbot intent examples."""

    file_path = DATA_DIR / "aiml_labelled_samples.json"

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        samples = json.load(file)

    return samples


def load_healthcare_test_cases():
    """Load the supplied healthcare test cases."""

    file_path = DATA_DIR / "aiml_healthcare_test_cases.txt"

    if not file_path.exists():
        raise FileNotFoundError(f"Test cases not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def load_all_data():
    """Load and prepare all supplied project datasets."""

    symptoms = load_symptoms_data()
    symptoms = clean_symptoms_data(symptoms)

    chatbot_samples = load_chatbot_samples()
    test_cases = load_healthcare_test_cases()

    return {
        "symptoms": symptoms,
        "chatbot_samples": chatbot_samples,
        "test_cases": test_cases
    }


if __name__ == "__main__":
    data = load_all_data()

    print("CareBot datasets loaded successfully!")
    print("Symptoms records:", len(data["symptoms"]))
    print("Chatbot samples:", len(data["chatbot_samples"]))
    print("Healthcare test cases loaded.")
