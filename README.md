# MarqForge

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/mit/)

[![Development Status](https://img.shields.io/badge/status-in%20development-orange)](https://pypi.org/)

**MarqForge** adalah sebuah *modular web security discovery framework* modern yang dirancang untuk kebutuhan pemindaian keamanan, pengumpulan informasi (*reconnaissance*), dan analisis kerentanan web secara otomatis dan terstruktur.

Dengan arsitektur berbasis modul yang dinamis, MarqForge memungkinkan praktisi keamanan siber (pentester) untuk membangun, mengintegrasikan, dan menjalankan berbagai alat bantu penemuan kerentanan (*security tools*) dalam satu ekosistem yang selaras.

---

## ✨ Fitur Utama

- 🧩 **Arsitektur Modular**: Tambah, kurangi, atau modifikasi modul pemindaian tanpa merusak fungsionalitas inti framework.
- ⚙️ **Metadata Dinamis Terpusat**: Versi, lisensi, informasi proyek, dan profil pengembang terintegrasi langsung dengan manajemen paket sistem (`pyproject.toml` & Git Tag).
- 🚀 **Runtime Agnostic & Lightweight**: Memiliki dependensi minimal, cepat dieksekusi, dan menyediakan detail lingkungan runtime yang akurat untuk debugging.
- 🛡️ **Enterprise-Grade Architecture**: Mengikuti standar penulisan kode Python modern (PEP 517/621) dengan pengetikan data yang ketat (*Strict Type Hinting*).

---

## 🚀 Memulai (Getting Started)

### Prasyarat
- **Python 3.8** atau versi yang lebih baru.
- **Git** terinstal di sistem Anda.

### Instalasi Lokal (Mode Pengembangan)

Untuk memasang MarqForge secara lokal agar sinkronisasi versi otomatis dari Git berjalan dengan baik, jalankan perintah berikut di terminal Anda:

```bash
git https://github.com/marqsec/marqforge
cd marqforge

pip install --upgrade pip

pip install -e .
```

---

## 🛠️ Contoh Penggunaan Modul Metadata

MarqForge menyediakan fungsionalitas bawaan untuk membaca profil proyek dan lingkungan runtime secara dinamis tanpa perlu konfigurasi manual:

```python
import marqforge

print(f"Versi Framework : {marqforge.__version__}")
print(f"Pembuat/Author  : {marqforge.__author__}")

runtime = marqforge.get_runtime()
print(f"Berjalan di     : {runtime['platform']} ({runtime['bits']})")
print(f"Versi Python    : {runtime['python']}")

project = marqforge.get_project()
print(f"Deskripsi       : {project['description']}")
```

---

## 📁 Struktur Folder Proyek

```text
MarqForge/
├── chrome-linux/            # Biner browser untuk modul scanning (Dikelola Git LFS)
├── metadata/                # Folder fisik kode utama framework (Dipanggil via 'import marqforge')
│   ├── __init__.py          # Pintu utama export fungsi publik framework
│   ├── author.py            # Modul informasi pembuat dinamis
│   ├── license.py           # Modul aturan lisensi dan hak cipta
│   ├── project.py           # Modul informasi profil proyek
│   ├── runtime.py           # Modul deteksi lingkungan sistem
│   └── version.py           # Modul pelacak versi otomatis
├── tests/                   # Folder untuk unit testing otomatis aplikasi
│   └── test_metadata.py     # Skrip penguji fungsi mendatata dinamis
├── .gitattributes           # Konfigurasi pelacakan file besar Git LFS
├── .gitignore               # Daftar file sampah/cache yang diabaikan oleh Git
├── pyproject.toml           # Konfigurasi manajemen paket modern (PEP 621) tanpa komentar
├── setup.py                 # Konfigurasi paket sinkron untuk kompatibilitas alat lama
└── README.md                # Dokumentasi utama proyek

```

---

## 🤝 Kontribusi

Kami sangat terbuka terhadap kontribusi dari komunitas! Jika Anda ingin menambahkan modul keamanan baru, memperbaiki *bug*, atau meningkatkan performa framework:

1. *Fork* repositori ini.
2. Buat *branch* fitur baru Anda (`git checkout -b fitur/modul-baru`).
3. Lakukan *commit* atas perubahan Anda (`git commit -m 'Menambahkan modul scanning X'`).
4. *Push* ke *branch* tersebut (`git push origin fitur/modul-baru`).
5. Buat sebuah *Pull Request*.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT** - Lihat berkas `LICENSE` untuk detail lebih lanjut. Seluruh aturan hak cipta dan modifikasi dideteksi secara otomatis melalui fungsi `get_license()`.

---

## ⚠️ Pernyataan Penyangkalan (Disclaimer)

*Alat ini dirancang khusus untuk tujuan pendidikan, penelitian keamanan, dan uji penetrasi resmi (*authorized penetration testing*). Penyalahgunaan framework ini untuk aktivitas ilegal atau tanpa izin tertulis dari pemilik sistem sepenuhnya bukan tanggung jawab pengembang MarqForge.*
