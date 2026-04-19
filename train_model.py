import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("insurance_data_linear.csv")

# -------------------------------
# Encoding (VERY IMPORTANT FIXED)
# -------------------------------
df['sex'] = df['sex'].map({'male': 0, 'female': 1})

df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})

df['region'] = df['region'].map({
    'southwest': 0,
    'southeast': 1,
    'northwest': 2,
    'northeast': 3
})

# -------------------------------
# Features & Target
# -------------------------------
X = df.drop("charges", axis=1)
y = df["charges"]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Model Training
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Save Model
# -------------------------------
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")