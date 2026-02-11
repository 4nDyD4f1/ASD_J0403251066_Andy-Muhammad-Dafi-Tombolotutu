import os

# Nama file database
FILE_NAME = "stok_barang.txt"

def baca_data():
    """Membaca data dari file ke dalam dictionary."""
    stok_dict = {}
    # Cek apakah file ada, jika tidak, buat file kosong
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass
        return stok_dict

    with open(FILE_NAME, "r") as f:
        for line in f:
            # Membersihkan whitespace dan memisahkan data berdasarkan koma
            data = line.strip().split(",")
            if len(data) == 3:
                kode, nama, stok = data
                stok_dict[kode] = {"nama": nama, "stok": int(stok)}
    return stok_dict

def simpan_data(stok_dict):
    """Menyimpan data dari dictionary kembali ke file .txt."""
    with open(FILE_NAME, "w") as f:
        for kode, info in stok_dict.items():
            f.write(f"{kode},{info['nama']},{info['stok']}\n")
    print("--- Data berhasil disimpan ke file! ---")

def tampilkan_barang(stok_dict):
    """Menu 1: Menampilkan semua barang."""
    if not stok_dict:
        print("Stok barang kosong.")
    else:
        print("\n--- DAFTAR STOK BARANG ---")
        print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok'}")
        print("-" * 35)
        for kode, info in stok_dict.items():
            print(f"{kode:<10} | {info['nama']:<15} | {info['stok']}")

def cari_barang(stok_dict):
    """Menu 2: Mencari barang berdasarkan kode."""
    kode = input("Masukkan kode barang yang dicari: ")
    if kode in stok_dict:
        info = stok_dict[kode]
        print(f"Ditemukan: {info['nama']} | Stok: {info['stok']}")
    else:
        print("Barang tidak ditemukan.")

def tambah_barang(stok_dict):
    """Menu 3: Menambah barang baru."""
    kode = input("Masukkan kode barang baru: ")
    if kode in stok_dict:
        print("Kode sudah digunakan.")
    else:
        nama = input("Masukkan nama barang: ")
        try:
            stok = int(input("Masukkan stok awal: "))
            stok_dict[kode] = {"nama": nama, "stok": stok}
            print("Barang berhasil ditambahkan!")
        except ValueError:
            print("Input stok harus berupa angka.")

def update_stok(stok_dict):
    """Menu 4: Update stok barang (tambah/kurang)."""
    kode = input("Masukkan kode barang yang akan diupdate: ")
    if kode in stok_dict:
        print(f"Barang: {stok_dict[kode]['nama']} (Stok saat ini: {stok_dict[kode]['stok']})")
        print("1. Tambah Stok")
        print("2. Kurangi Stok")
        pilihan = input("Pilih aksi (1/2): ")
        
        try:
            jumlah = int(input("Masukkan jumlah: "))
            if pilihan == "1":
                stok_dict[kode]['stok'] += jumlah
                print("Stok berhasil ditambah.")
            elif pilihan == "2":
                if stok_dict[kode]['stok'] - jumlah < 0:
                    print("Gagal! Stok tidak boleh negatif.")
                else:
                    stok_dict[kode]['stok'] -= jumlah
                    print("Stok berhasil dikurangi.")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")
    else:
        print("Barang tidak ditemukan.")

def main():
    """Fungsi utama untuk menjalankan loop program."""
    # Load data di awal program
    data_stok = baca_data()

    while True:
        print("\n=== SISTEM STOK KANTIN ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok")
        print("5. Simpan ke File")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_barang(data_stok)
        elif pilihan == "2":
            cari_barang(data_stok)
        elif pilihan == "3":
            tambah_barang(data_stok)
        elif pilihan == "4":
            update_stok(data_stok)
        elif pilihan == "5":
            simpan_data(data_stok)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Menu tidak tersedia, silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()