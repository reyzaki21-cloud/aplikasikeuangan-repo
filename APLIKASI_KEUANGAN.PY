import csv

FILE = 'data_keuangan.csv'

def load_data():
    data = []
    try:
        with open(FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['jumlah'] = int(row['jumlah'])
                data.append(row)
    except FileNotFoundError:
        with open(FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['tanggal', 'jenis', 'jumlah', 'kategori', 'deskripsi'])
            writer.writeheader()
    return data

def save_data(data):
    with open(FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['tanggal', 'jenis', 'jumlah', 'kategori', 'deskripsi'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def tambah_transaksi(data):
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (pemasukan/pengeluaran): ")
    try:
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    kategori = input("Kategori: ")
    deskripsi = input("Deskripsi: ")
    transaksi = {
        'tanggal': tanggal,
        'jenis': jenis,
        'jumlah': jumlah,
        'kategori': kategori,
        'deskripsi': deskripsi
    }
    data.append(transaksi)
    save_data(data)
    print(" Transaksi berhasil ditambahkan.")

def tampilkan_semua(data):
    print("\n📄 Daftar Semua Transaksi:")
    print(f"{'No':<3} {'Tanggal':<12} {'Jenis':<12} {'Jumlah':<10} {'Kategori':<15} Deskripsi")
    for i, row in enumerate(data):
        print(f"{i:<3} {row['tanggal']:<12} {row['jenis']:<12} Rp{row['jumlah']:<10} {row['kategori']:<15} {row['deskripsi']}")

def update_transaksi(data):
    tampilkan_semua(data)
    try:
        idx = int(input("Masukkan nomor transaksi yang ingin diubah: "))
    except ValueError:
        print(" Input harus berupa angka.")
        return
    if 0 <= idx < len(data):
        print("Masukkan data baru:")
        data[idx]['tanggal'] = input("Tanggal (YYYY-MM-DD): ")
        data[idx]['jenis'] = input("Jenis (pemasukan/pengeluaran): ")
        try:
            data[idx]['jumlah'] = int(input("Jumlah: "))
        except ValueError:
            print(" Jumlah harus berupa angka.")
            return
        data[idx]['kategori'] = input("Kategori: ")
        data[idx]['deskripsi'] = input("Deskripsi: ")
        save_data(data)
        print(" Transaksi berhasil diupdate.")
    else:
        print(" Nomor transaksi tidak valid.")

def hapus_transaksi(data):
    tampilkan_semua(data)
    try:
        idx = int(input("Masukkan nomor transaksi yang ingin dihapus: "))
    except ValueError:
        print(" Input harus berupa angka.")
        return
    if 0 <= idx < len(data):
        del data[idx]
        save_data(data)
        print("Transaksi berhasil dihapus.")
    else:
        print("Nomor transaksi tidak valid.")

def menu():
    data = load_data()
    while True:
        print("\n=== Aplikasi Keuangan Pribadi ===")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Update Transaksi")
        print("4. Hapus Transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_transaksi(data)
        elif pilihan == '2':
            tampilkan_semua(data)
        elif pilihan == '3':
            update_transaksi(data)
        elif pilihan == '4':
            hapus_transaksi(data)
        elif pilihan == '0':
            print(" Keluar dari program!")
            break
        else:
            print(" Menu tidak valid.")

if _name_ == "_main_":
    menu()
