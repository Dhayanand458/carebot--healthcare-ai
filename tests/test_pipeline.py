import json
import pandas as pd
import pytest

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def test_symptoms_dataset_exists():
    """Check whether the healthcare symptoms CSV exists."""
    file_path = DATA_DIR / "aiml_healthcare_symptoms.csv"

    assert file_path.exists(), "Symptoms dataset is missing"


def test_symptoms_dataset_can_be_loaded():
    """Check whether the symptoms CSV can be loaded."""
    file_path = DATA_DIR / "aiml_healthcare_symptoms.csv"

    df = pd.read_csv(file_path)

    assert not df.empty
    assert len(df) == 800


def test_symptoms_dataset_required_columns():
    """Check whether important healthcare columns are present."""
    file_path = DATA_DIR / "aiml_healthcare_symptoms.csv"

    df = pd.read_csv(file_path)

    required_columns = [
        "Age",
        "Gender",
        "Fever",
        "Cough",
        "BMI",
        "BP_Systolic",
        "BP_Diastolic",
        "SpO2",
        "Glucose_mg_dL",
        "HbA1c",
        "Diagnosis"
    ]

    for column in required_columns:
        assert column in df.columns, f"Missing column: {column}"


def test_symptoms_dataset_has_no_missing_values():
    """Check for missing values in the supplied symptoms dataset."""
    file_path = DATA_DIR / "aiml_healthcare_symptoms.csv"

    df = pd.read_csv(file_path)

    assert not df.isnull().any().any()


def test_chatbot_samples_exist():
    """Check whether the labelled chatbot JSON file exists."""
    file_path = DATA_DIR / "aiml_labelled_samples.json"

    assert file_path.exists(), "Chatbot samples file is missing"


def test_chatbot_samples_structure():
    """Check the structure of the labelled chatbot examples."""
    file_path = DATA_DIR / "aiml_labelled_samples.json"

    with open(file_path, "r", encoding="utf-8") as file:
        samples = json.load(file)

    assert isinstance(samples, list)
    assert len(samples) == 42

    for sample in samples:
        assert "text" in sample
        assert "intent" in sample
        assert "confidence" in sample


def test_chatbot_confidence_values():
    """Check that chatbot confidence values are between 0 and 1."""
    file_path = DATA_DIR / "aiml_labelled_samples.json"

    with open(file_path, "r", encoding="utf-8") as file:
        samples = json.load(file)

    for sample in samples:
        assert 0 <= sample["confidence"] <= 1


def test_healthcare_test_cases_exist():
    """Check whether the healthcare test cases file exists."""
    file_path = DATA_DIR / "aiml_healthcare_test_cases.txt"

    assert file_path.exists(), "Healthcare test cases file is missing"


def test_healthcare_test_cases_count():
    """Check whether the supplied test cases can be identified."""
    file_path = DATA_DIR / "aiml_healthcare_test_cases.txt"

    content = file_path.read_text(encoding="utf-8")

    test_cases = [
        line for line in content.splitlines()
        if line.strip().startswith("TEST_")
    ]

    assert len(test_cases) == 10