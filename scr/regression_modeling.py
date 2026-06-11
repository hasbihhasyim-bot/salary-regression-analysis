import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from src.config import RANDOM_STATE, TEST_SIZE

def prepare_features(df):
    """
    Menyiapkan variabel independen (X) dan dependen (y).
    Baseline Reference: Education Level = High School, Gender = Male.
    """
    # Mengesampingkan kategori gender 'Other' (n=14) demi menjaga stabilitas inferensi statistik
    df_filtered = df[df['Gender']!= 'Other'].copy()

    # One-hot encoding eksplisit
    edu_dummies = pd.get_dummies(df_filtered['Education Level'], prefix='Edu', drop_first=False)
    gender_dummies = pd.get_dummies(df_filtered['Gender'], prefix='Gender', drop_first=False)

    reg_df = pd.concat([df_filtered, edu_dummies, gender_dummies], axis=1)

    # Memilih fitur prediktor (High School dan Male dikeluarkan sebagai baseline reference)
    features =

    X = reg_df[features].astype(float)
    y = reg_df.astype(float)

    return X, y

def calculate_vif(X):
    """Menghitung Variance Inflation Factor (VIF) untuk setiap prediktor"""
    vif_df = pd.DataFrame()
    vif_df["Variable"] = X.columns
    vif_df["VIF"] = [
        variance_inflation_factor(X.values, i)
        for i in range(X.shape[1])
    ]
    return vif_df

class RegressionModel:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def fit_ols(self):
        """Melakukan fitting model Ordinary Least Squares (OLS)"""
        X_const = sm.add_constant(self.X)
        model = sm.OLS(self.y, X_const)
        results = model.fit()
        return results

    def fit_ridge(self, alpha=10.0):
        """Melakukan fitting model Regresi Ridge (Regularisasi L2)"""
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=TEST_SIZE, random_state=RANDOM_STATE
        )

        # Skala fitur wajib distandarisasi untuk regularisasi Ridge
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        ridge = Ridge(alpha=alpha)
        ridge.fit(X_train_scaled, y_train)

        y_pred = ridge.predict(X_test_scaled)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        coefs = dict(zip(self.X.columns, ridge.coef_))
        return r2, rmse, coefs