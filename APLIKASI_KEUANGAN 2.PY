import csv
import os
from datetime import datetime

# Nama file CSV
FILE_PEMASUKAN = "pemasukan.csv"
FILE_PENGELUARAN = "pengeluaran.csv"

# Kategori pengeluaran
kategori_pengeluaran = ["Makanan", "Transportasi", "Hiburan", "Tagihan", "Lainnya"]

# ==================== FUNGSI UTILITAS ====================

def simpan_csv(nama_file, data, header):
    """Simpan data ke file CSV."""
    with open(nama_file, mode="a", newline='') as file:
        writer = csv.writer(file)
        if os.stat(nama_file).st_size == 0:  # Kalau file kosong, tulis header
            writer.writerow(header)
        writer.writerow(data)

def baca_csv(nama_file):
    """Baca data dari file CSV dan kembalikan sebagai list of dict."""
    if not os.path.exists(nama_file):
        return []

    with open(nama_file, mode="r") as file:
        reader = csv.DictReader(file)
        return list(reader)

# ==================== FUNGSI FITUR ====================

def catat_pemasukan():
    try:
        jumlah = int(input("Masukkan jumlah pemasukan (Rp): "))
        keterangan = input("Keterangan: ")
        tanggal = datetime.now().date()
        simpan_csv(FILE_PEMASUKAN, [jumlah, tanggal, keterangan], ["jumlah", "tanggal", "keterangan"])
        print("✅ Pemasukan berhasil dicatat.")
    except ValueError:
        print("❌ Input jumlah harus berupa angka.")

def catat_pengeluaran():
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran (Rp): "))
        print(f"Kategori: {', '.join(kategori_pengeluaran)}")
        kategori = input("Kategori: ").capitalize()
        if kategori not in kategori_pengeluaran:
            kategori = "Lainnya"
        keterangan = input("Keterangan: ")
        tanggal = datetime.now().date()
        simpan_csv(FILE_PENGELUARAN, [jumlah, tanggal, kategori, keterangan], ["jumlah", "tanggal", "kategori", "keterangan"])
        print("✅ Pengeluaran berhasil dicatat.")
    except ValueError:
        print("❌ Input jumlah harus berupa angka.")

def laporan_bulanan():
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        tahun = int(input("Masukkan tahun: "))

        pemasukan = baca_csv(FILE_PEMASUKAN)
        pengeluaran = baca_csv(FILE_PENGELUARAN)

        total_masuk = sum(int(p["jumlah"]) for p in pemasukan
                          if datetime.strptime(p["tanggal"], "%Y-%m-%d").month == bulan and
                             datetime.strptime(p["tanggal"], "%Y-%m-%d").year == tahun)

        total_keluar = sum(int(e["jumlah"]) for e in pengeluaran
                           if datetime.strptime(e["tanggal"], "%Y-%m-%d").month == bulan and
                              datetime.strptime(e["tanggal"], "%Y-%m-%d").year == tahun)

        print(f"\n📆 Laporan Bulanan {bulan}/{tahun}")
        print(f"- Total Pemasukan  : Rp {total_masuk}")
        print(f"- Total Pengeluaran: Rp {total_keluar}")
        print(f"- Saldo            : Rp {total_masuk - total_keluar}")
    except ValueError:
        print("❌ Input tidak valid.")

def laporan_tahunan():
    try:
        tahun = int(input("Masukkan tahun: "))

        pemasukan = baca_csv(FILE_PEMASUKAN)
        pengeluaran = baca_csv(FILE_PENGELUARAN)

        total_masuk = sum(int(p["jumlah"]) for p in pemasukan
                          if datetime.strptime(p["tanggal"], "%Y-%m-%d").year == tahun)

        total_keluar = sum(int(e["jumlah"]) for e in pengeluaran
                           if datetime.strptime(e["tanggal"], "%Y-%m-%d").year == tahun)

        print(f"\n📅 Laporan Tahunan {tahun}")
        print(f"- Total Pemasukan  : Rp {total_masuk}")
        print(f"- Total Pengeluaran: Rp {total_keluar}")
        print(f"- Saldo            : Rp {total_masuk - total_keluar}")
    except ValueError:
        print("❌ Input tidak valid.")

def pengeluaran_per_kategori():
    data = baca_csv(FILE_PENGELUARAN)
    total_per_kategori = {}

    for item in data:
        kategori = item["kategori"]
        jumlah = int(item["jumlah"])
        total_per_kategori[kategori] = total_per_kategori.get(kategori, 0) + jumlah

    print("\n📂 Pengeluaran per Kategori:")
    for kategori, total in total_per_kategori.items():
        print(f"- {kategori}: Rp {total}")

# ==================== ANTARMUKA ====================

def menu():
    while True:
        print("\n=== Aplikasi Keuangan Pribadi (CSV) ===")
        print("1. Catat Pemasukan")
        print("2. Catat Pengeluaran")
        print("3. Laporan Bulanan")
        print("4. Laporan Tahunan")
        print("5. Lihat Pengeluaran per Kategori")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            catat_pemasukan()
        elif pilihan == "2":
            catat_pengeluaran()
        elif pilihan == "3":
            laporan_bulanan()
        elif pilihan == "4":
            laporan_tahunan()
        elif pilihan == "5":
            pengeluaran_per_kategori()
        elif pilihan == "0":
            print("👋 Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("❌ Menu tidak ditemukan.")

# ==================== JALANKAN ====================

if _name_ == "_main_":
    menu()
