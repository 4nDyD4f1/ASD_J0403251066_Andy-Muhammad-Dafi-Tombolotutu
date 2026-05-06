# Nama  : Andy Muhammad Dafi T
# NIM   : J0403251066
# Kelas : Teknologi Rekayasa Perangkat Lunak

import heapq

graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi paling dekat adalah Kantin (2 menit).
# 2. Jarak ke Aula adalah 7 menit (Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1).
# 3. Tidak. Jalur langsung Gerbang-Kantin-Aula adalah 9 menit, sedangkan melalui Lab hanya 7 menit.
# 4. Karena waktu tempuh tidak mungkin negatif, sehingga Dijkstra paling efisien.