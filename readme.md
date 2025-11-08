# 🧥 Aplikasi Clustering Pakaian (Streamlit + K-Means)

Aplikasi interaktif berbasis **Streamlit** untuk melakukan *clustering* data stok pakaian menggunakan algoritma **K-Means**.  
Dibangun untuk membantu analisis stok penjualan dan pengelompokan produk berdasarkan data *stok awal*, *stok akhir*, serta *jumlah terjual*.  

Tampilan dibuat modern dengan tema **hijau-putih elegan**, serta mendukung **CRUD (Create, Read, Update, Delete)** dan **Import/Export CSV** langsung dari UI.

---

## 🌿 Deskripsi Singkat

Aplikasi ini berfungsi untuk:
- Mengelompokkan data pakaian menggunakan **K-Means Clustering**.
- Menambahkan, mengedit, dan menghapus data tanpa restart aplikasi.
- Mengimpor file CSV tambahan ke dataset utama tanpa menghapus data lama.
- Mengekspor hasil clustering ke file Excel dan CSV.
- Menampilkan visualisasi data yang interaktif dan menarik.

---

## 🚀 Fitur Utama

| Fitur | Deskripsi |
|-------|------------|
| 🧠 **Clustering Otomatis (K-Means)** | Mengelompokkan pakaian berdasarkan *stok awal*, *stok akhir*, dan *jumlah terjual*. |
| 📊 **Visualisasi Interaktif** | Menampilkan hasil clustering dalam bentuk grafik scatter dan tabel data yang rapi. |
| 🧾 **Kelola Data Langsung** | Tambah, update, dan hapus data langsung dari antarmuka aplikasi. |
| 📥 **Import CSV Tambahan** | Tambahkan data baru dari file CSV tanpa menghapus data lama. |
| 💾 **Ekspor Data Cepat** | Download hasil clustering ke format Excel atau CSV. |
| 🎨 **UI Custom Elegan** | Tampilan modern dengan CSS hijau-putih yang lembut dan profesional. |

---

## 📁 Struktur Folder Project

```
📦 Klustering-Pakaian/
├── venv/
│   ├── app/
│   │   ├── src/
│   │   │   └── app.py               # File utama aplikasi Streamlit
│   │   └── data/
│   │       └── jenis_pakaian.csv    # Dataset utama aplikasi
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
├── requirements.txt
└── README.md
```
---

> 💡 **Catatan Penting:**  
> - Semua file data disimpan di folder: `venv/app/data/jenis_pakaian.csv`  
> - Jalankan aplikasi dari folder `venv/app/src` menggunakan:
>   ```bash
>   streamlit run app.py
>   ```
> - Folder `data/` akan otomatis dibuat jika belum ada.
