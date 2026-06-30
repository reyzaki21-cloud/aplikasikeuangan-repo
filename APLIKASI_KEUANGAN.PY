from datetime import datetime

transaksi = []
anggaran = {}

def format_rupiah(nominal):
    # Mengubah angka menjadi format Rupiah dengan pemisah ribuan titik
    return f"Rp{int(nominal):,}".replace(",", ".")

def atur_anggaran():
    print("\n=== ATUR ANGGARAN KATEGORI ===")
    kategori = input("Masukkan nama kategori pengeluaran: ").strip().lower()
    nominal = float(input(f"Masukkan batas anggaran untuk kategori '{kategori}': "))
    
    anggaran[kategori] = nominal
    print(f"Anggaran untuk kategori '{kategori.capitalize()}' berhasil diatur sebesar {format_rupiah(nominal)}!")

def cek_anggaran():
    print("\n===== STATUS ANGGARAN =====")
    
    if not anggaran:
        print("Belum ada anggaran yang diatur.")
        return

    pengeluaran_per_kategori = {}
    for data in transaksi:
        if data["jenis"] == "Pengeluaran":
            kat = data["kategori"].lower()
            pengeluaran_per_kategori[kat] = pengeluaran_per_kategori.get(kat, 0) + data["jumlah"]

    for kategori, batas_anggaran in anggaran.items():
        terpakai = pengeluaran_per_kategori.get(kategori, 0)
        
        print(f"\nKategori : {kategori.capitalize()}")
        print(f"Anggaran : {format_rupiah(batas_anggaran)}")
        print(f"Terpakai : {format_rupiah(terpakai)}")
        
        if terpakai > batas_anggaran:
            print("⚠ PERINGATAN! Anggaran telah terlampaui.")
        elif terpakai >= (batas_anggaran * 0.8):
            print("⚠ Hati-hati! Pengeluaran sudah mencapai 80% dari anggaran.")

def rekomendasi_penghematan():
    print("\n===== REKOMENDASI PENGHEMATAN =====")
    
    if not anggaran:
        print("Belum ada data anggaran. Atur anggaran terlebih dahulu di Menu 3.")
        return

    pengeluaran_per_kategori = {}
    for data in transaksi:
        if data["jenis"] == "Pengeluaran":
            kat = data["kategori"].lower()
            pengeluaran_per_kategori[kat] = pengeluaran_per_kategori.get(kat, 0) + data["jumlah"]

    ada_rekomendasi = False

    for kategori, batas_anggaran in anggaran.items():
        terpakai = pengeluaran_per_kategori.get(kategori, 0)
        persentase = (terpakai / batas_anggaran) * 100 if batas_anggaran > 0 else 0

        if persentase > 100:
            sisa_over = terpakai - batas_anggaran
            print(f"💡 [Kritis] Kategori '{kategori.capitalize()}' bocor {format_rupiah(sisa_over)}!")
            print(f"   -> Tindakan: HENTIKAN pengeluaran untuk kategori ini segera atau alihkan sisa dana dari kategori lain.")
            ada_rekomendasi = True
        elif persentase >= 80:
            print(f"💡 [Waspada] Kategori '{kategori.capitalize()}' sudah terpakai {persentase:.1f}%.")
            print(f"   -> Tindakan: Batasi transaksi harian untuk kategori ini hingga akhir bulan agar tidak overbudget.")
            ada_rekomendasi = True
        elif persentase >= 50:
            print(f"💡 [Info] Kategori '{kategori.capitalize()}' sudah berjalan setengah dari batas budget.")
            print(f"   -> Tindakan: Pertahankan ritme belanja kamu saat ini. Jangan melakukan pembelian besar non-esensial.")
            ada_rekomendasi = True

    if not ada_rekomendasi:
        print("✅ Pengeluaran kamu di semua kategori masih sangat aman dan terkontrol. Bagus, pertahankan!")

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
            kategori_total[kategori] = kategori_total.get(kategori, 0) + data["jumlah"]

    saldo_akhir = pemasukan - pengeluaran
    print(f"{'Total Pemasukan':<17} : {format_rupiah(pemasukan)}")
    print(f"{'Total Pengeluaran':<17} : {format_rupiah(pengeluaran)}")
    print(f"{'Saldo Akhir':<17} : {format_rupiah(saldo_akhir)}")

    print("\nPengeluaran per Kategori:")
    for kategori, total in kategori_total.items():
        print(f"- {' '.join(word.capitalize() for word in kategori.split()):<9} : {format_rupiah(total)}")

def grafik_ascii():
    kategori_total = {}
    for data in transaksi:
        if data["jenis"] == "Pengeluaran":
            kategori = data["kategori"]
            kategori_total[kategori] = kategori_total.get(kategori, 0) + data["jumlah"]

    print("\n===== GRAFIK PENGELUARAN =====")
    if not kategori_total:
        print("Belum ada data pengeluaran.")
        return

    maksimum = max(kategori_total.values())
    for kategori, jumlah in kategori_total.items():
        panjang = int((jumlah / maksimum) * 30) if maksimum > 0 else 0
        batang = "█" * panjang
        print(f"{kategori:<15} | {batang} {format_rupiah(jumlah)}")

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
            print(f"{data['tanggal']} {data['waktu']} | {data['jenis']} | {data['kategori']} | {format_rupiah(data['jumlah'])}")
            ditemukan = True
    if not ditemukan:
        print("Data tidak ditemukan.")

while True:
    print("\n===== MENU =====")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Atur Anggaran Kategori")
    print("4. Lihat Saldo")
    print("5. Rekap Bulanan")
    print("6. Grafik ASCII")
    print("7. Rekomendasi Persentase")
    print("8. Cari Transaksi")
    print("9. Cek Anggaran")
    print("10. Rekomendasi Penghematan")
    print("11. Keluar")

    pilih = input("Pilih Menu: ")

    if pilih == "1":
        tambah_pemasukan()
    elif pilih == "2":
        tambah_pengeluaran()
    elif pilih == "3":
        atur_anggaran()
    elif pilih == "4":
        lihat_saldo()
    elif pilih == "5":
        rekap_bulanan()
    elif pilih == "6":
        grafik_ascii()
    elif pilih == "7":
        rekomendasi()
    elif pilih == "8":
        cari_transaksi()
    elif pilih == "9":
        cek_anggaran()
    elif pilih == "10":
        rekomendasi_penghematan()
    elif pilih == "11":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
