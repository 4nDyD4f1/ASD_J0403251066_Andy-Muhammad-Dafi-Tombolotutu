#=========================================================================
#Nama : Andy Muhammad Dafi Tombolotutu
#NIM : J0403251066
#Kelas : TPL B2
#=========================================================================


"""
Materi rekursif : menjumlahkan elemen list
"""

def jumlah_list(data, index=0):
    if index == len(data):
        return 0
    # recursive case
    return data[index] + jumlah_list(data, index=0)

print("========== Program Jumlah Data List ============")
print(jumlah_list([1,2,3]))
