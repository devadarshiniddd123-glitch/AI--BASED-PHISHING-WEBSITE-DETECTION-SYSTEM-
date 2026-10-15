
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 1. Load dataset
data = pd.read_csv("phishing_dataset.csv")

# 2. Remove missing values
data = data.dropna(subset=["url", "label"])

# 3. Prepare input and output
X = data["url"].astype(str)
y = data["label"]

# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 5. Convert URL text into numerical features
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 5)
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# 6. Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_vectorized, y_train)

# 7. Predict test data
predictions = model.predict(X_test_vectorized)

# 8. Calculate evaluation metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(
    y_test, predictions, average="weighted", zero_division=0
)
recall = recall_score(
    y_test, predictions, average="weighted", zero_division=0
)
f1 = f1_score(
    y_test, predictions, average="weighted", zero_division=0
)

# 9. Display results
print("AI-Based Phishing Website Detection")
print("-----------------------------------")
print("Model trained successfully")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test, predictions, zero_division=0
))

# 10. Save trained model and vectorizer
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "url_vectorizer.pkl")

print("\nModel and vectorizer saved successfully.")

