# Nama : [Isi Nama Anda]
# NIM : [Isi NIM Anda]
# Kelas : [Isi Kelas Anda]
# Praktikum 13 Graph III: Spanning Tree

# Daftar edge graph awal [cite: 903]
edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('C', 'D'), ('B', 'D')
]

# Contoh spanning tree yang valid (tanpa cycle) [cite: 910]
spanning_tree = [
    ('A', 'C'), ('C', 'D'), ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges)) [cite: 926]
print("Jumlah edge spanning tree =", len(spanning_tree)) [cite: 927]

# Jawaban Analisis:
# 1. Graph awal mengandung cycle dan memiliki jalur berlebih, sedangkan spanning tree menghubungkan semua node tanpa cycle[cite: 632, 647].
# 2. Cycle dihindari karena menyebabkan penggunaan edge berlebih dan meningkatkan biaya total tanpa menambah konektivitas[cite: 648, 649].
# 3. Karena jumlah edge spanning tree selalu (n-1), di mana n adalah jumlah node, untuk memastikan efisiensi koneksi[cite: 634, 641].