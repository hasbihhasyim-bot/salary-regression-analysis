import os
from pathlib import Path

# Mendefinisikan direktori utama proyek
BASE_DIR = Path(__file__).resolve().parent.parent

# Jalur direktori data
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Jalur berkas data spesifik
RAW_DATA_PATH = os.path.join(RAW_DATA_DIR, "Salary_Data (1).csv")
PROCESSED_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, "Salary_Data_Cleaned.csv")

# Parameter Statistik & Pemodelan
RANDOM_STATE = 42
TEST_SIZE = 0.2
RIDGE_ALPHA = 10.0