#=========================================================
#Nama   : Andy Muhammad Dafi Tombolotutu
#NIM    : J0403251066
#Kelas  : Teknologi Rekayasa Perangkat Lunak
#=========================================================

#=========================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar) pada call stack
#input 3
# Masuk 1 - 2 - 3
# Keluar 3 - 2 - 1
#=========================================================

def hitung(n):
    print("Masuk:", n)
    if n == 0:
        print("Base case tercapai, berhenti.")
        return 1
    hasil = n * hitung(n-1)
    print("Keluar:", n)
    return hasil

print("=====Program Hitung=====")
hitung(3)