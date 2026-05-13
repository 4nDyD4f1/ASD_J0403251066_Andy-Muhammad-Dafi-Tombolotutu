# Nama : [Isi Nama Anda]
# NIM : [Isi NIM Anda]
# Kelas : [Isi Kelas Anda]
# Praktikum 13 Graph III: Spanning Tree

edges = [
    (1, 'C', 'D'), (2, 'A', 'C'), (3, 'B', 'D'),
    (4, 'A', 'B'), (5, 'A', 'D')
] [cite: 941]

edges.sort() # Mengurutkan berdasarkan bobot [cite: 952]
mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree (Latihan 2):")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge C-D dipilih pertama kali karena memiliki bobot terkecil (1)[cite: 720, 722].
# 2. Karena Kruskal bertujuan mencari total bobot minimum dengan memprioritaskan biaya terkecil secara global[cite: 693].
# 3. Total bobot MST yang dihasilkan adalah 6 (1 + 2 + 3)[cite: 731].
# 4. Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena semua node sudah terhubung, dan menambahkannya akan membentuk cycle[cite: 701, 725].