#=========================================================
#Nama   : Andy Muhammad Dafi Tombolotutu
#NIM    : J0403251066
#Kelas  : Teknologi Rekayasa Perangkat Lunak
#=========================================================

#=========================================================
#Studi Kasus : Sistem Antrian Layanan Akademik
#Implementasi Queue =>
# Stack ==> Front -> C -> B -> A -> None
# Enqueue : Memindahkan pointer rear (belakang)
# Dequeue : Memindahkan pointer front (depan)
# Front -> A -> Rear
#=========================================================

#1) Mendefinisikan class Node
class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.next = None

#2) Mendefinisikan queue, terdiri dari front dan rear
class QueueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self,nim,nama):
        #1) Membuat node baru
        nodeBaru = Node(nim, nama)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #2) Jika queue tidak kosong, rear lama menunjuk ke node baru, lalu rear pindah ke node baru
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    def dequeue(self):
        #1) Lihat data yang paling depan (front)
        if self.is_empty():
            print("Queue kosong, tidak dapat melakukan dequeue.")
            return None
        node_dilayani = self.front

        #2) Geser front ke node berikutnya
        self.front = self.front.next

        #3) Jika setelah menggeser front menjadi None, maka rear juga harus diatur ke None
        if self.front is None:
            self.rear = None

        node_dilayani.next = None
        return node_dilayani
    
    def tampilkan(self):
        print("Daftar Antrian Layanan Akademik (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1
        print("None - Rear di node terakhir")
    
# Program Utama

def main():
    # instansiasi queue
    q = QueueAkademik()

    while True:
        print("=== Sistem Antrian Layanan Akademik ===")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nim = input("Masukkan NIM Mahasiswa: ")
            nama = input("Masukkan Nama Mahasiswa: ")
            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian.")

        elif pilihan == "2":
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani is not None:
                print(f"Mahasiswa dengan NIM {mahasiswa_dilayani.nim} - {mahasiswa_dilayani.nama} sedang dilayani.")
            else:
                print("Tidak ada mahasiswa dalam antrian.")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem antrian layanan akademik.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")


if __name__ == "__main__":
    main()