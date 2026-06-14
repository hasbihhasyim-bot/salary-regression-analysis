# employee-salary-regression
# 📈 Analisis Regresi Multivariat Terhadap Faktor Penentu Gaji Karyawan

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
