class Node:
    def __init__(self, data):
        self.data = data    # menyimpan data pada node (Nama Jabatan)
        self.left = None    # penunjuk ke bawahan di sisi kiri
        self.right = None   # penunjuk ke bawahan di sisi kanan

def preorder(node):
    if node is not None:
        print(node.data, end=' | ')
        preorder(node.left)
        preorder(node.right)    

# Membuat node root (Pimpinan Tertinggi)
root = Node("Direktur")

# Membuat child level 1 (Para Manajer)
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Membuat child level 2 (Staff di bawah Manajer A)
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

# Membuat child level 2 (Staff di bawah Manajer B)
root.right.left = Node("Staff 3")
root.right.right = Node("Staff 4")

# Menampilkan isi struktur organisasi
print('Struktur Organisasi Perusahaan (Preorder): ')
preorder(root)

#Penjelasan:
# 1. Kode ini menggambarkan hierarki organisasi menggunakan struktur Binary Tree.
# 2. Direktur bertindak sebagai 'Root' atau pusat komando tertinggi.
# 3. Manajer A dan B adalah 'Child' langsung dari Direktur (Level 1).
# 4. Staff 1 & 2 adalah bawahan (Child) dari Manajer A, sedangkan Staff 3 & 4 adalah bawahan Manajer B.
# 5. Fungsi 'preorder' mencetak data dengan urutan Atasan dulu, baru bawahan kiri, lalu bawahan kanan.
# 6. Visualisasi Struktur:
#
#             [ Direktur ]
#              /        \
#      [Manajer A]    [Manajer B]
#        /    \         /    \
#    [Staff1] [Staff2] [Staff3] [Staff4]
#
# Hasil Output Preorder: Direktur | Manajer A | Staff 1 | Staff 2 | Manajer B | Staff 3 | Staff 4 |