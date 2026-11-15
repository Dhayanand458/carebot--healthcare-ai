
import re


# Healthcare terms for initial keyword-based extraction
HEALTHCARE_TERMS = {
    "symptoms": [
        "fever",
        "cough",
        "fatigue",
        "breathlessness",
        "chest pain",
        "nausea",
        "headache",
        "chills",
        "shivering",
        "runny nose",
        "sore throat",
        "high temperature"
    ],

    "conditions": [
        "malaria",
        "diabetes",
        "hypertension",
        "influenza",
        "pneumonia",
        "anaemia",
        "anemia"
    ],

    "medical_information": [
        "blood pressure",
        "blood sugar",
        "glucose",
        "hba1c",
        "spo2",
        "bmi",
        "medication",
        "medicine",
        "prescription",
        "follow-up"
    ]
}


def extract_entities(text):
    """
    Identify healthcare-related keywords in input text.

    This is a basic keyword matching approach.
    It does not perform clinical diagnosis.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    text = text.lower()

    extracted = {
        "symptoms": [],
        "conditions": [],
        "medical_information": []
    }

    for category, terms in HEALTHCARE_TERMS.items():
        for term in terms:

            pattern = r"\b" + re.escape(term) + r"\b"

            if re.search(pattern, text):
                extracted[category].append(term)

    return extracted


if __name__ == "__main__":

    example = "Patient has fever, cough and high blood pressure."

    result = extract_entities(example)

    print("Input:", example)
    print("Extracted information:", result)
