from datetime import datetime

transaksi = []
anggaran = {}

def format_rupiah(nominal):
    # Mengubah angka menjadi format Rupiah dengan pemisah ribuan titik
    return f"Rp{int(nominal):,}".replace(",", ".")

def tambah_pemasukan():
    tanggal = input("Tanggal (dd-mm-yyyy): ")
    waktu = input("Waktu (HH:MM): ")
    nominal = float(input("Nominal: "))
    kategori = input("Kategori: ")
    keterangan = input("Keterangan: ")

    transaksi.append({
        "tanggal": tanggal,
        "waktu": waktu,
        "jenis": "Pemasukan",
        "kategori": kategori,
        "jumlah": nominal,
        "keterangan": keterangan
    })

    print("Pemasukan berhasil ditambahkan!")

def tambah_pengeluaran():
    tanggal = input("Tanggal (dd-mm-yyyy): ")
    waktu = input("Waktu (HH:MM): ")
    nominal = float(input("Nominal: "))
    kategori = input("Kategori: ")
    keterangan = input("Keterangan: ")

    transaksi.append({
        "tanggal": tanggal,
        "waktu": waktu,
        "jenis": "Pengeluaran",
        "kategori": kategori,
        "jumlah": nominal,
        "keterangan": keterangan
    })

    print("Pengeluaran berhasil ditambahkan!")

def lihat_saldo():
    pemasukan = 0
    pengeluaran = 0

    for data in transaksi:
        if data["jenis"] == "Pemasukan":
            pemasukan += data["jumlah"]
        else:
            pengeluaran += data["jumlah"]

    saldo = pemasukan - pengeluaran

    print("\n=== SALDO ===")
    print(f"Total Pemasukan   : {format_rupiah(pemasukan)}")
    print(f"Total Pengeluaran : {format_rupiah(pengeluaran)}")
    print(f"Saldo             : {format_rupiah(saldo)}")

def rekap_bulanan():
    # Mengambil bulan dan tahun saat ini jika ingin dinamis, 
    # atau Anda bisa menyesuaikan inputannya. 
    # Di sini kita buat statis sesuai contoh gambar terlebih dahulu.
    print("\n===== RINGKASAN JUNI 2025 =====")

    pemasukan = 0
    pengeluaran = 0
    kategori_total = {}

    for data in transaksi:
        if data["jenis"] == "Pemasukan":
            pemasukan += data["jumlah"]
        else:
            pengeluaran += data["jumlah"]
            kategori = data["kategori"]

            if kategori in kategori_total:
                kategori_total[kategori] += data["jumlah"]
            else:
                kategori_total[kategori] = data["jumlah"]

    saldo_akhir = pemasukan - pengeluaran

    # Format output seperti pada gambar
    print(f"{'Total Pemasukan':<17} : {format_rupiah(pemasukan)}")
    print(f"{'Total Pengeluaran':<17} : {format_rupiah(pengeluaran)}")
    print(f"{'Saldo Akhir':<17} : {format_rupiah(saldo_akhir)}")

    print("\nPengeluaran per Kategori:")
    for kategori, total in kategori_total.items():
        # Menyesuaikan spasi agar titik dua (:) sejajar
        print(f"- {' '.join(word.capitalize() for word in kategori.split()):<9} : {format_rupiah(total)}")

def grafik_ascii():
    kategori_total = {}

    for data in transaksi:
        if data["jenis"] == "Pengeluaran":
            kategori = data["kategori"]

            if kategori in kategori_total:
                kategori_total[kategori] += data["jumlah"]
            else:
                kategori_total[kategori] = data["jumlah"]

    print("\n=== GRAFIK ASCII ===")

    for kategori, total in kategori_total.items():
        batang = "#" * int(total / 100000) # Disesuaikan skalanya agar tidak terlalu panjang
        print(f"{kategori:15} {batang}")

def rekomendasi():
    pemasukan = 0
    hiburan = 0

    for data in transaksi:
        if data["jenis"] == "Pemasukan":
            pemasukan += data["jumlah"]

        if data["jenis"] == "Pengeluaran" and data["kategori"].lower() == "hiburan":
            hiburan += data["jumlah"]

    if pemasukan > 0:
        persen = (hiburan / pemasukan) * 100

        print(f"Hiburan = {persen:.2f}% dari pemasukan")

        if persen > 20:
            print("Saran: Kurangi pengeluaran hiburan.")
        else:
            print("Pengeluaran hiburan masih aman.")
    else:
        print("Belum ada data pemasukan.")

def cari_transaksi():
    kata = input("Masukkan kategori atau tanggal: ").lower()

    print("\n=== HASIL PENCARIAN ===")

    ditemukan = False

    for data in transaksi:
        if kata in data["kategori"].lower() or kata in data["tanggal"]:
            print(
                f"{data['tanggal']} {data['waktu']} | "
                f"{data['jenis']} | "
                f"{data['kategori']} | "
                f"{format_rupiah(data['jumlah'])}"
            )
            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.")

while True:
    print("\n===== MENU =====")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Saldo")
    print("4. Rekap Bulanan")
    print("5. Grafik ASCII")
    print("6. Rekomendasi")
    print("7. Cari Transaksi")
    print("8. Keluar")

    pilih = input("Pilih Menu: ")

    if pilih == "1":
        tambah_pemasukan()

    elif pilih == "2":
        tambah_pengeluaran()

    elif pilih == "3":
        lihat_saldo()

    elif pilih == "4":
        rekap_bulanan()

    elif pilih == "5":
        grafik_ascii()

    elif pilih == "6":
        rekomendasi()

    elif pilih == "7":
        cari_transaksi()

    elif pilih == "8":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
