# Nama  : Andy Muhammad Dafi T
# NIM   : J0403251066
# Kelas : Teknologi Rekayasa Perangkat Lunak
# Praktikum 12 Graph II: Shortest Path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A->B->D =", jalur_1)
print("Jalur 2: A->C->D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A->B->D")
else:
    print("Jalur terpendek adalah A->C->D")

# Jawaban Analisis:
# 1. Total bobot jalur A->B->D adalah 9 (4 + 5).
# 2. Total bobot jalur A->C->D adalah 3 (2 + 1).
# 3. Jalur yang dipilih adalah A->C->D.
# 4. Karena yang dihitung adalah akumulasi bobot (biaya), bukan jumlah langkah (edge).