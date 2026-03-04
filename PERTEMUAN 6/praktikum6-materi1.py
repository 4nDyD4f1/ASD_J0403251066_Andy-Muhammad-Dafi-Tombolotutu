#========================================================
#Insertion Sort (Ascending)
#========================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        #Loop untuk membandingkan key dengan elemen sebelumnya
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting:", insertion_sort(angka))
hasil = insertion_sort(angka)