def insertation_sort(data):
    for i in range(1, len(data)):

        key = data[i]

        j = i - 1

        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key

angka = [13,100, 7, 120, 25, 1, 90]
insertation_sort(angka)
print(angka)