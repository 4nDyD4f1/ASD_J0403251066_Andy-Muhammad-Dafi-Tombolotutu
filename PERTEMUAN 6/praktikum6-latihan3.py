'''
Soal
1. Tuliskan isi list setelah iterasi i = 1
[2, 5, 4, 6, 1, 3]

2. Tuliskan isi list setelah iterasi i = 2
[2, 4, 5, 6, 1, 3]

3. Berapa kali pergesera terjadi pada iterasi i = 4
Pada iterasi i = 4, terjadi 3 kali pergeseran

'''

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

print("Hasil Sorting:", insertion_sort([5,2,4,6,1,3]))