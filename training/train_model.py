import joblib
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load feature dataset
data = pd.read_csv("dataset/features.csv")

# Separate features and labels
X = data.drop("label", axis=1)
y = data["label"]

print("Dataset loaded!")
print("Features:", X.shape)
print("Labels:", y.shape)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

joblib.dump(model, "models/phishing_model.pkl")

print("Model saved successfully!")


print("\nModel training completed!")


# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    "importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\n5-Fold Cross-Validation:")
print("Scores:", scores)
print("Mean Accuracy:", round(scores.mean() * 100, 2), "%")