graph = { 
'Rumah': ['Sekolah', 'Toko'], 
'Sekolah': ['Perpustakaan'], 
'Toko': ['Pasar'], 
'Perpustakaan': [], 
'Pasar': [] 
}

from collections import deque

def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 
    
    visited.add(start) 

    while queue: 
        node = queue.popleft()
        print(node, end=" ") 

    for neighbor in graph[node]: 
        if neighbor not in visited: 
            visited.add(neighbor) 
            queue.append(neighbor) 

print("BFS dari Rumah:") 
bfs(graph, 'Rumah')

# Pertanyaan Analisis:
# 1. Node mana yang dikunjungi pertama?  
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?

# Jawaban:
# 1. Node yang dikunjungi pertama adalah Rumah. Dalam algoritma BFS (dan DFS), node awal yang ditentukan sebagai parameter start akan selalu menjadi titik pertama yang dimasukkan ke dalam antrean (queue) dan dicetak.
# 2. BFS cocok untuk mencari jalur terdekat karena algoritma ini mengeksplorasi semua tetangga dari node saat ini sebelum melanjutkan ke tingkat berikutnya. Dengan cara ini, BFS memastikan bahwa jalur yang ditemukan pertama kali adalah jalur terpendek dalam hal jumlah edge (atau langkah) dari node awal ke node tujuan.
# 3. Urutan dalam list: Dalam kode tersebut, graph['Rumah'] berisi ['Sekolah', 'Toko']. Jika urutannya ditukar menjadi ['Toko', 'Sekolah'], maka BFS akan mengunjungi 'Toko' terlebih dahulu sebelum 'Sekolah', karena BFS memproses elemen sesuai urutan antrean masuk.