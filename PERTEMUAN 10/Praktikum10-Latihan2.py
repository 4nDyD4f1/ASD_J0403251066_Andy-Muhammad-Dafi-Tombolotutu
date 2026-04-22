# ========================================================== 
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk BST 
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
    return root 
 
 
# Fungsi preorder untuk melihat bentuk tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L")
        # Fungsi sederhana untuk menampilkan struktur tree 
        tampil_struktur(root.right, level + 1, "R")

# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None 
# Data dimasukkan berurutan naik 
data_list = [10, 20, 30] 
for data in data_list: 
    root = insert(root, data) 

print("Preorder BST:") 
preorder(root) 

print("\n\nStruktur BST:") 
tampil_struktur(root)

#Penjelasan:
# 1. Kode ini mendemonstrasikan pembentukan Skewed Tree (Pohon Miring), yaitu kondisi khusus di mana BST tidak bercabang secara merata.
# 2. Fenomena ini terjadi karena data dimasukkan secara berurutan (10, 20, 30), sehingga setiap data baru selalu lebih besar dari sebelumnya.
# 3. Akibatnya, semua node baru akan terus ditambahkan ke sisi kanan ('Right Child'), membuat pohon terlihat seperti garis lurus atau 'Linked List'.
# 4. Fungsi 'preorder' mencetak data dengan urutan Akar -> Kiri -> Kanan, yang dalam kasus ini menghasilkan urutan yang sama dengan data input.
# 5. Fungsi 'tampil_struktur' memberikan gambaran visual tingkat kedalaman (level) untuk menunjukkan betapa tidak seimbangnya pohon tersebut.
# 6. Visualisasi Struktur:
# [ 10 ] (Root)
# \
# [ 20 ] (Right Child)
# \
# [ 30 ] (Right Child)
# 7. Dampak Struktur Ini: Pencarian data dalam pohon yang miring menjadi tidak efisien (lambat) karena sistem harus melewati semua node satu per satu, mirip dengan mencari data dalam daftar biasa.
# 8. Hasil Output Preorder: 10 20 30