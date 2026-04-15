class Node:
    def __init__(self, data):
        self.data = data    # menyimpan data pada node
        self.left = None    # child kiri
        self.right = None   # child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=' ') # Langkah 1: Cetak data node saat ini (Root)
        preorder(node.left)       # Langkah 2: Kunjungi cabang kiri secara rekursif
        preorder(node.right)      # Langkah 3: Kunjungi cabang kanan secara rekursif

# Membuat node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node
print('Preorder Traversal:')
preorder(root)

#penjelasan:
# 1. Kode ini mengimplementasikan penelusuran pohon (Tree Traversal) menggunakan metode Preorder.
# 2. Fungsi 'preorder(node)' bekerja secara rekursif. Artinya, fungsi akan memanggil dirinya sendiri
#    sampai menemukan node yang kosong (None).
# 3. Urutan eksekusi Preorder adalah "Root-Left-Right":
#    - Pertama, cetak isi node (A).
#    - Kedua, masuk ke cabang kiri (B), lalu cetak B, lalu ke anak-anaknya (D dan E).
#    - Terakhir, setelah sisi kiri selesai, pindah ke cabang kanan (C).
# 4. Berdasarkan struktur pohon yang dibuat, urutan output yang muncul adalah: A B D E C.
# 5. Visualisasi alur: A -> B -> D -> E -> C.