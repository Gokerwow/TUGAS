# Analisis Motivasi Belajar Mahasiswa

Proyek ini bertujuan untuk menganalisis motivasi belajar mahasiswa berdasarkan data survei. Dengan menggunakan Python, program ini menghasilkan visualisasi yang membantu memahami hubungan antara berbagai faktor seperti manajemen waktu, jam belajar, prokrastinasi, dan motivasi mahasiswa.

## Fitur Program
1. Membersihkan dan memproses data dari file CSV.
2. Mengelompokkan motivasi mahasiswa menjadi dua kategori: **Termotivasi** dan **Tidak Termotivasi**.
3. Membuat model **Decision Tree Classifier** untuk analisis data.
4. Menghasilkan visualisasi data dalam bentuk grafik, seperti:
   - Pohon keputusan (Decision Tree).
   - Hubungan antara jam belajar, prokrastinasi, dan motivasi.
   - Pengaruh kerja paruh waktu terhadap motivasi.
   - Proporsi motivasi berdasarkan usia dan program studi.
   - Hubungan manajemen waktu dan jam belajar.

## Persyaratan Sistem
- **Python**: Versi 3.7 atau lebih baru.
- **Pustaka Python yang dibutuhkan**:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `imbalanced-learn`

## Cara Menjalankan Program

### 1. Persiapan
- Pastikan Python telah diinstal di komputer Anda. Jika belum, unduh dan instal Python dari [python.org](https://www.python.org/downloads/).
- Instal pustaka yang dibutuhkan dengan menjalankan perintah berikut di terminal atau command prompt:

  ```bash
  pip install pandas matplotlib seaborn scikit-learn imbalanced-learn
  ```

### 2. Siapkan Data
- Pastikan Anda memiliki file CSV yang berjudul:
  `Prediksi motivasi belajar mahasiswa (Responses) - Form responses 1 (2).csv`.
- Letakkan file ini di folder yang sama dengan skrip Python.

### 3. Jalankan Program
- File kode bisa didownload secara manual dan dimasukkan Pada VS Code atau Dapat melakukan clone pada repository
- Jalankan Kode

### 4. Hasil
Setelah program dijalankan, beberapa grafik visualisasi akan dihasilkan dan disimpan sebagai file gambar di folder yang sama dengan skrip. Nama file yang dihasilkan meliputi:
- `Decision tree hasil.png`
- `motivation_decision_tree.png`
- `part_time_job_count.png`
- `motivation_age_program_stacked.png`
- `time_management_study_hours_line.png`

File dapat dibuka dalam VS Code itu sendiri, atau bisa pergi ke path dimana file kode tersimpan

## Format Data
Pastikan file CSV Anda memiliki kolom-kolom berikut agar program dapat berjalan dengan baik:
- **"Apakah anda merasa termotivasi untuk melakukan yang terbaik di bidang akademik?"**
- **"Berapa jam per hari Anda alokasikan untuk belajar di luar jam kuliah?"**
- **"Seberapa teratur Anda dalam membuat jadwal harian atau mingguan untuk kegiatan akademik dan non-akademik?"**
- **"Apakah Anda sering menunda-nunda tugas kuliah?"**

Jika nama kolom berbeda, sesuaikan nama kolom di skrip Python.

## Jika Terjadi Error
- Pastikan semua pustaka telah diinstal dengan benar.
- Periksa format dan isi file CSV.
- Pastikan Anda menggunakan versi Python yang sesuai (disarankan versi 3.7 atau lebih baru).
