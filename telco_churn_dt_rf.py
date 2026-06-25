import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv("Telco_customer_churn.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# Remove customerID
df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"].fillna(
    df["TotalCharges"].median(),
    inplace=True
)

# Remove duplicates
df.drop_duplicates(inplace=True)


# Encode Target Variable
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})


# One-Hot Encoding
df = pd.get_dummies(df, drop_first=True)

X = df.drop("Churn", axis=1)
y = df["Churn"]



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Decision Tree
dt = DecisionTreeClassifier(
    random_state=42
)

dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)


# Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# Evaluation
print("\nDecision Tree Results")
print("Train Accuracy:",
      dt.score(X_train, y_train))

print("Test Accuracy:",
      dt.score(X_test, y_test))

print("\nClassification Report")
print(classification_report(y_test, dt_pred))

print("Confusion Matrix")
print(confusion_matrix(y_test, dt_pred))


print("\nRandom Forest Results")
print("Train Accuracy:",
      rf.score(X_train, y_train))

print("Test Accuracy:",
      rf.score(X_test, y_test))

print("\nClassification Report")
print(classification_report(y_test, rf_pred))

print("Confusion Matrix")
print(confusion_matrix(y_test, rf_pred))

# Accuracy Comparison
dt_acc = accuracy_score(y_test, dt_pred)
rf_acc = accuracy_score(y_test, rf_pred)

print("\nAccuracy Comparison")
print(f"Decision Tree : {dt_acc:.4f}")
print(f"Random Forest : {rf_acc:.4f}")

# Visualize Decision Tree
plt.figure(figsize=(20, 10))

plot_tree(
    dt,
    feature_names=X.columns,
    class_names=["No Churn", "Churn"],
    filled=True,
    max_depth=3
)

plt.title("Decision Tree Visualization")
plt.show()

# Decision Tree Feature Importance
dt_importance = pd.Series(
    dt.feature_importances_,
    index=X.columns
)

dt_importance = dt_importance.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 5))
dt_importance.plot(kind="bar")
plt.title("Top 10 Decision Tree Features")
plt.ylabel("Importance")
plt.show()

# Random Forest Feature Importance
rf_importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
)

rf_importance = rf_importance.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 5))
rf_importance.plot(kind="bar")
plt.title("Top 10 Random Forest Features")
plt.ylabel("Importance")
plt.show()