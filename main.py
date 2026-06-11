"""
salary_analysis.py
------------------
Skrip ekonometrika komprehensif untuk analisis penentu gaji karyawan.
Dirancang untuk integrasi siap pakai pada repositori Git riset korporasi.
"""

import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error


class SalaryDataPipeline:
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw_data = None
        self.df = None
        self.X_ols = None
        self.y = None

    def load_and_clean_data(self):
        """
        Memuat dataset, menangani nilai kosong, menghapus duplikasi,
        dan menormalkan inkonsistensi string pada tingkat pendidikan.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Berkas data tidak ditemukan di: {self.filepath}")
        
        # Membaca data dengan pembatas titik koma (sesuai spesifikasi dataset riil)
        self.raw_data = pd.read_csv(self.filepath, sep=';')
        self.df = self.raw_data.copy()

        # 1. Menghapus nilai kosong (null values)
        self.df.dropna(subset=, inplace=True)
        
        # 2. Menghapus baris duplikat
        self.df.drop_duplicates(inplace=True)

        # 3. Menyamakan format string kategori pendidikan
        education_map = {
            "Bachelor's Degree": "Bachelor's",
            "Bachelor's": "Bachelor's",
            "Master's Degree": "Master's",
            "Master's": "Master's",
            "phD": "PhD",
            "PhD": "PhD",
            "High School": "High School"
        }
        self.df['Education Level'] = self.df['Education Level'].map(education_map)
        
        # Sisa nilai yang tidak terpetakan akan dihapus
        self.df.dropna(subset=['Education Level'], inplace=True)
        
        # Konversi tipe data numerik ke float
        self.df['Age'] = self.df['Age'].astype(float)
        self.df = self.df.astype(float)
        self.df = self.df.astype(float)

        print(f"Pembersihan Selesai. Sisa baris observasi: {len(self.df)}")
        return self.df

    def calculate_inequality_metrics(self):
        """
        Menghitung Shannon Entropy (untuk mereproduksi angka 8.11 & 7.88)
        serta menghitung Indeks Theil T yang sesungguhnya secara matematis.
        """
        results = {}
        for gender in ['Male', 'Female']:
            group_salaries = self.df[self.df['Gender'] == gender].values
            group_salaries = group_salaries[group_salaries > 0]
            
            if len(group_salaries) == 0:
                continue
            
            # A. Replikasi: Shannon Entropy (pustaka scipy mengasumsikan sum(p)=1)
            shannon_entropy = stats.entropy(group_salaries)
            
            # B. Indeks Theil T Matematis yang Sesungguhnya (GE(1))
            n = len(group_salaries)
            mean_salary = np.mean(group_salaries)
            shares = group_salaries / mean_salary
            # Menghindari log(0) dengan memotong nilai di bawah batas minimum aman
            shares = np.where(shares <= 0, 1e-10, shares)
            theil_t = np.mean(shares * np.log(shares))
            
            results[gender] = {
                "Sample_Size": n,
                "Mean_Salary": mean_salary,
                "Shannon_Entropy_Raw_Salary": shannon_entropy,
                "True_Theil_T_Index": theil_t
            }
        
        return pd.DataFrame(results).T

    def prepare_regression_variables(self):
        """
        Mengonstruksi variabel dummy dan menyiapkan matriks desain regresi.
        Reference Baseline: Education Level = High School, Gender = Male.
        """
        # Pembuatan Variabel Dummy secara eksplisit
        edu_dummies = pd.get_dummies(self.df['Education Level'], prefix='Edu', drop_first=False)
        gender_dummies = pd.get_dummies(self.df['Gender'], prefix='Gender', drop_first=False)
        
        # Menggabungkan dummy ke dataframe utama
        reg_df = pd.concat([self.df, edu_dummies, gender_dummies], axis=1)

        # Menentukan matriks variabel independen (X) dengan membuang baseline reference
        # Baseline reference: Edu_High School dan Gender_Male dibuang
        features =
        
        self.X_ols = reg_df[features].astype(float)
        self.y = reg_df.astype(float)
        
        # Menambahkan konstanta intersep untuk estimasi model OLS statsmodels
        self.X_ols = sm.add_constant(self.X_ols)
        return self.X_ols, self.y

    def calculate_vif(self):
        """
        Menghitung nilai Variance Inflation Factor (VIF) untuk mendeteksi multikolinearitas.
        """
        # Menghitung VIF untuk seluruh prediktor (tanpa konstanta intersep)
        predictors = self.X_ols.drop(columns=['const'])
        vif_df = pd.DataFrame()
        vif_df["Variable"] = predictors.columns
        vif_df["VIF"] = [
            variance_inflation_factor(predictors.values, i)
            for i in range(predictors.shape)
        ]
        return vif_df

    def run_ols_regression(self):
        """
        Mengeksekusi regresi OLS menggunakan pustaka statsmodels untuk summary statistik lengkap.
        """
        model = sm.OLS(self.y, self.X_ols)
        results = model.fit()
        return results

    def run_ridge_regression(self, alpha=1.0):
        """
        Mengeksekusi Ridge Regression (L2 Regularization) untuk mengatasi kolinearitas Age-Experience.
        """
        # Memisahkan data latih dan uji (80:20)
        X_train, X_test, y_train, y_test = train_test_split(
            self.X_ols.drop(columns=['const']), self.y, test_size=0.2, random_state=42
        )
        
        # Regularisasi mensyaratkan standarisasi skala fitur
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        ridge = Ridge(alpha=alpha)
        ridge.fit(X_train_scaled, y_train)
        
        y_pred = ridge.predict(X_test_scaled)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        coef_dict = dict(zip(X_train.columns, ridge.coef_))
        return r2, rmse, coef_dict


if __name__ == "__main__":
    # Menentukan lokasi penyimpanan berkas data riil
    data_path = "data/raw/Salary_Data (1).csv"
    
    # Membuat direktori data mentah jika belum tersedia secara lokal
    if not os.path.exists("data/raw/"):
        os.makedirs("data/raw/")
        
    print("=== Memulai Pipeline Ekonometrika ===")
    pipeline = SalaryDataPipeline(data_path)
    
    try:
        df_clean = pipeline.load_and_clean_data()
        
        print("\n=== Perhitungan Indeks Ketimpangan ===")
        ineq_df = pipeline.calculate_inequality_metrics()
        print(ineq_df.to_string())
        
        X, y = pipeline.prepare_regression_variables()
        
        print("\n=== Deteksi Multikolinearitas (VIF) ===")
        vif_df = pipeline.calculate_vif()
        print(vif_df.to_string(index=False))
        
        print("\n=== Estimasi Regresi OLS ===")
        ols_results = pipeline.run_ols_regression()
        print(ols_results.summary())
        
        print("\n=== Estimasi Regresi Ridge (Mengatasi Kolinearitas) ===")
        r2, rmse, ridge_coefs = pipeline.run_ridge_regression(alpha=10.0)
        print(f"R-squared (Ridge): {r2:.4f}")
        print(f"RMSE (Ridge): {rmse:.2f}")
        print("Koefisien Ridge Terstandarisasi:")
        for var, coef in ridge_coefs.items():
            print(f"  {var:25s}: {coef:.2f}")
            
    except Exception as e:
        print(f"Terjadi kesalahan eksekusi pipeline: {str(e)}")