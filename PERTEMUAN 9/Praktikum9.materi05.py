class Node:
    def __init__(self, data):
        self.data = data    # menyimpan data pada node
        self.left = None    # child kiri
        self.right = None   # child kanan

def postorder(node):
    if node is not None:
        postorder(node.left)      # Langkah 1: Kunjungi cabang kiri sampai ujung
        postorder(node.right)     # Langkah 2: Kunjungi cabang kanan sampai ujung
        print(node.data, end=' ') # Langkah 3: Cetak data node tersebut (Root/Parent)

# Membuat node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menyampaikan isi node
print('Postorder Traversal:')
postorder(root)

#penjelasan:
# 1. Kode ini mengimplementasikan penelusuran 'Postorder' dengan prinsip: Selesaikan anak-anaknya dulu, baru orang tuanya.
# 2. Urutan langkahnya adalah: Sisi Kiri -> Sisi Kanan -> Root.
# 3. Alur eksekusi pada pohon ini:
#    - Program menuju ke paling bawah kiri yaitu D. (D dicetak)
#    - Program menuju ke saudara kanannya yaitu E. (E dicetak)
#    - Setelah anak-anaknya selesai, barulah parent mereka dicetak yaitu B. (B dicetak)
#    - Program pindah ke sisi kanan root utama yaitu C. (C dicetak)
#    - Terakhir, barulah titik paling atas atau root utama dicetak. (A dicetak)
# 4. Hasil akhir output yang dihasilkan adalah: D E B C A.