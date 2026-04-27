# ☁️ Beijing Air Quality Analysis Dashboard ✨

Proyek ini merupakan Submission Akhir untuk kelas **Belajar Fundamental Analisis Data** di Dicoding. Dashboard ini dibuat untuk memonitor dan menganalisis tren polusi udara (PM2.5) di berbagai stasiun pemantauan di Beijing, membandingkan kualitas udara antar wilayah, serta melihat korelasi antara kondisi meteorologi (seperti kecepatan angin) terhadap tingkat polusi.

## 🌐 Akses Dashboard (Streamlit Cloud)

Anda tidak perlu melakukan instalasi apa pun untuk melihat hasil analisis ini. Dashboard telah di-deploy secara publik dan dapat diakses langsung melalui tautan berikut:

👉 **[Link Streamlit App: https://beijing-air-quality-dashboard-hafizh.streamlit.app/]**

---

## 💻 Cara Menjalankan Dashboard Secara Lokal

Jika Anda ingin menjalankan proyek ini secara lokal di mesin Anda, silakan ikuti panduan *setup environment* di bawah ini. Pastikan Anda sudah berada di dalam direktori proyek (`submission`).

### Setup Environment - Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal (menggunakan venv)

```bash
# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment (Windows)
.\venv\Scripts\activate

# Mengaktifkan virtual environment (Mac/Linux)
source venv/bin/activate

# Install semua library pendukung
pip install -r requirements.txt
```

### Run Streamlit App

Setelah environment aktif dan seluruh dependensi ter-install, jalankan aplikasi Streamlit dengan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

Aplikasi akan otomatis terbuka di browser bawaan Anda melalui http://localhost:8501.

---

## 👤 Informasi Pembuat

**Dibuat oleh:** Hafizh Iman Wicaksono

**Email:** hafizhimanwicaksono@gmail.com

**ID Dicoding:** hafizhiman
