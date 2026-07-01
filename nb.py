import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("spam.csv", encoding="latin-1")

df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report")
print(classification_report(y_test, predictions))


print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))


new_sms = [
    "Congratulations! You have won a FREE lottery prize. Call now!"
]

new_sms_tfidf = vectorizer.transform(new_sms)

prediction = model.predict(new_sms_tfidf)

print("\nNew SMS:")
print(new_sms[0])

if prediction[0] == 1:
    print("Prediction: Spam")
else:
    print("Prediction: Ham (Not Spam)")