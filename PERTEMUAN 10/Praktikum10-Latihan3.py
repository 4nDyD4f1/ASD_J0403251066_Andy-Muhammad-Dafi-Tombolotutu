# ========================================================== 
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
# ========================================================== 
 
# Class Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
 
 
# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 
 
 
# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara

    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2

     # y menjadi root baru 
    return y    

# ----------------------------- 
# Program utama 
# ----------------------------- 
# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10) 
root.right = Node(20) 
root.right.right = Node(30) 

print("Preorder sebelum rotasi kiri:") 
preorder(root) 

print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root) 

# Melakukan rotasi kiri pada root 
root = rotate_left(root) 

print("\nPreorder sesudah rotasi kiri:") 
preorder(root) 

print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root)

#Penjelasan:
# 1. Kode ini mendemonstrasikan teknik 'Left Rotation', sebuah operasi dasar untuk menyeimbangkan Binary Search Tree (BST) yang condong ke kanan.
# 2. Rotasi dilakukan untuk menurunkan tinggi pohon agar pencarian data tetap efisien dan tidak berubah menjadi linear seperti Linked List.
# 3. Fungsi 'rotate_left' bekerja dengan cara menarik Node kanan (20) ke atas menjadi 'Root' baru, dan menggeser Root lama (10) menjadi 'Left Child'.
# 4. Jika Node kanan memiliki anak kiri (T2), anak tersebut akan dipindahkan menjadi anak kanan dari Root yang lama agar aturan BST tetap terjaga.
# 5. Sebelum rotasi, pohon berbentuk miring ke kanan (Skewed Right) dengan kedalaman 3 tingkat.
# 6. Sesudah rotasi, pohon menjadi lebih seimbang dengan 20 sebagai pusat, 10 di kiri, dan 30 di kanan.
# 7. Visualisasi Perubahan Struktur:
# [Sebelum Rotasi]           [Sesudah Rotasi]
# 10 (Root)                  20 (Root)
# \                       /    \
# 20                  10       30
# \
# 30
# 8. Hasil Output Preorder:
# - Sebelum: 10 20 30 (Miring)
# - Sesudah: 20 10 30 (Seimbang)