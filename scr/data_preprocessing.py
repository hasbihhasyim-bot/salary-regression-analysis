import os
import pandas as pd
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

class DataPreprocessor:
    def __init__(self, raw_path=RAW_DATA_PATH, processed_path=PROCESSED_DATA_PATH):
        self.raw_path = raw_path
        self.processed_path = processed_path

    def load_data(self):
        """Memuat dataset mentah dengan pembatas semicolon (;)"""
        if not os.path.exists(self.raw_path):
            raise FileNotFoundError(
                f"Berkas data mentah tidak ditemukan di: {self.raw_path}. "
                "Pastikan Anda telah meletakkan berkas Salary_Data (1).csv di folder data/raw/."
            )
        return pd.read_csv(self.raw_path, sep=';')

    def clean_data(self, df):
        """Membersihkan nilai kosong, baris duplikat, dan menormalkan kategori pendidikan"""
        # 1. Menghapus baris dengan nilai kosong pada kolom kunci
        essential_cols =
        df = df.dropna(subset=essential_cols).copy()
        
        # 2. Menghapus baris duplikat (mengurangi bias replikasi sampel)
        df = df.drop_duplicates()

        # 3. Normalisasi string penamaan Education Level
        education_map = {
            "Bachelor's Degree": "Bachelor's",
            "Bachelor's": "Bachelor's",
            "Master's Degree": "Master's",
            "Master's": "Master's",
            "phD": "PhD",
            "PhD": "PhD",
            "High School": "High School"
        }
        df['Education Level'] = df['Education Level'].map(education_map)
        df = df.dropna(subset=['Education Level'])

        # 4. Memastikan tipe data numerik konsisten
        df['Age'] = df['Age'].astype(float)
        df = df.astype(float)
        df = df.astype(float)

        return df

    def save_processed_data(self, df):
        """Menyimpan data olahan ke direktori data/processed/"""
        os.makedirs(os.path.dirname(self.processed_path), exist_ok=True)
        df.to_csv(self.processed_path, index=False)
        print(f" Data bersih disimpan di: {self.processed_path}")

    def run_pipeline(self):
        """Menjalankan seluruh alur kerja prapemrosesan data"""
        df_raw = self.load_data()
        df_clean = self.clean_data(df_raw)
        self.save_processed_data(df_clean)
        return df_clean