#========================================================
#Insertion Sort dengan tracing
#========================================================

def insertion_sort(data):
    print("Data awal:", data)
    print("=" * 50)

    for i in range(1, len(data)):

        key = data[i]
        j = i - 1

        print(f"Iterasi: {i}")
        print(f"Key: {key}")
        print(f"Bagian kiri(terurut) {data[:i]}")
        print(f"Bagian kanan(terurut) {data[i:]}")

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print("Setelah disisipkan:", data)
        print("-" * 50)
    return data
        

angka = [7,8,5,2,4,6]
print("Hasil Sorting:", insertion_sort(angka))