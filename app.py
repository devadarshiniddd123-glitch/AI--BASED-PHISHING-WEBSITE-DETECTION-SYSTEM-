
import streamlit as st
import joblib
from urllib.parse import urlparse

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    model = joblib.load("phishing_model.pkl")
    vectorizer = joblib.load("url_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

st.title("🛡️ AI-Based Phishing Website Detection")
st.write(
    "Check a website URL using our machine learning model."
)

st.info(
    "Enter a URL to check whether the model identifies "
    "it as potentially phishing or likely legitimate."
)

with st.form("url_checker"):
    url = st.text_input(
        "Website URL",
        placeholder="https://example.com"
    )
    submitted = st.form_submit_button(
        "🔍 Scan Website",
        use_container_width=True
    )

if submitted:
    cleaned_url = url.strip()

    if not cleaned_url:
        st.warning("Please enter a website URL.")

    else:
        if "://" not in cleaned_url:
            cleaned_url = "https://" + cleaned_url

        parsed = urlparse(cleaned_url)

        valid_url = (
            parsed.scheme in ("http", "https")
            and bool(parsed.hostname)
            and "." in parsed.hostname
            and " " not in cleaned_url
        )

        if not valid_url:
            st.error("Enter a valid HTTP or HTTPS URL.")

        else:
            try:
                features = vectorizer.transform([cleaned_url])
                prediction = model.predict(features)[0]

                st.subheader("Scan Result")

                if str(prediction).lower() == "phishing":
                    st.error("⚠️ Potentially Phishing Website")
                    st.write(
                        "Avoid entering passwords or banking details."
                    )
                else:
                    st.success("✅ Likely Legitimate Website")
                    st.write(
                        "The current model did not classify "
                        "this URL as phishing."
                    )

                if hasattr(model, "predict_proba"):
                    probabilities = model.predict_proba(features)[0]
                    classes = list(model.classes_)

                    if "phishing" in classes:
                        index = classes.index("phishing")
                        score = float(probabilities[index])

                        st.metric(
                            "Model phishing score",
                            f"{score * 100:.1f}%"
                        )
                        st.caption(
                            "This is the model's estimated class "
                            "probability, not a guarantee of safety."
                        )

                st.caption(
                    "This tool checks URL text only. It does not "
                    "guarantee that a website is safe."
                )

            except Exception as error:
                st.error(
                    "Unable to scan this URL. Check the model files "
                    "and try again."
                )
                st.caption(f"Technical details: {error}")
