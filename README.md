# employee-salary-regression
# 📈 Analisis Regresi Multivariat Terhadap Faktor Penentu Gaji Karyawan

Analisis ini menggunakan metode statistik **Regresi Linear Berganda (Multiple Linear Regression)** untuk mengidentifikasi, memodelkan, dan memprediksi pengaruh karakteristik individu—seperti usia, masa kerja, tingkat pendidikan formal, dan gender—terhadap tingkat gaji tahunan karyawan.

Proyek ini dibangun menggunakan pustaka `scikit-learn` untuk pemodelan prediktif dan `statsmodels` untuk evaluasi statistik inferensial yang mendalam.

---

## 🎯 Tujuan Proyek
1. **Prediksi Akurat:** Membangun model regresi linear berganda untuk memprediksi kompensasi tahunan karyawan berdasarkan profil profesional mereka.
2. **Evaluasi Inferensial:** Menguji signifikansi statistik dari masing-masing variabel independen guna memahami faktor penentu upah yang paling dominan di pasar kerja.
3. **Analisis Disparitas & Bias:** Mengukur kesenjangan upah berbasis gender (*gender wage gap*) secara objektif menggunakan variabel kontrol dummy kontrol.

---

## 📊 Dataset & Karakteristik Data
Dataset riil yang digunakan dalam proyek ini adalah **Salary Data** yang diperoleh secara terbuka dari Kaggle. Dataset ini berisi **6.704 observasi individu** yang dikompilasi dari survei industri dan pangkalan data ketenagakerjaan publik.

### 1. Metadata Variabel
Berikut adalah taksonomi variabel yang dianalisis dalam model regresi:

|Variabel|Jenis Data|Deskripsi|Unit Pengukuran|
|:---|:---|:---|:---|
|`Age`|Numerik (Rasio)|Usia biologis karyawan |Tahun|
|`Gender`|Kategorikal (Nominal)|Identitas gender pekerja |Male, Female, Other|
|`Education Level`|Kategorikal (Ordinal)|Tingkat pendidikan formal tertinggi |High School, Bachelor's, Master's, PhD|
|`Years of Experience`|Numerik (Rasio)|Masa kerja profesional akumulatif |Tahun|
|`Salary`|Numerik (Rasio)|Tingkat pendapatan tahunan |Dolar AS (USD)|

### 2. Statistik Deskriptif Sampel
Analisis awal menunjukkan distribusi demografis sampel terdiri atas **3.671 pekerja laki-laki**, **3.013 pekerja perempuan**, dan **14 pekerja** dengan identitas gender lainnya (*other*). 

Rata-rata pendapatan tahunan berdasarkan profil demografis adalah sebagai berikut :
* **Sekolah Menengah (High School):** Perempuan (USD 30.368) vs Laki-laki (USD 39.381)
* **Sarjana (Bachelor's):** Perempuan (USD 89.165) vs Laki-laki (USD 98.972)
* **Magister (Master's):** Perempuan (USD 122.695) vs Laki-laki (USD 140.061)
* **Doktor (PhD):** Perempuan (USD 160.266) vs Laki-laki (USD 168.711)

---

## 🔬 Metodologi & Spesifikasi Model

Untuk mengakomodasi variabel kategorikal ke dalam persamaan linear, tingkat pendidikan formal diubah menjadi variabel dummy dengan menetapkan kategori **Sekolah Menengah (*High School*)** sebagai referensi baseline. Variabel gender dikodekan dengan menetapkan kategori **Laki-laki (*Male*)** sebagai baseline acuan.

Persamaan teoritis model regresi linear berganda dirumuskan sebagai berikut:

$$Salary_i=\beta_0+\beta_1(Age_i)+\beta_2(Experience\_Years_i)+\beta_3(Bachelor_i)+\beta_4(Master_i)+\beta_5(PhD_i)+\beta_6(Female_i)+\beta_7(Other\_Gender_i)+\epsilon_i$$

Di mana:
* $Salary_i$ = Estimasi gaji tahunan individu ke-$i$.
* $\beta_0$ = Parameter intersep (nilai dasar gaji untuk kontrol baseline).
* $\beta_1, \beta_2$ = Koefisien regresi untuk variabel numerik `Age` dan `Years of Experience`.
* $\beta_3, \beta_4, \beta_5$ = Koefisien dampak parsial tingkat pendidikan formal relatif terhadap lulusan *High School*.
* $\beta_6, \beta_7$ = Koefisien dampak parsial identitas gender pekerja relatif terhadap kategori *Male*.
* $\epsilon_i$ = Istilah galat acak (*error term*).

> ⚠️ **Catatan Metodologi:** Model ini secara khusus menguji dan mengontrol korelasi linear yang kuat antara variabel `Age` (Usia) dan `Years of Experience` (Pengalaman Kerja) untuk meminimalkan dampak bias multikolinearitas yang dapat membengkakkan kesalahan standar (*standard error*) dari koefisien model.
