from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)

    features = {
        "url_length": len(url),
        "has_ip": any(char.isdigit() for char in parsed.netloc),
        "has_at_symbol": "@" in url,
        "has_https": parsed.scheme == "https",
        "has_hyphen": "-" in parsed.netloc,
        "has_suspicious_words": any(
            word in url.lower()
            for word in ["login", "verify", "account", "secure", "update", "bank"]
        )
    }

    return features


def detect_phishing(url):
    features = extract_features(url)

    risk_score = 0

    if features["url_length"] > 75:
        risk_score += 1

    if features["has_ip"]:
        risk_score += 1

    if features["has_at_symbol"]:
        risk_score += 2

    if not features["has_https"]:
        risk_score += 1

    if features["has_hyphen"]:
        risk_score += 1

    if features["has_suspicious_words"]:
        risk_score += 1

    if risk_score >= 3:
        return "Potentially Phishing", risk_score

    return "Likely Legitimate", risk_score


print("AI-Based Phishing Website Detection System")
print("--------------------------------------------")

url = input("Enter website URL: ")

result, score = detect_phishing(url)

print("\nDetection Result:", result)
print("Risk Score:", score)
