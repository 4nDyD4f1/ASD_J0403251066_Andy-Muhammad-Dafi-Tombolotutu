# Nama : [Isi Nama Anda]
# NIM : [Isi NIM Anda]
# Kelas : [Isi Kelas Anda]
# Praktikum 13 Graph III: Spanning Tree

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
} [cite: 981]

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

mst, total = prim(graph, 'A')
print("Minimum Spanning Tree (Latihan 3):")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah 'A'[cite: 1032].
# 2. Edge A-C (bobot 2) dipilih pertama kali karena merupakan edge terkecil yang terhubung ke node awal A[cite: 789, 791].
# 3. Prim menentukan edge berikutnya dengan membandingkan semua edge yang menghubungkan node yang sudah dikunjungi ke node yang belum dikunjungi[cite: 767, 776].
# 4. Total bobot MST adalah 6[cite: 1036].
# 5. Prim membangun tree dari satu node (lokal), sedangkan Kruskal memilih edge global terkecil di seluruh graph[cite: 869, 872].