#=========================================================
#Nama   : Andy Muhammad Dafi Tombolotutu
#NIM    : J0403251066
#Kelas  : Teknologi Rekayasa Perangkat Lunak
#=========================================================

#=========================================================
#Materi Rekursif : Faktorial
# recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
#=========================================================

def faktorial(n):
    #1) Base case
    if n == 0:
        return 1

    #2) Recursive case
    return n * faktorial(n-1)

print("=====Program Faktorial=====")
print("Hasil Faktorial :", faktorial(3))