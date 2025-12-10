# 🚀 To-Do List Pro (Flask App)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-green?style=for-the-badge&logo=flask)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.0-06B6D4?style=for-the-badge&logo=tailwindcss)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

Aplikasi manajemen tugas (To-Do List) modern dengan fitur lengkap, dibangun menggunakan **Python Flask**. Proyek ini dirancang untuk membantu produktivitas dengan antarmuka **Dark Mode Glassmorphism** yang nyaman di mata.

> **Catatan:** Proyek ini dikembangkan sebagai bagian dari portofolio Mahasiswa Informatika Universitas Mercu Buana Yogyakarta.

---

## ✨ Fitur Utama

✅ **Sistem Autentikasi**: Login & Register aman (Password Hashing dengan `Werkzeug`).  
✅ **CRUD Tugas**: Tambah, Edit, Hapus, dan Tandai Selesai tugas dengan mudah.  
✅ **Manajemen Deadline**: Penanda warna otomatis untuk tugas Hari Ini, Terlambat, atau Mendatang.  
✅ **Kategori & Filter**: Kelompokkan tugas (Kuliah, Pekerjaan, dll) dan filter berdasarkan status.  
✅ **Pencarian Cerdas**: Cari tugas spesifik menggunakan keyword.  
✅ **Modern UI**: Menggunakan Tailwind CSS dengan tema Dark Mode & Glassmorphism.  
✅ **Flash Messages**: Notifikasi interaktif untuk setiap aksi user.  

---

## 📸 Screenshots

*(Kamu bisa ganti bagian ini dengan screenshot aplikasi aslimu nanti)*

| Halaman Login | Dashboard Utama |
|:---:|:---:|
| ![Login UI](https://via.placeholder.com/400x300?text=Login+Screen) | ![Dashboard UI](https://via.placeholder.com/400x300?text=Dashboard+Screen) |

---

## 🛠️ Teknologi yang Digunakan

* **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-Login.
* **Frontend**: HTML5, Jinja2 Template, Tailwind CSS (CDN), Lucide Icons.
* **Database**: SQLite (Default) / PostgreSQL (Production Ready).

---

## 🚀 Cara Install & Jalanin (Localhost)

Ikuti langkah ini untuk menjalankan proyek di komputer kamu:

### 1. Clone Repository
```bash
git clone [https://github.com/username-kamu/nama-repo.git](https://github.com/username-kamu/nama-repo.git)
cd nama-repo
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
### Windows
python -m venv venv
venv\Scripts\activate
```
#### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variable
```bash
Buat file .env di root folder, lalu isi dengan konfigurasi berikut (atau biarkan default di app.py):
Cuplikan kode
SECRET_KEY=kunci_rahasia_kamu_disini
DATABASE_URL=sqlite:///todo.db
```

### 5. Jalankan Aplikasi
```bash
python app.py
```
Buka browser dan akses: http://127.0.0.1:5000/

```bash
📂 Struktur Folder
📂 root/
├── 📂 instance/       # Database SQLite tersimpan di sini
├── 📂 templates/      # File HTML (Jinja2)
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── edit.html
├── .env               # Konfigurasi Environment
├── app.py             # Main Application Logic
├── requirements.txt   # Daftar Library
└── README.md          # Dokumentasi Proyek
```

### 🤝 Kontribusi
Tertarik mengembangkan fitur baru? Silakan fork repository ini dan buat Pull Request!

### Fork Project

```bash
Create Feature Branch (git checkout -b feature/NewFeature)
Commit Changes (git commit -m 'Add some NewFeature')
Push to Branch (git push origin feature/NewFeature)

Open Pull Request
```

📝 Lisensi
Distributed under the MIT License. See LICENSE for more information.

<center> Dibuat dengan ❤️ oleh <a href="https://www.google.com/search?q=https://github.com/username-kamu">Rizal Rio Andiran</a> </center>


-----  

### Tips Tambahan Biar Repo Makin Kece:

1.  **Ganti Username:** Jangan lupa ganti bagian `username-kamu` dan `nama-repo` di kode di atas dengan link GitHub aslimu.
2.  **Screenshot:** Nanti kalau sempat, kamu screenshot tampilan web-nya di laptop (pake Snipping Tool), upload gambarnya ke folder repo (bikin folder `screenshots` misalnya), terus ganti link `https://via.placeholder...` itu dengan path gambarmu (contoh: `screenshots/dashboard.png`). Visual itu penting banget\!

Gimana bro? Udah siap push ke GitHub? Atau mau dibantu cara `git push`-nya sekalian
