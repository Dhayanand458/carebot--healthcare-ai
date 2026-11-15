# CareBot Healthcare AI — Model Architecture and Evaluation Metrics

**Project:** CareBot Healthcare AI  
**Milestone:** Week 1 — Research and Architecture Design

## 1. Introduction

This document describes the proposed architecture and evaluation strategy for the CareBot Healthcare AI project.

The purpose of CareBot is to explore the use of Artificial Intelligence, Machine Learning and Natural Language Processing techniques in healthcare-related applications.

The proposed architecture is based on the datasets supplied for the project and the research reviewed during Week 1.

The initial design focuses on two areas:

1. Healthcare symptom-based classification.
2. Healthcare chatbot intent recognition.

Clinical-note information extraction and summarisation are also described in the project brief and will be considered as a separate component, subject to suitable input data and confirmation of the implementation scope.

---

## 2. Available Datasets

The project currently includes three supplied datasets.

### 2.1 Healthcare Symptoms Dataset

**File:** `aiml_healthcare_symptoms.csv`

- Contains 800 records and 17 columns.
- Includes patient attributes such as age and gender.
- Includes symptoms such as fever, cough, fatigue, breathlessness, chest pain, nausea and headache.
- Includes measurements such as BMI, blood pressure, SpO2, glucose and HbA1c.
- Contains a Diagnosis column that can be used as the target variable for supervised classification.

**Proposed use:** Explore and develop a symptom-based classification model.

### 2.2 Healthcare Test Cases

**File:** `aiml_healthcare_test_cases.txt`

Contains 10 supplied test cases covering:

- Healthcare triage.
- Diabetes screening.
- Hypertension classification.
- Anaemia detection.
- Healthy baseline.
- False-positive validation.
- Model evaluation.
- Explainability.
- Data-split validation.

**Proposed use:** Check expected system behaviour and validate selected project components.

### 2.3 Labelled Chatbot Samples

**File:** `aiml_labelled_samples.json`

Contains 42 text examples with corresponding intent labels and confidence values.

The available intent categories include:

- Fever.
- Malaria.
- Diabetes.
- Cold and flu.
- Hypertension.
- General queries.

**Proposed use:** Explore healthcare chatbot intent classification using labelled text examples.

---

## 3. Proposed System Architecture

The proposed architecture consists of separate processing components that can be developed and evaluated independently.

### 3.1 Overall Architecture

```text
             CAREBOT HEALTHCARE AI
                      |
               INPUT DATA
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Symptoms   Chatbot Text  Clinical Notes
        Dataset     Samples       (Future)
          |           |           |
          v           v           v
     Preprocessing  Text       Text
          |        Processing  Processing
          v           |           |
    Feature          v           v
    Preparation  Intent      Information
          |       Classification Extraction
          v           |           |
    Classification   v           v
       Model       Intent     Structured
          |        Result     Information
          v                       |
    Predicted                       v
    Class                    LLM Summarisation
          |                       |
          v                       v
    Evaluation               Summary Output
          |                       |
          +-----------+-----------+
                      |
               VALIDATION
                      |
              STRUCTURED OUTPUT
```

**Note:** The clinical-note branch is a proposed future component. It is not implemented using the currently supplied datasets.

### 3.2 Component 1 — Data Input

The system receives input from the supplied project datasets.

The initial inputs are:

- Structured healthcare records in CSV format.
- Healthcare chatbot examples in JSON format.
- Test cases in TXT format.

Clinical text input will be considered separately if the required data becomes available.

### 3.3 Component 2 — Data Preprocessing

The preprocessing component prepares input data for further processing.

Proposed activities include:

- Loading CSV and JSON files.
- Inspecting column names and data types.
- Checking missing and invalid values.
- Checking duplicate records.
- Handling categorical variables.
- Preparing numerical and categorical features.
- Preparing text samples for NLP processing.

The preprocessing stage will preserve the original data and document any transformations.

### 3.4 Component 3 — Symptom-Based Classification

The symptom classification component will use the healthcare symptoms dataset.

Proposed workflow:

1. Select relevant input features such as symptoms, age, BMI and health measurements.
2. Separate the input features from the Diagnosis target column.
3. Divide the available data into training, validation and testing sets.
4. Explore suitable supervised machine-learning algorithms.
5. Train and evaluate the selected model.
6. Generate a predicted class for test inputs.

The model will be evaluated using classification metrics rather than relying only on accuracy.

The output will represent an experimental model prediction, not a confirmed medical diagnosis.

### 3.5 Component 4 — Chatbot Intent Recognition

This component will process user text and identify its corresponding intent.

For example:

**Input:** "I have high temperature."

**Expected intent:** `fever`

Proposed workflow:

1. Receive user text.
2. Apply basic text preprocessing.
3. Convert the text into a suitable numerical representation.
4. Apply an intent classification approach.
5. Identify the predicted intent.
6. Return the predicted intent and relevant response category.

The supplied labelled JSON examples will be used for initial exploration.

Since the dataset contains a limited number of examples, further data and validation will be needed before considering a reliable chatbot model.

### 3.6 Component 5 — Clinical Information Extraction (Proposed)

The project brief also describes extracting important information from doctor notes or healthcare text.

The proposed extraction component may identify:

- Diagnosis.
- Medication.
- Follow-up instructions.
- Relevant clinical information.

The research reviewed in Week 1 suggests that Named Entity Recognition and clinical NLP tools can help identify relevant information from clinical text.

MedSpaCy is one possible technology to explore for clinical text processing.

This component requires suitable clinical-note input data before implementation.

### 3.7 Component 6 — Clinical Note Summarisation (Proposed)

After relevant information has been extracted, an LLM-based component may organise it into a readable summary.

Proposed workflow:

1. Receive extracted clinical information.
2. Organise information into predefined categories.
3. Generate a concise summary using an LLM.
4. Validate the generated output against the source information.
5. Present the summary for human review.

The design is informed by the Extract-Then-Abstract approach discussed in the reviewed research.

This component is proposed for future development and is not yet implemented.

### 3.8 Component 7 — Output and Validation

The system should produce structured and understandable outputs.

Depending on the component, outputs may include:

- Predicted classification labels.
- Predicted chatbot intents.
- Extracted healthcare information.
- Structured JSON responses.
- Generated summaries, when that component is implemented.

Outputs should be checked for completeness, correct formatting and consistency with the input data.

---

## 4. Proposed Evaluation Metrics

Different components require different evaluation methods.

### 4.1 Classification Metrics

The symptom-based classification model will be evaluated using the following metrics.

**Accuracy**

Measures the proportion of correctly predicted classifications among all predictions.

**Precision**

Measures how many predictions for a particular class were correct.

**Recall**

Measures how many actual examples of a particular class were correctly identified.

**F1-score**

Measures the balance between precision and recall.

**Confusion Matrix**

Shows the number of correct and incorrect predictions for each class.

These metrics will help identify cases where the model performs well or incorrectly classifies a healthcare category.

### 4.2 Chatbot Intent Recognition Metrics

The chatbot intent classification component will be evaluated using:

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion matrix.

Additional checks will include:

- Whether the predicted intent matches the expected intent.
- Whether the system handles unfamiliar or unclear inputs appropriately.
- Whether the output contains the expected intent structure.

### 4.3 Clinical Information Extraction Metrics

If the clinical information extraction component is developed, the proposed evaluation metrics are:

- Entity-level precision.
- Entity-level recall.
- Entity-level F1-score.
- Correct identification of diagnosis, medication and follow-up information.
- Completeness of extracted information.

These metrics require suitable annotated clinical-text evaluation data.

### 4.4 Clinical Summarisation Evaluation

If the summarisation component is implemented, it will require additional evaluation.

Proposed checks include:

- Factual consistency with the original input.
- Completeness of important clinical information.
- Correctness of extracted details.
- Readability and clarity.
- Human expert review.

The summary should not introduce information that is absent from the source notes.

### 4.5 Output Validation Metrics

Structured outputs will also be checked for:

- Valid JSON formatting.
- Presence of required fields.
- Correct data types.
- Consistency with the expected output structure.

### 4.6 Evaluation Summary

| Component | Proposed evaluation |
|---|---|
| Symptom classification | Accuracy, precision, recall, F1-score, confusion matrix |
| Chatbot intent recognition | Accuracy, precision, recall, F1-score, confusion matrix |
| Clinical information extraction | Entity precision, recall and F1-score |
| Clinical summarisation | Factual consistency, completeness, readability and human review |
| Structured output | JSON validity and required-field completeness |

Actual performance scores will be reported only after the corresponding components have been implemented and tested.

---

## 5. Data Splitting Strategy

The healthcare symptoms dataset will be divided into separate subsets for model development and evaluation.

A proposed initial split is:

- Training set: 70%.
- Validation set: 15%.
- Testing set: 15%.

For the supplied dataset of 800 records, this corresponds to:

| Dataset | Records |
|---|---:|
| Training | 560 |
| Validation | 120 |
| Testing | 120 |
| Total | 800 |

The split should be performed before model training, with appropriate attention to class distribution.

The testing set will be kept separate from training and model selection to provide an independent evaluation.

---

## 6. Proposed Technology Stack

The following tools and technologies may be used during development.

| Technology | Proposed purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading and manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine-learning models and evaluation |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| spaCy | Natural Language Processing |
| MedSpaCy | Clinical text processing |
| LLM | Proposed clinical summarisation component |
| Git and GitHub | Version control and project management |

The final technology selection will depend on implementation requirements and evaluation results.

---

## 7. Responsible AI and Healthcare Safety

Since CareBot is a healthcare-related project, responsible AI practices are important.

The following principles will guide development:

1. Use the supplied project datasets and avoid real patient-identifiable information.
2. Do not present experimental predictions as confirmed medical diagnoses.
3. Do not generate unsupported medical information.
4. Validate outputs against the available input data.
5. Clearly communicate uncertainty and limitations.
6. Keep human healthcare professionals responsible for clinical decisions.
7. Protect sensitive information and maintain appropriate data handling practices.

---

## 8. Current Scope and Limitations

The current supplied datasets support symptom-based classification and chatbot intent recognition.

However, the project brief also describes a clinical-note summarisation pipeline involving doctor transcripts and the extraction of diagnosis, medication and follow-up information.

The supplied CSV, TXT and labelled JSON files do not provide the clinical-note transcript dataset required to directly implement and evaluate that summarisation workflow.

Therefore:

- Symptom classification and chatbot intent recognition can be explored using the supplied data.
- Clinical information extraction and summarisation remain proposed components pending suitable input data and confirmation of scope.
- Model performance cannot be established until implementation and testing are completed.

---

## 9. Conclusion

This document establishes the initial architecture and evaluation strategy for CareBot Healthcare AI.

The proposed system uses modular components for data preprocessing, symptom classification, chatbot intent recognition, clinical information extraction and summarisation.

The architecture is informed by the research reviewed during Week 1, particularly the use of NER, LLM-based summarisation, structured information extraction and source-based verification.

The proposed evaluation metrics will help assess the performance and reliability of each component as development progresses.

**Project Status:** Week 1 — Proposed Architecture and Evaluation Design.