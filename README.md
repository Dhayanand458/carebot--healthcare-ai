# CareBot Healthcare AI

## Project Overview

CareBot Healthcare AI is an AI/ML project focused on exploring healthcare-related data processing, machine learning, Natural Language Processing (NLP), and clinical information summarisation.

The project aims to develop a structured healthcare AI system using the datasets and requirements provided for the internship.

## Project Objectives

- Explore and preprocess healthcare datasets.
- Develop symptom-based classification approaches.
- Explore chatbot intent recognition.
- Investigate clinical information extraction.
- Explore LLM-based clinical note summarisation.
- Evaluate system performance using suitable metrics and test cases.
- Follow responsible AI practices for healthcare applications.

## Dataset Description

The project uses three supplied datasets:

1. `aiml_healthcare_symptoms.csv` — Healthcare records containing symptoms and patient measurements.
2. `aiml_healthcare_test_cases.txt` — Ten predefined healthcare test cases.
3. `aiml_labelled_samples.json` — Labelled healthcare chatbot text examples.

Detailed dataset information is available in `data/README.md`.

## Proposed System Architecture

The initial architecture consists of:

1. Data input and loading.
2. Data preprocessing.
3. Symptom-based classification.
4. Chatbot intent recognition.
5. Clinical information extraction.
6. Proposed clinical note summarisation.
7. Output validation and evaluation.

The clinical information extraction and summarisation components are proposed based on the project brief and require suitable clinical-note data for implementation.

## Evaluation Metrics

The proposed evaluation metrics include:

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion matrix.
- Entity extraction evaluation.
- JSON output validation.
- Summary factual consistency and human review.

Detailed architecture and evaluation information is available in `docs/architecture.md`.

## Repository Structure

```text
carebot-healthcare-ai/
│
├── README.md
│
├── data/
│   ├── aiml_healthcare_symptoms.csv
│   ├── aiml_healthcare_test_cases.txt
│   ├── aiml_labelled_samples.json
│   └── README.md
│
├── docs/
│   ├── research_review.md
│   └── architecture.md
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── extract_entities.py
│   └── pipeline.py
│
└── tests/
    └── test_pipeline.py
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- spaCy
- MedSpaCy
- Matplotlib
- Seaborn
- Git and GitHub

## Responsible AI

- Use the supplied project datasets.
- Avoid real patient-identifiable information.
- Do not treat experimental predictions as medical diagnoses.
- Validate generated information against available input data.
- Keep human healthcare professionals responsible for clinical decisions.


**Project:** CareBot Healthcare AI  
**Internship:** AI/ML Internship — Cynaris Solutions