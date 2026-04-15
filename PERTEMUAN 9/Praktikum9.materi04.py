class Node:
    def __init__(self, data):
        self.data = data    # menyimpan data pada node
        self.left = None    # child kiri
        self.right = None   # child kanan

def inorder(node):
    if node is not None:
        inorder(node.left)        # Langkah 1: Kunjungi cabang kiri sampai ujung
        print(node.data, end=' ') # Langkah 2: Cetak data node (Root/Parent)
        inorder(node.right)       # Langkah 3: Kunjungi cabang kanan

# Membuat node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menyampaikan isi node
print('Inorder Traversal:')
inorder(root)

#penjelasan:
# 1. Kode ini menggunakan metode penelusuran 'Inorder' dengan urutan: Kiri -> Root -> Kanan.
# 2. Cara kerjanya: Program akan turun ke cabang paling kiri (D), kemudian mencetak parent-nya (B),
#    lalu mengecek anak kanan (E), baru kemudian kembali ke root paling atas (A), dan terakhir ke sisi kanan (C).
# 3. Urutan eksekusi pada kode ini adalah:
#    - Cek kiri dari A -> ke B. Cek kiri dari B -> ke D. (D dicetak)
#    - Kembali ke B. (B dicetak)
#    - Cek kanan dari B -> ke E. (E dicetak)
#    - Kembali ke root utama. (A dicetak)
#    - Cek kanan dari A -> ke C. (C dicetak)
# 4. Hasil akhir output yang dihasilkan adalah: D B E A C.