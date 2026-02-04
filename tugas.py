jumlah_baris = 0
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
    jumlah_baris = baris = 1
    baris = baris.strip()
    print("Baris ke- ", jumlah_baris)