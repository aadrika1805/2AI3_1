# Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("insurance_data_linear.csv")

# Show basic info
print(df.head())
print(df.info())

# -------------------------------
# 1. Handle Missing Values
# -------------------------------
print(df.isnull().sum())

# Fill missing values (if any)
df = df.dropna()   # or use fillna()

# -------------------------------
# 2. Encode Categorical Data
# -------------------------------
le = LabelEncoder()

# Convert categorical columns
categorical_cols = ['sex', 'smoker', 'region']

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# -------------------------------
# 3. Feature & Target Split
# -------------------------------
X = df.drop("charges", axis=1)   # features
y = df["charges"]                # target

# -------------------------------
# 4. Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 5. Feature Scaling
# -------------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------
# Done ✅
# -------------------------------
print("Preprocessing completed!")