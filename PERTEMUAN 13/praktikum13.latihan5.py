# Nama : [Isi Nama Anda]
# NIM : [Isi NIM Anda]
# Kelas : [Isi Kelas Anda]
# Praktikum 13 Graph III: Spanning Tree

# Kasus Pilihan: Kasus 2 - Jaringan Komputer [cite: 1086]
# Menggunakan Algoritma Prim untuk menghubungkan router secara bertahap.

import heapq

graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
} [cite: 1087, 1092]

def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst_hasil, total_hasil = prim(graph, 'RouterA')

print("MST Jaringan Komputer:")
for u, v, weight in mst_hasil:
    print(f"{u} terhubung ke {v} dengan bobot {weight}")
print("Total bobot minimum =", total_hasil)

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Kasus 2 (Jaringan Komputer)[cite: 1086].
# 2. Algoritma yang digunakan adalah Prim[cite: 1095].
# 3. Edge yang dipilih: RouterA-RouterC (2), RouterC-RouterD (1), RouterA-RouterB (3).
# 4. Total bobot MST adalah 6.
# 5. Edge RouterB-RouterC (4) dan RouterB-RouterD (5) tidak dipilih karena bobotnya lebih besar dan node-node tersebut sudah terhubung melalui jalur yang lebih efisien[cite: 663, 695].