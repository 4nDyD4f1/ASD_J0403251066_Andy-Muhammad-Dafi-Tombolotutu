# Nama  : Andy Muhammad Dafi T
# NIM   : J0403251066
# Kelas : Teknologi Rekayasa Perangkat Lunak

import heapq

# 1. Representasi graph berbobot
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]: continue
        
        for neighbor, weight in graph[curr_node].items():
            path = curr_dist + weight
            if path < distances[neighbor]:
                distances[neighbor] = path
                heapq.heappush(pq, (path, neighbor))
    return distances

# 3 & 4. Penentuan node awal dan Output
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

# Jawaban Analisis:
# 1. Node awal adalah Bogor.
# 2. Node Bogor (jarak 0). Selain node awal, yang terkecil adalah Depok (jarak 2).
# 3. Node Bandung (jarak 8).
# 4. Algoritma mencari tetangga terdekat Bogor (Depok), lalu mengeksplorasi jalur dari Depok ke Jakarta (2+2=4), yang lebih murah daripada jalur langsung Bogor-Jakarta (5).