
# employee-salary-econometric-analysis

# 📊 Analisis Regresi Multivariat Terhadap Faktor Penentu Gaji Karyawan

Proyek ini mengimplementasikan analisis ekonometrika menggunakan **Multiple Linear Regression (OLS)** dan **Ridge Regression** untuk mengidentifikasi faktor-faktor yang memengaruhi tingkat kompensasi karyawan. Analisis dilakukan pada dataset **Salary Data** dari Kaggle yang berisi 6.704 observasi individu dengan karakteristik demografis dan profesional yang beragam.

Selain pemodelan regresi, proyek ini juga mencakup:

- Data Cleaning & Feature Engineering
- Analisis Statistik Deskriptif
- Pengukuran Gender Wage Gap
- Pengukuran Ketimpangan Pendapatan (Shannon Entropy & Theil Index)
- Diagnostik Multikolinearitas (VIF)
- Regularisasi Ridge Regression

---

## 🎯 Tujuan Proyek

1. **Mengidentifikasi Faktor Penentu Gaji**
   - Mengukur pengaruh usia, pengalaman kerja, pendidikan, dan gender terhadap tingkat gaji.

2. **Membangun Model Prediksi**
   - Mengembangkan model regresi yang mampu memprediksi gaji tahunan karyawan berdasarkan profil individu.

3. **Mengukur Kesenjangan Upah**
   - Menganalisis perbedaan kompensasi berdasarkan gender dan tingkat pendidikan.

4. **Menganalisis Ketimpangan Pendapatan**
   - Menggunakan Shannon Entropy dan Theil Index untuk mengevaluasi distribusi gaji.

5. **Mengatasi Multikolinearitas**
   - Mengimplementasikan Ridge Regression untuk meningkatkan stabilitas model.

---

## 📂 Dataset

Dataset yang digunakan adalah **Salary Data** yang tersedia secara publik di Kaggle.

### Karakteristik Dataset

| Variabel | Tipe Data | Deskripsi |
|-----------|------------|------------|
| Age | Numerik | Usia karyawan |
| Gender | Kategorikal | Gender karyawan |
| Education Level | Kategorikal | Tingkat pendidikan terakhir |
| Job Title | Kategorikal | Jabatan pekerjaan |
| Years of Experience | Numerik | Lama pengalaman kerja |
| Salary | Numerik | Gaji tahunan |

Jumlah observasi awal:

- 6.704 baris data

Setelah data cleaning:

- Null value dihapus
- Duplikasi data dihapus
- Standarisasi kategori pendidikan dilakukan

---

## 🧹 Data Cleaning & Feature Engineering

### Normalisasi Tingkat Pendidikan

Beberapa kategori pendidikan yang tidak konsisten disatukan:

| Sebelum | Sesudah |
|----------|----------|
| Bachelor's Degree | Bachelor's |
| Master's Degree | Master's |
| phD | PhD |

### Variabel Dummy

Kategori referensi:

- Education Level → High School
- Gender → Male

Dummy yang dibentuk:

```text
Bachelor's
Master's
PhD

Female
Other
````

---

## 📈 Analisis Statistik Deskriptif

### Distribusi Gender

| Gender | Jumlah |
| ------ | ------ |
| Male   | 3.671  |
| Female | 3.013  |
| Other  | 14     |

### Rata-rata Gaji Tahunan

| Gender | Rata-rata Gaji |
| ------ | -------------- |
| Female | USD 107.889    |
| Male   | USD 121.396    |
| Other  | USD 125.870    |

---

## 🎓 Pengaruh Pendidikan Terhadap Gaji

| Pendidikan  | Female      | Male        |
| ----------- | ----------- | ----------- |
| High School | USD 30.368  | USD 39.381  |
| Bachelor's  | USD 89.165  | USD 98.972  |
| Master's    | USD 122.695 | USD 140.061 |
| PhD         | USD 160.266 | USD 168.711 |

Temuan utama:

* Semakin tinggi pendidikan, semakin tinggi rata-rata gaji.
* Gender wage gap muncul pada seluruh tingkat pendidikan.
* Kesenjangan terbesar terjadi pada tingkat Master's Degree.

---

## 📉 Analisis Ketimpangan Pendapatan

### Shannon Entropy

Digunakan untuk mereplikasi hasil laporan awal.

Formula:

```math
H = -\sum p_i \log(p_i)
```

Keterangan:

* pᵢ = proporsi kontribusi gaji individu terhadap total gaji kelompok.

### True Theil Index

Digunakan sebagai ukuran ketimpangan yang lebih valid.

Formula:

```math
T = \frac{1}{N}\sum \frac{y_i}{\mu}
\ln\left(\frac{y_i}{\mu}\right)
```

Keterangan:

* yᵢ = gaji individu
* μ = rata-rata gaji kelompok
* N = jumlah observasi

---

## 🔬 Model Regresi Linear Berganda

Persamaan model:

```math
Salary_i =
β_0 +
β_1 Age_i +
β_2 Experience_i +
β_3 Bachelor's_i +
β_4 Master's_i +
β_5 PhD_i +
β_6 Female_i +
β_7 Other_i +
ε_i
```

Dimana:

* Salary = Gaji tahunan
* Age = Usia
* Experience = Lama pengalaman kerja
* Bachelor's, Master's, PhD = Dummy pendidikan
* Female, Other = Dummy gender
* ε = Error term

---

## ⚠️ Diagnostik Multikolinearitas

Karena variabel:

```text
Age
Years of Experience
```

sangat berkorelasi, maka dilakukan pengujian menggunakan:

### Variance Inflation Factor (VIF)

Formula:

```math
VIF_j = \frac{1}{1-R_j^2}
```

Interpretasi:

| Nilai VIF | Keterangan               |
| --------- | ------------------------ |
| < 5       | Aman                     |
| 5 – 10    | Perlu perhatian          |
| > 10      | Multikolinearitas tinggi |

---

## 🛠 Ridge Regression

Untuk mengurangi dampak multikolinearitas digunakan Ridge Regression.

Objective Function:

```math
RSS + \lambda \sum \beta_j^2
```

Keuntungan:

* Menstabilkan koefisien regresi
* Mengurangi varians model
* Mempertahankan seluruh variabel penting
* Mengatasi korelasi tinggi antar fitur

---

## 📦 Library Python yang Digunakan

```python
pandas
numpy
matplotlib
seaborn

scikit-learn
statsmodels

scipy
```

Instalasi:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels scipy
```

---

## 🚀 Hasil Utama

* Pendidikan formal merupakan faktor paling kuat dalam peningkatan gaji.
* Pengalaman kerja berpengaruh positif terhadap kompensasi.
* Terdapat gender wage gap pada seluruh tingkat pendidikan.
* Variabel Age dan Experience menunjukkan indikasi multikolinearitas tinggi.
* Ridge Regression meningkatkan stabilitas model.
* Ketimpangan distribusi pendapatan lebih akurat diukur menggunakan Theil Index dibanding Shannon Entropy.

---

## 📚 Referensi

* Kaggle Salary Data Dataset
* Scikit-Learn Documentation
* Statsmodels Documentation
* Human Capital Theory
* Ridge Regression Literature
* Generalized Entropy & Theil Index Theory

```

Format ini sudah siap digunakan sebagai **README.md GitHub** untuk proyek analisis regresi gaji karyawan dan mengikuti gaya yang sama seperti contoh yang Anda berikan.
```
