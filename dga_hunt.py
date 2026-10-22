import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


Discord_Webhook_URL = "Your_Discord_Webhook_URL_Here"

def send_discord_alert(domain_name):
    payload = {
        "content": f"SOC ALert :  Threat Detected: {domain_name}"
    }
    requests.post(Discord_Webhook_URL, json=payload)

domains = [
    
    "google.com", "amazon.com", "wikipedia.org", "netflix.com", "github.com", "linkedin.com",
    
    
    "xkqj1239z.com", "zxcvbnm123.net", "qweasdzxc.org", "pqncv88.info", "lkjhg99.biz", "mnbvc12.ru"
]

labels = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2,3))
X_math = vectorizer.fit_transform(domains)

ai_model = MultinomialNB()
ai_model.fit(X_math, labels)

new_traffic = ["instagram.com", "v88qnc.info"]
new_math = vectorizer.transform(new_traffic)
predictions = ai_model.predict(new_math)

print("--- SOC AI Threat Analysis---")
for domain, result in zip(new_traffic, predictions):
    if result == 1:
        print(f"Malware threat detected: {domain}")
        send_discord_alert(domain)
    else:
        print(f"safe human domain: {domain}")