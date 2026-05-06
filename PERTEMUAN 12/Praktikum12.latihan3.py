# Nama  : Andy Muhammad Dafi T
# NIM   : J0403251066
# Kelas : Teknologi Rekayasa Perangkat Lunak

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Bobot langsung A ke B adalah 5.
# 2. Total bobot A->C->B adalah 2 (4 + (-2)).
# 3. Jalur A->C->B menghasilkan jarak lebih kecil.
# 4. Karena Bellman-Ford memeriksa semua kemungkinan edge berulang kali tanpa asumsi greedy.
# 5. Relaksasi adalah proses memperbarui estimasi jarak terpendek ke sebuah node jika ditemukan jalur yang lebih murah.
# 6. Dijkstra lebih cepat tapi tidak bisa bobot negatif; Bellman-Ford lebih lambat tapi bisa menangani bobot negatif.