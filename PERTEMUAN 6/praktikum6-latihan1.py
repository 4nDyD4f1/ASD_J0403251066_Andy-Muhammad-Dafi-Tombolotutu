def insertion_sort(data):
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

'''
Soal:
1. Mengapa Perulangan dimulai dari index 1?
Karena pada index 0 dianggap sudah terurut, sehingga perulangan dimulai dari index 1 untuk membandingkan elemen selanjutnya dengan elemen sebelumnya.

2. Apa fungsi variable key?
Variable key digunakan untuk menyimpan nilai elemen yang sedang diproses dalam perulangan. Nilai key akan dibandingkan dengan elemen-elemen sebelumnya untuk menentukan posisi yang tepat dalam urutan yang sudah terurut.

3. Mengapa digunakan while, bukan for?
While digunakan karena jumlah iterasi yang diperlukan untuk membandingkan key dengan elemen-elemen sebelumnya tidak diketahui secara pasti. For biasanya digunakan ketika jumlah iterasi sudah diketahui, sedangkan while lebih fleksibel untuk kondisi yang tidak pasti.

4. Operasi apa yang terjadi di dalam while?
Di dalam while, terjadi pergeseran elemen-elemen yang lebih besar dari key ke posisi yang lebih tinggi (data[j + 1] = data[j]). Proses ini terus berlanjut hingga ditemukan posisi yang tepat untuk key, yaitu ketika key tidak lagi lebih kecil dari elemen sebelumnya atau ketika j sudah mencapai batas awal (j < 0). Setelah itu, key ditempatkan pada posisi yang sesuai (data[j + 1] = key).

'''