#========================================================
#Identitas Mahasiswa
#========================================================

#========================================================
#Merge Sort (Ascending)
#========================================================


def insertion_sort(data):
    # Melihat data awal
    print(f"Data awal: {data}")
    print("=" * 50)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"iterasi ke-{i}")
        print(f"Nilai key = {key}")
        print(f"Bagian Kiri (terurut) : {data[:i]}")
        print(f"Bagian Kanan (belum terurut) : {data[i:]}")

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

        print(f"Setelah disisipkan : {data}")
        print("-" * 50)
    return data

print("Hasil Sorting:", insertion_sort([7,8,5,2,4,6]))