import streamlit as st
st.markdown("""
<style>
/* === Background terang === */
html, body, [class*="css"] {
    background-color: #f5f7fa !important;
    color: #222 !important;
    font-family: 'Poppins', sans-serif !important;
}

/* === Semua teks dan label jadi hitam === */
body, p, span, div, label, h1, h2, h3, h4, h5, h6 {
    color: #222 !important;
}

/* === Heading pakai warna hijau elegan === */
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #1d6e52 !important;
    font-weight: 600 !important;
}

/* === Sidebar hijau tua === */
[data-testid="stSidebar"] {
    background-color: #114e3a !important;
}
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* === Tabel dan card jadi terang === */
.dataframe th {
    background-color: #1d6e52 !important;
    color: white !important;
}
.dataframe td {
    color: #222 !important;
}
div[data-testid="stVerticalBlock"] {
    background-color: #ffffff !important;
    border-radius: 12px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    padding: 1rem 1.5rem;
}

/* === Tombol hijau === */
div.stButton > button {
    background-color: #1d6e52 !important;
    color: white !important;
    border-radius: 6px;
    border: none;
    padding: 0.5rem 1rem;
}
div.stButton > button:hover {
    background-color: #145b3b !important;
    transform: translateY(-2px);
}

/* === Hilangkan footer Streamlit === */
footer, #MainMenu {visibility: hidden;}
</style>

""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Tambahan untuk hilangin background hitam global === */
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
section.main,
main {
    background-color: #f5f7fa !important;  /* warna putih lembut */
    color: #222 !important;  /* pastikan teks tetap gelap */
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Ubah warna top bar (header Streamlit) === */
header[data-testid="stHeader"] {
    background-color: #f5f7fa !important;  /* ganti hitam ke putih lembut */
    color: #222 !important;
    border-bottom: 1px solid #e0e0e0 !important; /* garis pemisah halus */
    box-shadow: none !important;
}

/* Hilangkan efek shadow gelap di bawah top bar */
header[data-testid="stHeader"] div {
    background-color: #f5f7fa !important;
}

/* Ubah warna ikon "Deploy" dan panah kiri di top bar */
header [data-testid="stToolbarActions"] * {
    color: #1d6e52 !important; /* ikon hijau elegan */
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Fix dropdown portal (list hitam) === */
div[data-baseweb="popover"] {
    background-color: #ffffff !important;   /* ubah latar jadi putih */
    color: #222 !important;                 /* teks hitam */
    border: 1px solid #ccc !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
}

/* Item di dalam list dropdown */
div[data-baseweb="popover"] li {
    background-color: #ffffff !important;
    color: #222 !important;
}

/* Hover state item dropdown */
div[data-baseweb="popover"] li:hover {
    background-color: #e8f5e9 !important;   /* hijau muda */
    color: #1d6e52 !important;
}

/* Saat dropdown aktif, border hijau */
div[data-baseweb="select"]:focus-within > div {
    border: 1px solid #1d6e52 !important;
    box-shadow: 0 0 0 2px rgba(29, 110, 82, 0.2) !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Perbaiki warna Selectbox / Dropdown === */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;  /* background dropdown */
    color: #222 !important;                /* teks hitam */
    border: 1px solid #ccc !important;
    border-radius: 6px !important;
}

/* === Saat fokus / hover === */
div[data-baseweb="select"]:focus-within > div,
div[data-baseweb="select"] > div:hover {
    border: 1px solid #1d6e52 !important;
    box-shadow: 0 0 0 2px rgba(29, 110, 82, 0.2) !important;
}

/* === Item di dalam dropdown list === */
ul[role="listbox"] {
    background-color: #ffffff !important; /* dropdown list putih */
    color: #222 !important;               /* teks hitam */
    border-radius: 6px !important;
}

/* Item highlight saat hover */
ul[role="listbox"] > li:hover {
    background-color: #e8f5e9 !important; /* hijau muda */
    color: #1d6e52 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* === Fix dropdown portal (list hitam) === */
div[data-baseweb="popover"] {
    background-color: #ffffff !important;   /* ubah latar jadi putih */
    color: #222 !important;                 /* teks hitam */
    border: 1px solid #ccc !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
}

/* Item di dalam list dropdown */
div[data-baseweb="popover"] li {
    background-color: #ffffff !important;
    color: #222 !important;
}

/* Hover state item dropdown */
div[data-baseweb="popover"] li:hover {
    background-color: #e8f5e9 !important;   /* hijau muda */
    color: #1d6e52 !important;
}

/* Saat dropdown aktif, border hijau */
div[data-baseweb="select"]:focus-within > div {
    border: 1px solid #1d6e52 !important;
    box-shadow: 0 0 0 2px rgba(29, 110, 82, 0.2) !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Styling Tabel Rapi Dengan Border === */
table.dataframe {
    width: 100% !important;
    border-collapse: collapse !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    font-size: 0.9rem !important;
    margin-top: 10px !important;
    margin-bottom: 25px !important;
    border: 1px solid #d0d0d0 !important; /* 🔹 border luar tabel */
}

/* Header tabel */
table.dataframe thead th {
    background-color: #1d6e52 !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    text-align: center !important;
    padding: 10px !important;
    border: 1px solid #c0c0c0 !important; /* 🔹 border antar header */
}

/* Baris tabel */
table.dataframe tbody tr {
    background-color: #ffffff !important;
    border-bottom: 1px solid #e0e0e0 !important;
}

/* Zebra stripe */
table.dataframe tbody tr:nth-child(even) {
    background-color: #f9f9f9 !important;
}

/* Sel tabel */
table.dataframe td {
    padding: 8px 12px !important;
    color: #222 !important;
    text-align: right !important;
    border: 1px solid #d0d0d0 !important; /* 🔹 border antar sel */
}

/* Kolom terakhir (Nama Pakaian) rata kiri */
table.dataframe td:last-child {
    text-align: left !important;
}

/* Hover row effect */
table.dataframe tbody tr:hover {
    background-color: #e8f5e9 !important;
    transition: background-color 0.2s ease-in-out;
}

/* Sudut tabel */
table.dataframe {
    border-radius: 8px !important;
    overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Styling tombol download (CSV, Excel, dsb) === */
div[data-testid="stDownloadButton"] > button {
    background-color: #1d6e52 !important;  /* hijau elegan */
    color: #ffffff !important;             /* teks putih */
    border: none !important;
    border-radius: 6px !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    transition: all 0.2s ease-in-out !important;
    box-shadow: 0 3px 6px rgba(0,0,0,0.1) !important;
}

/* Hover effect */
div[data-testid="stDownloadButton"] > button:hover {
    background-color: #145b3b !important;  /* sedikit lebih gelap */
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
}

/* Saat tombol disabled (belum siap diunduh) */
div[data-testid="stDownloadButton"] > button:disabled {
    background-color: #ccc !important;
    color: #666 !important;
    cursor: not-allowed !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* === Styling elegan untuk komponen file uploader === */
[data-testid="stFileUploader"] {
    background-color: #ffffff !important; /* Putih bersih */
    border: 2px dashed #1d6e52 !important; /* Hijau lembut */
    border-radius: 12px !important;
    padding: 1.5rem !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    transition: all 0.3s ease-in-out;
}

/* Hover effect */
[data-testid="stFileUploader"]:hover {
    border-color: #145b3b !important;
    box-shadow: 0 6px 16px rgba(0,0,0,0.1) !important;
}

/* === Warna tombol "Browse files" === */
button[title="Browse files"],
div[data-testid="stFileUploader"] button {
    background-color: #1d6e52 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
    padding: 0.4rem 1.2rem !important;
    transition: all 0.2s ease-in-out !important;
}

/* Hover tombol */
button[title="Browse files"]:hover,
div[data-testid="stFileUploader"] button:hover {
    background-color: #145b3b !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
}

/* === Teks drag and drop === */
[data-testid="stFileUploaderDropzone"] div {
    color: #1d6e52 !important;
    font-weight: 500 !important;
    font-size: 0.95rem !important;
}

/* Hilangkan warna hitam pekat area drop */
[data-testid="stFileUploaderDropzone"] {
    background-color: #f9fafb !important;
}

/* === Ikon cloud di tengah === */
[data-testid="stFileUploaderIcon"] svg {
    color: #1d6e52 !important;
    width: 36px !important;
    height: 36px !important;
}
</style>
""", unsafe_allow_html=True)

import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import io
import time
from io import BytesIO
import os


# Inisialisasi state untuk menandakan bahwa aplikasi baru saja dimulai
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.page = 'Home'
    st.session_state.show_label_column = True  # Menandakan apakah kolom label harus ditampilkan
    st.session_state.cluster_1 = None
    st.session_state.cluster_2 = None
    
# Fungsi untuk membaca atau membuat dataset
@st.cache_data
def load_or_create_dataset():
    try:
        df = pd.read_csv("data/jenis_pakaian.csv")
    except FileNotFoundError: 
        df = pd.DataFrame(columns=['label', 'stok_awal', 'stok_akhir', 'terjual'])
    return df

# Fungsi untuk Elbow Method
def elbow_method(data):
    clusters = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i).fit(data)
        clusters.append(km.inertia_)

    # Mencari indeks elbow (titik di mana penurunan inersia tidak signifikan)
    elbow_index = -1
    for i in range(1, len(clusters) - 1):
        if (clusters[i - 1] - clusters[i]) / (clusters[i] - clusters[i + 1]) > 0.1:
            elbow_index = i
            break

    # Plot hasil Elbow Method dengan penanda elbow
    fig_elbow, ax_elbow = plt.subplots(figsize=(12, 8))
    sns.lineplot(x=list(range(1, 11)), y=clusters, ax=ax_elbow, marker='o')
    ax_elbow.set_title("Elbow Method")
    ax_elbow.set_xlabel("Jumlah Cluster")
    ax_elbow.set_ylabel("Inertia")
    
    # Menambahkan penanda elbow
    optimal_clusters = elbow_index + 1
    ax_elbow.annotate('Elbow Point', xy=(optimal_clusters, clusters[elbow_index]), xytext=(optimal_clusters, clusters[elbow_index] + 100), arrowprops=dict(facecolor='red', shrink=0.05))
    
    st.pyplot(fig_elbow)

    return optimal_clusters

# Fungsi untuk melakukan clustering
def perform_clustering(data, n_clusters):

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    data['cluster'] = kmeans.fit_predict(data[['stok_awal', 'stok_akhir', 'terjual']])
    center_points = pd.DataFrame(kmeans.cluster_centers_, columns=['stok_awal', 'stok_akhir', 'terjual'])
    
    return data, kmeans.inertia_, center_points  # Tambahkan return untuk data asli

def clustering(original_data) :
    
    clean_data = original_data.drop(['label'], axis=1)
    
    st.subheader("1. Menentukan jumlah cluster")
    
    # Elbow Method
    # optimal_clusters = elbow_method(clean_data)
    optimal_clusters = st.slider("Jumlah Cluster", min_value=1, max_value=10)
    
    st.subheader("2. Melakukan Perhitungan K-Means")
    # Plot hasil clustering
    data, inertia, center_points = perform_clustering(clean_data, optimal_clusters)
    
    # Inisialisasi session state untuk hasil clustering
    for i in range(10):
        st.session_state[f"cluster_{i + 1}"] = pd.DataFrame()

    
    # Perbarui data hasil clustering dalam session state
    for i in range(optimal_clusters):
        st.session_state[f"cluster_{i + 1}"] = data[data['cluster'] == i]

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(x='stok_awal', y='stok_akhir', hue='cluster', data=data, palette='viridis', ax=ax)
    sns.scatterplot(x=center_points['stok_awal'], y=center_points['stok_akhir'], color='red', marker='X', s=300, label='Center Point', ax=ax)
    
    for i, center in center_points.iterrows():
        ax.text(center['stok_awal'], center['stok_akhir'], f'Cluster {i + 1}', fontsize=12, color='black', ha='center', va='top')
    ax.set_title("Hasil Clustering dengan KMeans")
    ax.set_xlabel("Stok Awal")
    ax.set_ylabel("Stok Akhir")
    st.pyplot(fig)

    st.write("Inertia (Jumlah total jarak kuadrat antar data dengan center cluster):", int(inertia))
    
    st.session_state.show_label_column = True
    
    # Tampilkan data sesuai kluster dalam tabel
    st.subheader("Hasil Clustering :")
    for cluster_id in range(optimal_clusters):
        cluster_data = data[data['cluster'] == cluster_id]
        st.write(f"Cluster {cluster_id +1 }:")

        # Tampilkan kolom label sesuai indeks data dalam cluster
        if 'label' in original_data.columns:
            # Dapatkan label dari data asli berdasarkan indeks
            cluster_data['Nama Pakaian'] = original_data.loc[cluster_data.index, 'label'].values
        else:
            # Jika kolom 'label' tidak ada, gunakan indeks data sebagai label
            cluster_data['Nama Pakaian'] = cluster_data.index.astype(str)

        if 'Nama Pakaian' in cluster_data.columns:
            cluster_copy = cluster_data.copy()
            cluster_copy.columns = [ 'Stok Awal', 'Stok Akhir', 'Terjual', 'Cluster','Nama Pakaian']
            cluster_copy['Cluster'] = cluster_copy['Cluster'] + 1
            # st.markdown(cluster_copy.to_html(index=False), unsafe_allow_html=True)
# Format angka agar tidak ada .0
            cluster_copy = cluster_copy.copy()
            for col in ['Stok Awal', 'Stok Akhir', 'Terjual']:
                cluster_copy[col] = cluster_copy[col].astype(int)

            # Render ke HTML rapi
            st.markdown(cluster_copy.to_html(index=False), unsafe_allow_html=True)

            # st.table(cluster_copy.style.format(precision=0))
        else:
            st.table(Dcluster_data[['stok_awal', 'stok_akhir', 'terjual']].style.format(precision=0))

        # Simpan hasil clustering ke dalam session state
        st.session_state[f"cluster_{cluster_id + 1}"] = cluster_data
    
@st.cache_data
def convert_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')
    

# Halaman Home
def home():
    st.title("Aplikasi Clustering Pakaian")
    st.write("Laporan dan Analisis Data Pakaian")
    
    st.header("5 Data Terbaru")
    original_data = load_or_create_dataset()
    
    # Data terbaru bersama dengan kolom label
    latest_data = load_or_create_dataset().tail(5)
    
    # Ganti nama kolom sesuai dengan yang diinginkan
    latest_data.columns = ['Stok Awal', 'Stok Akhir', 'Terjual','Nama Pakaian']

    st.table(latest_data.style.format(precision=0))

    clustering(original_data)

# Halaman Input Data
def input_data():
    st.title("Input Data Baru")
    new_data = st.text_input("Nama Pakaian")
    stok_awal = st.number_input("Stok Awal",  format='%g')
    stok_akhir = st.number_input("Stok Akhir", format='%g')
    terjual = st.number_input("Terjual", format='%g')

    if st.button("Tambahkan Data"):
        new_row = {'label': new_data, 'stok_awal': stok_awal, 'stok_akhir': stok_akhir, 'terjual': terjual}
        df = pd.concat([load_or_create_dataset(), pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv("data/jenis_pakaian.csv", index=False)
        st.success("Data berhasil ditambahkan!")

#Halaman Import
def import_csv():
    st.title("📦 Import Data CSV")
    st.write(
        "Unggah file CSV baru untuk menambahkan data ke dataset utama. "
        "Jika label sudah ada, data lama akan **tetap dipertahankan**."
    )

    uploaded_file = st.file_uploader("Pilih file CSV", type=['csv'])

    if uploaded_file is not None:
        try:
            new_data = pd.read_csv(uploaded_file, encoding='utf-8-sig')
            new_data.columns = new_data.columns.str.strip().str.lower()

            expected_cols = ['stok_awal', 'stok_akhir', 'terjual', 'label']
            if not all(col in new_data.columns for col in expected_cols):
                st.error(f"❌ Kolom CSV tidak sesuai. Kolom ditemukan: {new_data.columns.tolist()}")
                return

            # 🔹 Pastikan kolom angka bener-bener numerik
            for col in ['stok_awal', 'stok_akhir', 'terjual']:
                new_data[col] = pd.to_numeric(new_data[col], errors='coerce')

            # 🔹 Tentukan lokasi file CSV utama (venv/app/data)
            base_dir = os.path.dirname(__file__)
            data_dir = os.path.join(base_dir, "../data")
            os.makedirs(data_dir, exist_ok=True)
            csv_path = os.path.join(data_dir, "jenis_pakaian.csv")

            # 🔹 Baca dataset lama
            try:
                old_data = pd.read_csv(csv_path, encoding='utf-8-sig')
            except FileNotFoundError:
                old_data = pd.DataFrame(columns=expected_cols)

            st.info(f"📊 Data lama: {len(old_data)} baris | Data baru: {len(new_data)} baris")

            # 🔹 Tambahkan data baru TANPA mengganti yang lama (mode Skip)
            combined_data = old_data.copy()
            for _, row in new_data.iterrows():
                label = row['label']
                if label not in combined_data['label'].values:
                    combined_data = pd.concat([combined_data, pd.DataFrame([row])], ignore_index=True)

            # 🔹 Simpan hasil akhir (encoding benar)
            combined_data.to_csv(csv_path, index=False, encoding='utf-8-sig')

            # 🔹 Bersihkan cache dan refresh halaman
            st.cache_data.clear()
            st.success(f"✅ Import selesai! Total data sekarang: {len(combined_data)} baris.")
            st.dataframe(combined_data.tail(10))

            # 🔹 Auto balik ke Home
            st.toast("📈 Data berhasil diimport! Halaman akan diperbarui...")
            time.sleep(1.5)
            st.session_state.page = "Home"
            st.rerun()


        except Exception as e:
            st.error(f"❌ Gagal mengimpor file CSV: {e}")



# Halaman Cetak Laporan
def cetak_laporan():
    st.title("Cetak Laporan")
    st.write("Hasil Clustering") 
    
    if all(st.session_state[f"cluster_{i + 1}"] is None or st.session_state[f"cluster_{i + 1}"].empty for i in range(10)):
        st.warning("Silahkan lakukan clustering terlebih dulu")
    else:

        # Create a Pandas DataFrame to combine all cluster data
        combined_data =pd.concat([st.session_state[f"cluster_{i + 1}"] for i in range(10)], ignore_index=True)
        
        # Mengubah nilai cluster di dalam data gabungan
        combined_data['cluster'] += 1


        # Tombol untuk download seluruh data cluster format Excel 
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            combined_data.to_excel(writer, sheet_name='Combined_Cluster_Results', index=False)
        
        download_excel_button = st.download_button(
            label="Download Combined Data format Excel",
            data=excel_buffer,
            file_name="Laporan.xlsx",
            mime='application/vnd.ms-excel'
        )
            

    for cluster_id in range(1, 11):
        if st.session_state[f"cluster_{cluster_id}"] is None or st.session_state[f"cluster_{cluster_id}"].empty:
            st.warning(f"Cluster {cluster_id} belum ditemukan. Silahkan lakukan clustering terlebih dulu.")
        else:        
            st.subheader(f"Cluster {cluster_id}")
            st.table(st.session_state[f"cluster_{cluster_id}"][['Nama Pakaian', 'stok_awal', 'stok_akhir', 'terjual']].style.format(precision=0))
            
            # Tombol Download CSV
            csv_data = convert_to_csv(st.session_state[f"cluster_{cluster_id}"])
            download_csv_button = st.download_button(
                label=f"Download Data Cluster {cluster_id} format CSV",
                data=csv_data,
                file_name=f'Cluster_{cluster_id}_Results.csv',
                mime='text/csv'
            )

            # Tombol Download Excel
            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                st.session_state[f"cluster_{cluster_id}"].to_excel(writer, sheet_name=f'Cluster_{cluster_id}_Results', index=False)

            download_excel_button = st.download_button(
                label=f"Download Data Cluster {cluster_id} format Excel",
                data=excel_buffer,
                file_name=f'Cluster_{cluster_id}_Results.xlsx',
                mime='application/vnd.ms-excel'
            )

# Halaman Kelola Data
def kelola_data():
    st.title("Kelola Dataset")
    st.write("Data Stok Pakaian")
    df = load_or_create_dataset()
    df_copy = df.copy()
    df_copy.columns = [ 'Stok Awal', 'Stok Akhir', 'Terjual','Nama Pakaian',]
    df_copy.insert(0, 'ID', range(1, len(df_copy) + 1))

    # 🔹 Konversi nilai angka ke integer agar tidak muncul .0
    for col in ['Stok Awal', 'Stok Akhir', 'Terjual']:
        df_copy[col] = df_copy[col].astype(int)

    # 💅 Render tabel rapi pakai HTML agar CSS aktif
    st.markdown(df_copy.to_html(index=False), unsafe_allow_html=True)
    # st.table(df_copy.style.format(precision=0))
    
    
    
    
    # Fungsi untuk mengupdate data dalam tabel
    def update_data(df):
        st.subheader("Update Data")
        # selected_index = st.selectbox("Pilih indeks data yang akan diupdate", df.index)
        # Tampilkan label tapi tetap kirim index-nya
        options = {row.Index: row.label for row in df.itertuples()}
        selected_index = st.selectbox(
            "Pilih data pakaian yang akan diupdate",
            options.keys(),
    format_func=lambda x: options[x]
)

        selected_data = df.loc[selected_index]

        new_label = st.text_input("Nama Pakaian", selected_data['label'])
        new_stok_awal = st.number_input("Stok Awal", value=int(selected_data['stok_awal']), format='%d')
        new_stok_akhir = st.number_input("Stok Akhir", value=int(selected_data['stok_akhir']), format='%d')
        new_terjual = st.number_input("Terjual", value=int(selected_data['terjual']), format='%d')

        if st.button("Update Data"):
            df.loc[selected_index] = [ new_stok_awal, new_stok_akhir, new_terjual,new_label]
            df.to_csv("data/jenis_pakaian.csv", index=False)
            st.cache_data.clear()
            st.success("Data berhasil diupdate!")
            st.rerun()    
            
            # time.sleep(2)
            # st.rerun()


    # Fungsi untuk menghapus data dalam tabel
    def delete_data(df):
        st.subheader("Delete Data")
        # selected_index = st.selectbox("Pilih indeks data yang akan dihapus", df.index)
        options = {row.Index: row.label for row in df.itertuples()}
        selected_index = st.selectbox(
            "Pilih data pakaian yang akan dihapus",
            options.keys(),
            format_func=lambda x: options[x]
        )
        selected_data = df.loc[selected_index]

        st.write("Data yang akan dihapus:")
        st.table(selected_data[['label', 'stok_awal', 'stok_akhir', 'terjual']])
         
        # Konfirmasi sebelum menghapus data
        confirm_delete = st.checkbox("Saya yakin  menghapus data ini.")
        if st.button("Hapus Data"):
            if confirm_delete:
                df.drop(selected_index, inplace=True)
                df.to_csv("data/jenis_pakaian.csv", index=False)
                st.cache_data.clear()
                st.success("Data berhasil dihapus!.")
                # time.sleep(2)
                st.rerun() 
            else:
                st.info("Penghapusan data dibatalkan.")
    
    
    action = st.radio("Pilih Aksi", ("Update Data", "Hapus Data"))

    if action == "Update Data":
        update_data(df)
    elif action == "Hapus Data":
        delete_data(df)

def main():
    st.sidebar.title("Menu")

    home_page = st.sidebar.button("🏠 Home", key="home_btn")
    kelola_data_page = st.sidebar.button("🧾 Kelola Data", key="kelola_btn")
    input_data_page = st.sidebar.button("➕ Input Data", key="input_btn")
    cetak_laporan_page = st.sidebar.button("📊 Cetak Laporan", key="laporan_btn")
    import_csv_page = st.sidebar.button("📥 Import CSV", key="import_btn")  # 🟢 tambahin key unik

    # Tentukan halaman aktif
    if home_page:
        st.session_state.page = 'Home'
    elif kelola_data_page:
        st.session_state.page = 'Kelola Data'
    elif input_data_page:
        st.session_state.page = 'Input Data'
    elif cetak_laporan_page:
        st.session_state.page = 'Cetak Laporan'
    elif import_csv_page:
        st.session_state.page = 'Import CSV'

    # Render halaman sesuai state
    if st.session_state.page == 'Home':
        home()
    elif st.session_state.page == 'Kelola Data':
        kelola_data()
    elif st.session_state.page == 'Input Data':
        input_data()
    elif st.session_state.page == 'Cetak Laporan':
        cetak_laporan()
    elif st.session_state.page == 'Import CSV':
        import_csv()


if __name__ == "__main__":
    main()
