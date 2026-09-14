import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("url_vectorizer.pkl")

# Page title
st.title("🛡️ AI-Based Phishing Website Detection System")

st.write("Enter a website URL to check whether it is legitimate or potentially phishing.")

# URL input
url = st.text_input("Enter Website URL:")

# Check button
if st.button("Check Website"):
    if url:
        features = vectorizer.transform([url])
        prediction = model.predict(features)[0]

        if prediction == "phishing":
            st.error("⚠️ Potentially Phishing Website")
            st.write("This website may be unsafe. Please avoid entering personal or banking information.")
        else:
            st.success("✅ Likely Legitimate Website")
            st.write("No phishing indication was detected by the current model.")
    else:
        st.warning("Please enter a website URL.")