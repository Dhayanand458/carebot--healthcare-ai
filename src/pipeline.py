
from src.preprocess import load_all_data
from src.extract_entities import extract_entities


def run_pipeline():
    """Run the initial CareBot data pipeline."""

    print("=" * 50)
    print("       CAREBOT HEALTHCARE AI PIPELINE")
    print("=" * 50)

    # Step 1: Load and prepare datasets
    print("\nStep 1: Loading project datasets...")

    data = load_all_data()

    symptoms = data["symptoms"]
    chatbot_samples = data["chatbot_samples"]
    test_cases = data["test_cases"]

    print("Symptoms records:", len(symptoms))
    print("Symptoms columns:", len(symptoms.columns))
    print("Chatbot examples:", len(chatbot_samples))

    # Step 2: Display dataset information
    print("\nStep 2: Dataset information...")

    print("\nDiagnosis categories:")
    print(symptoms["Diagnosis"].value_counts())

    # Step 3: Extract information from sample text
    print("\nStep 3: Healthcare information extraction...")

    example_text = "Patient has fever, cough and headache."

    extracted = extract_entities(example_text)

    print("Input text:", example_text)
    print("Extracted information:", extracted)

    # Step 4: Display test case information
    test_case_count = sum(
        1 for line in test_cases.splitlines()
        if line.strip().startswith("TEST_")
    )

    print("\nStep 4: Test case information...")
    print("Available healthcare test cases:", test_case_count)

    print("\nCareBot initial pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
