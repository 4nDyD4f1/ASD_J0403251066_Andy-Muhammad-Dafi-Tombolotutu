def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge_sort(left_sorted, right_sorted)

'''
Soal
1. Apa yang dimaksud dengan base case?
Base case adalah kondisi di mana fungsi rekursif berhenti memanggil dirinya sendiri. Dalam konteks merge sort, base case terjadi ketika panjang data yang akan diurutkan kurang dari atau sama dengan 1, karena data dengan satu elemen atau kosong sudah dianggap terurut.

2. Mengapa fungsi memanggil dirinya sendiri?
Fungsi memanggil dirinya sendiri untuk membagi data menjadi bagian yang lebih kecil hingga mencapai base case. Proses ini memungkinkan algoritma untuk mengurutkan bagian-bagian kecil dari data sebelum menggabungkannya kembali menjadi satu kesatuan yang terurut.

3. Apa tujuan fungsi merge?
Tujuan fungsi merge adalah untuk menggabungkan dua bagian data yang sudah terurut (left_sorted dan right_sorted) menjadi satu kesatuan yang terurut. Fungsi ini membandingkan elemen-elemen dari kedua bagian dan menyusunnya dalam urutan yang benar, sehingga menghasilkan data yang sudah terurut secara keseluruhan.
'''