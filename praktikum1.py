#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#============================================

#membuka file dengan mode read ("r")

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah baris", isi_file.count("\n")+1)

#membuka file per baris
print("===Membaca File per Baris===")
jumlah_baris=0
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)



#====================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Parsing baris menjadi kolom data
#====================================================
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #mengambil data
        print("NIM:", nim, "| Nama:", nama, "| Nilai: ", nilai)




#====================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3: Membaca file dan menyimpan file ke list
#====================================================

data_list= [] #List untuk menampung data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        # Simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim,nama,int(nilai)])

    print("========================= Data Mahasiswa dalam list =========================")
    print(data_list)

    print("========================= Jumlah Record dalam List =========================")
    print("Jumlah record", len(data_list))

    print("========================= Menampilkan data record tertentu =========================")
    print("Contoh record pertama: ", data_list[0])


#====================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4: Membaca file dan menyimpan file ke dictionary
#====================================================

data_dict = {}
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #Simpan data mahsiswa ke dictionary dengan key NIM
        data_dict[nim] = {          #key
        "nama": nama,               #values
        "nilai": int(nilai)         #values
        }
    print("====Data Mahasiswa dalam Dictionary===")
    print(data_dict)

data_dict = {}
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split (",")
        