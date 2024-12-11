# **Proyek Analisis Kualitas Udara: Stasiun Wanshouxigong**

## Live Dashboard
[https://maireza-airquality.streamlit.app/](https://maireza-airquality.streamlit.app/)

## Gambaran Umum Proyek
Proyek ini merupakan tugas untuk kursus **"Belajar Analisis Data dengan Python"** di Dicoding. Fokus utama adalah menganalisis data kualitas udara, khususnya tingkat PM2.5, dari stasiun Wanshouxigong. Tujuannya adalah mengungkap tren, variasi musiman, serta dampak kondisi cuaca terhadap kualitas udara.

## Pengumpulan Tugas
Proyek ini diajukan sebagai tugas akhir untuk kursus **"Belajar Analisis Data dengan Python"** yang diselenggarakan oleh Dicoding. Proyek ini menunjukkan penerapan teknik analisis data serta keterampilan visualisasi yang telah dipelajari selama kursus.

---

## **Daftar Isi**
- [Pendahuluan](#pendahuluan)
- [Sumber Data](#sumber-data)
- [Pustaka yang Digunakan](#pustaka-yang-digunakan)
- [Temuan Utama](#temuan-utama)
- [Cara Menjalankan Dashboard](#cara-menjalankan-dashboard)
- [Tentang Saya](#tentang-saya)

---

## **Pendahuluan**
Proyek ini bertujuan untuk menganalisis data kualitas udara, khususnya konsentrasi polutan PM2.5, dan memahami hubungannya dengan berbagai faktor lingkungan. Analisis ini mencakup identifikasi tren, pola musiman, serta korelasi dengan kondisi cuaca.

---

## **Sumber Data**
Dataset yang digunakan dalam proyek ini mencakup pengukuran kualitas udara dari stasiun Wanshouxigong, dengan fokus pada tingkat PM2.5 dan data lingkungan terkait lainnya.

---

## **Pustaka yang Digunakan**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **NumPy**
- **SciPy**
- **Statsmodels**

---

## **Temuan Utama**
- **Variasi Musiman**: Tingkat PM2.5 menunjukkan konsentrasi yang lebih tinggi pada bulan-bulan dingin.
- **Korelasi dengan Cuaca**: Polutan PM2.5 memiliki hubungan dengan suhu dan kelembaban.
- **Analisis Tren Waktu**: Tren dan pola penting terungkap melalui analisis data deret waktu.

---

## **Cara Menjalankan Dashboard**

Ikuti langkah-langkah berikut untuk menjalankan aplikasi Streamlit secara lokal:

### **1. Persiapan Lingkungan**
- **Membuat dan Mengaktifkan Lingkungan Python**:
  - **Menggunakan Conda**:
    ```bash
    conda create --name airquality-env python=3.11
    conda activate airquality-env
    ```
  - **Menggunakan venv**:
    ```bash
    python -m venv .env-airquality
    source env-airquality/bin/activate
    ```

- **Instalasi Paket yang Diperlukan**:
  ```bash
  pip install pandas numpy scipy matplotlib seaborn streamlit statsmodels
  ```
  **Atau**, instal melalui file persyaratan:  
  ```bash
  pip install -r requirements.txt
  ```

### **2. Menjalankan Aplikasi Streamlit**
1. **Navigasi ke Folder Proyek**: Pastikan Anda berada di direktori tempat file `dashboard.py` berada.  
2. **Jalankan Aplikasi**:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

### **3. Struktur File Tambahan**
- Dataset yang digunakan dalam analisis disertakan di repositori proyek.  
- Notebook Python yang mendokumentasikan analisis dan visualisasi (`maliki-dicoding-ds-airquality.ipynb`) juga tersedia.
