# Nama : [Isi Nama Anda]
# NIM : [Isi NIM Anda]
# Kelas : [Isi Kelas Anda]
# Praktikum 13 Graph III: Spanning Tree

# Studi Kasus: Jaringan Kabel Antar Gedung [cite: 1044]
# Menggunakan Algoritma Kruskal untuk efisiensi pemilihan biaya minimum secara global.

edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
] [cite: 1048, 1053]

edges.sort()
mst = []
total_biaya = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_biaya += weight
        connected.add(u)
        connected.add(v)

print("Jaringan Kabel Minimum:")
for u, v, cost in mst:
    print(f"{u} - {v}: Biaya {cost}")
print("Total biaya minimum =", total_biaya)

# Jawaban Analisis:
# 1. Algoritma Kruskal digunakan karena kasus ini melibatkan daftar biaya global[cite: 1064].
# 2. Edge yang dipilih: GedungC-GedungD (1), GedungA-GedungC (2), dan GedungB-GedungD (3).
# 3. Total biaya minimum adalah 6.
# 4. MST cocok karena tujuannya adalah menghubungkan semua titik (gedung) dengan total biaya/bobot paling rendah tanpa ada jalur mubazir (cycle)[cite: 663, 671].