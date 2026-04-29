graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': []
}

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 

visited = set()

print("DFS dari A:") 
dfs(graph, 'A', visited) 

# Pertanyaan Analisis:
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
# 2. Apa yang terjadi jika urutan neighbor diubah?  
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.

# Jawaban:
# 1. DFS masuk ke node terdalam karena menggunakan sistem rekursi/stack, 
#    di mana setiap ada tetangga baru, ia langsung mengeksplorasi cabang tersebut 
#    sebelum menyelesaikan tetangga di level yang sama.
# 2. Jika urutan neighbor diubah, urutan kunjungan juga akan berubah karena 
#    DFS memproses tetangga berdasarkan urutan indeks di dalam list.
# 3. Perbandingannya: BFS akan mengunjungi node secara melebar (per level), 
#    sedangkan DFS akan mengunjungi node secara mendalam (per jalur/cabang). 
#    Urutan BFS untuk graph ini adalah A, B, C, D, E, F.
