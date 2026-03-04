def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

'''
Soal
1. Lengkapi kondisi agar menjadi ascending
    left[i] < right[j]:

2. Jelaskan fungsi result.extend()
Fungsi result.extend() digunakan untuk menambahkan elemen-elemen dari list left[i:] dan right[j:] ke dalam list result. Ini memastikan bahwa semua elemen yang tersisa dari kedua list akan dimasukkan ke dalam hasil akhir setelah proses penggabungan selesai.

'''
