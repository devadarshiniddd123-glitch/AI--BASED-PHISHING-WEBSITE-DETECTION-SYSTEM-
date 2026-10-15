# AI-Based Phishing Website Detection System

## Project Overview

The AI-Based Phishing Website Detection System is a web-based application designed to identify potentially phishing websites using Artificial Intelligence and Machine Learning techniques.

The system accepts a website URL, validates the input, and uses a trained machine learning model to classify the URL as potentially phishing or likely legitimate. The application displays the detection result through a simple and user-friendly interface built using Streamlit.

## Project Objectives

- Detect potentially phishing website URLs.
- Analyze URL text using machine learning techniques.
- Classify URLs as potentially phishing or likely legitimate.
- Validate user input before processing.
- Display clear and understandable detection results.
- Provide an accessible web application for phishing awareness.

## Project Progress

**Review 2 Progress: Approximately 70%**

The project has progressed from initial planning to a working web application. The main interface has been implemented, the trained model has been integrated, and initial functional testing has been completed.

### Completed Work

- Defined the project problem and objectives.
- Designed the system workflow and architecture.
- Prepared the initial URL-based detection approach.
- Implemented the Streamlit web application.
- Integrated the machine learning model and URL vectorizer.
- Added website URL input functionality.
- Implemented URL input validation.
- Added phishing detection result display.
- Added model phishing score display when supported.
- Deployed the application using Streamlit Community Cloud.
- Performed initial functional tests for legitimate, empty, invalid, and suspicious-looking URLs.
- Updated project documentation on GitHub.

## System Workflow

1. User enters a website URL.
2. The application validates the URL.
3. The URL is transformed into machine learning features using the trained vectorizer.
4. The machine learning model predicts the URL class.
5. The application displays the prediction result.
6. If supported by the model, the phishing probability score is displayed.

**Workflow:**

User Input → URL Validation → Feature Vectorization → ML Model Prediction → Result Display

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Feature Extraction:** TF-IDF Vectorization
- **Classification Algorithm:** Random Forest Classifier
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib
- **Version Control:** GitHub
- **Deployment Platform:** Streamlit Community Cloud

## Application Features

- Simple and user-friendly interface.
- Website URL input field.
- URL format validation.
- Machine learning-based URL classification.
- Phishing and legitimate result messages.
- Model phishing score display when supported.
- Error handling for unsuccessful scans.
- Online application access through Streamlit Community Cloud.

## Functional Testing

| Test Case | Input | Observed Result |
|---|---|---|
| Legitimate URL | https://www.google.com | Expected legitimate result received |
| Empty URL | Empty input | Validation warning displayed |
| Invalid URL | abc | Invalid URL message displayed |
| Suspicious-looking URL | http://example.com/login/verify-account | Potentially Phishing Website displayed |

These tests verify basic application functionality. They do not independently establish the model's overall accuracy or its ability to detect all phishing websites.

## Current Limitations

- Predictions depend on the quality and coverage of the training dataset.
- URL text analysis alone cannot guarantee website safety.
- The displayed phishing score, when available, is a model estimate and not a guarantee.
- Comprehensive evaluation using a separate test dataset is still required.
- Further testing is needed with a wider range of phishing and legitimate URLs.

## Remaining Work

- Evaluate the model using a separate test dataset.
- Calculate accuracy, precision, recall, and F1-score.
- Review false-positive and false-negative predictions.
- Improve dataset quality and model performance where necessary.
- Perform additional functional and edge-case testing.
- Capture application screenshots and document results.
- Finalize the project report and presentation.

## Future Enhancements

- Expand the dataset with diverse phishing and legitimate URLs.
- Improve feature extraction and model evaluation.
- Add detailed scan reports.
- Improve the user interface and result explanations.
- Explore additional URL and domain-related security features.

## Project Status

**Current Progress: Approximately 70% — Review 2**

The application interface, model integration, URL validation, initial detection testing, and online deployment have been completed. Model evaluation, broader testing, performance improvement, and final documentation remain ongoing tasks.

**Disclaimer:** This application provides an initial machine learning-based URL assessment. A result classified as legitimate does not guarantee that a website is safe. Users should avoid entering sensitive information on websites they do not trust.
