import streamlit as st
import pandas as pd
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Rubik By Kuze", layout="wide")

# 1. Tampilkan Banner Canva
if os.path.exists("Rubik By Kuze.PNG"):
    st.image("Rubik By Kuze.PNG", use_container_width=True)

st.title("Rubik By Kuze")
st.divider()

try:
    if os.path.exists("data_rubik1.csv"):
        df = pd.read_csv("data_rubik1.csv")
        
        # Membersihkan data dari nilai kosong di kolom penting
        df = df.dropna(subset=['foto', 'kategori', 'nama'])

        daftar_kategori = df['kategori'].unique()

        for kat in daftar_kategori:
            st.header(f"Rubik Jenis {str(kat).capitalize()}")
            data_per_kat = df[df['kategori'] == kat]

            # Membuat grid 4 kolom
            cols = st.columns(4)

            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row['foto']).strip()
                
                # Menggunakan modul % 4 agar produk terbagi rata di 4 kolom
                with cols[index % 4]:
                    if os.path.exists(nama_foto):
                        st.image(nama_foto, use_container_width=True)
                    else:
                        # Tampilkan placeholder jika foto fisik tidak ada
                        st.warning(f"Foto tidak ditemukan: {nama_foto}")
                    
                    st.subheader(row['nama'])

                    # --- HARGA & STATUS DENGAN FONT LEBIH BESAR ---
                    try:
                        harga_formatted = f"{int(row['harga']):,}".replace(",", ".")
                        st.markdown(f"### **Rp {harga_formatted}**")
                    except:
                        st.markdown(f"### **Rp {row['harga']}**")
                        
                    st.markdown(f"**Status:** {row['status']}")
            st.divider()

    else:
        st.error("File 'Data_Rubik1.csv' tidak ditemukan!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

# --- BAGIAN KONTAK & ALAMAT (FOOTER) ---
st.write("") 
st.write("")

st.subheader("📞 Hubungi Kami")
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    **Alamat Galeri:** Jl Sidokabul No.4c Sorosutan Umbulharjo Yogyakarta
    """)

with col_info2:
    # Format nomor HP WA wajib menggunakan kode negara (misal: 62)
    no_hp = "6289531588666"
    pesan_wa = "Halo Mas, saya tertarik memesan rubik di katalog Anda."
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"

    st.markdown("**WhatsApp:**")
    st.link_button("Pesan Sekarang via WhatsApp", link_wa)
    
st.caption("© 2026 Rubik By Kuze - Semua Hak Dilindungi")
