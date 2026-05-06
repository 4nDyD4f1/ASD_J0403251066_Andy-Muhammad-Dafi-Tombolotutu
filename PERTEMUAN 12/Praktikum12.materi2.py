def bellman_ford(graph, start):
    # Inisialisasi jarak awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Proses Relaksasi diulang sebanyak (V-1) kali
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Update jika jarak ke node + bobot edge lebih kecil dari jarak neighbor saat ini
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    return distances

# Contoh graph dengan bobot negatif
graph_negatif = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

hasil = bellman_ford(graph_negatif, 'A')
print("Hasil Bellman-Ford (Materi 2):", hasil)