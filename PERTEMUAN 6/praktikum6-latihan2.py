def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and key < data[j]: #question 1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key #question 1

    return data
angka = [7,8,5,2,4,6]
print("Hasil Sorting:", insertion_sort(angka))



'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending
    *Sudah saya lengkapi

2. Ubah agar menjadi descending
while j >= 0 and key > data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

dibagian baris ke 6 diubah dari "<" menjadi ">" untuk sorting descending

'''