class Node:
    def __init__(self, data):
        self.data = data    #menyimpan data pada node
        self.left = None   #child kiri
        self.right = None  #child kanan

#Membuat node root
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menyampaikan isi node
print('Data pada root:', root.data)
print('Child kiri root:', root.left.data)
print('Child kanan root:', root.right.data)
print('Data pada child kiri root:', root.left.left.data)
print('Data pada child kanan root:', root.left.right.data)

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Penunjuk ke anak (child) sebelah kiri
        self.right = None   # Penunjuk ke anak (child) sebelah kanan

# Membuat node root sebagai fondasi awal pohon
root = Node("A")

# Membuat child level 1: menghubungkan node B dan C ke root
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2: menghubungkan node D dan E ke node B
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node untuk verifikasi struktur
print('Data pada root:', root.data)
print('Child kiri root:', root.left.data)
print('Child kanan root:', root.right.data)
print('Data pada child kiri dari B (D):', root.left.left.data)
print('Data pada child kanan dari B (E):', root.left.right.data)

#penjelasan:
# 1. Kode ini membangun struktur Binary Tree (Pohon Biner) yang terdiri dari 3 level.
# 2. 'root' adalah level 0 (puncak) yang berisi data "A".
# 3. 'root.left' dan 'root.right' adalah level 1, yang menampung data "B" dan "C".
# 4. 'root.left.left' dan 'root.left.right' adalah level 2, di mana data "D" dan "E" 
#    menjadi anak dari node "B".
# 5. Struktur ini menunjukkan hubungan hierarki: A adalah parent dari B & C, 
#    sedangkan B adalah parent dari D & E.
# 6. Jika divisualisasikan, bentuknya seperti ini:
#          A
#        /   \
#       B     C
#      / \
#     D   E