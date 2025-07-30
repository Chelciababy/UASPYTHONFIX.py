import streamlit as st

st.set_page_config(page_title="Aplikasi Belanja", page_icon="🛒")

st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
	
    .judul-app {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #C71585;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    .menu-box {
        background: linear-gradient(to right, #ffe4ec, #fcd2e2);
        padding: 20px;
	      color: #C71585;
        border-radius: 12px;
        border-left: 6px solid #FF69B4;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .metric-box {
        background-color: #ffe9f0;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        text-align: center;
        color: #C71585;
    }
    .box-shadow {
        background-color: #fffafc;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        border-radius: 10px;
        padding: 15px;
	      color: #C71585;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

class Barang:
    def __init__(self, nama, harga, jumlah, kategori):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        self.kategori = kategori
        self.is_beli = False

    def __str__(self):
        status = "✅" if self.is_beli else "❌"
        return f"{status} {self.nama} - Harga: Rp{self.harga:,}, Jumlah: {self.jumlah}, Kategori: {self.kategori}"

if 'data_barang' not in st.session_state:
    st.session_state.data_barang = []

def hitung_total():
    total = sum(b.harga * b.jumlah for b in st.session_state.data_barang)
    return f"Rp{total:,}"

st.markdown('<div class="judul-app">🛒 Aplikasi Daftar Belanja Sederhana</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
        <div class="menu-box">
        <h4>📋 Menu:</h4>
        <ol>
        <li>📄 Lihat Daftar Barang</li>
        <li>➕ Tambah Barang</li>
        <li>✔️ Tandai Barang Sudah Dibeli</li>
        <li>✏️ Edit Barang</li>
        <li>🗑️ Hapus Barang</li>
        </ol>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="metric-box">
            💰 <strong>Total Harga:</strong><br>{hitung_total()}
        </div>
    """, unsafe_allow_html=True)

menu = st.text_input("Masukkan angka menu (1-5):")


