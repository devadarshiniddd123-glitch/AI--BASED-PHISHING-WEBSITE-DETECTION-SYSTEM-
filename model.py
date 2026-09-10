import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("phishing_dataset.csv")

# Input and output
X = data["url"]
y = data["label"]

# Convert URLs into numerical features
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 5))
X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.25, random_state=42
)

# Train ML model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Phishing Detection ML Model")
print("----------------------------")
print("Model trained successfully")
print("Accuracy:", accuracy)
