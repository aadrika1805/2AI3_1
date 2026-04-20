import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Import your friend's preprocessing file
import preprocessing as pp

# Use their variables directly
X_test = pp.X_test
y_test = pp.y_test

# Load trained model
with open("model.pkl", "rb") as f:
        model = pickle.load(f)


# 1. Add these lines BEFORE your prediction
        print("EXPECTED by model:", model.n_features_in_) 
# Note: Use model.feature_names_in_ if it was trained on a DataFrame

# 2. Check what your current X_test looks like
        print("ACTUALLY providing:", X_test.shape[1], "features")


        # Predict
        y_pred = model.predict(X_test)

        # Evaluation
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        print("MAE:", mae)
        print("MSE:", mse)
        print("RMSE:", rmse)
        print("R2 Score:", r2)

        # Plot
        plt.scatter(y_test, y_pred)
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("Actual vs Predicted")
        plt.show()