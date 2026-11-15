# CareBot Healthcare AI — Dataset Documentation

## Overview

This folder contains the datasets provided for the CareBot Healthcare AI project.

These datasets are used for initial data exploration, preprocessing, chatbot intent recognition, and healthcare-related model development.

## 1. Healthcare Symptoms Dataset

**File:** `aiml_healthcare_symptoms.csv`

**Description:**

This dataset contains 800 healthcare records with 17 columns.

It includes:
- Patient information such as age and gender.
- Symptoms such as fever, cough, fatigue and headache.
- Health measurements such as BMI, blood pressure, SpO2, glucose and HbA1c.
- Diagnosis labels.

**Purpose:** To explore healthcare data and develop symptom-based classification models.

## 2. Healthcare Test Cases

**File:** `aiml_healthcare_test_cases.txt`

**Description:**

This file contains 10 predefined healthcare test cases.

The test cases cover:
- Healthcare triage.
- Diabetes screening.
- Hypertension classification.
- Anaemia detection.
- Healthy baseline.
- Model validation.
- Model evaluation.
- Explainability.
- Data-split validation.

**Purpose:** To check expected system behaviour and evaluate different project components.

## 3. Labelled Chatbot Samples

**File:** `aiml_labelled_samples.json`

**Description:**

This JSON dataset contains 42 labelled text examples.

Each example includes:
- Text: User input.
- Intent: Corresponding healthcare-related category.
- Confidence: Supplied confidence value.

Available intent categories include:
- Fever.
- Malaria.
- Diabetes.
- Cold and flu.
- Hypertension.
- General queries.

**Purpose:** To explore healthcare chatbot intent recognition and text classification.

## Data Usage and Safety

- Use these datasets for project development and testing.
- Preserve the original supplied data.
- Do not introduce real patient-identifiable information.
- Treat model predictions as experimental outputs, not confirmed medical diagnoses.

## Dataset Summary

| Dataset | Format | Records / Cases |
|---|---|---:|
| Healthcare symptoms | CSV | 800 |
| Healthcare test cases | TXT | 10 |
| Labelled chatbot samples | JSON | 42 |

**Project:** CareBot Healthcare AI  
**Milestone:** Week 1 — Research and Architecture Design