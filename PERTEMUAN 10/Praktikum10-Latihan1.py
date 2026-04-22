#=============================================================================================
#Latihan 1 : BST
#=============================================================================================

class Node:
    def __init__(self,data):    #
        self.data = data        #
        self.left = None        #
        self.right = None       #

#Alur Fungsi insert BST :

def insert(root,data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left,data)
    elif data > root.data:
        root.right = insert(root.right,data)

    return root

#Mengisi data BST
root = None
data_list = [50,30,70,20,40,50,80]

for data in data_list:
    root = insert(root,data)

print("BST berhasil dibuat")

#=============================================================================================
#Latihan 2 : Traversal Inorder
#=============================================================================================

#Alur fungsi inorder :

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Hasil Inorder:")
inorder(root)

#=============================================================================================
#Latihan 3 : Search di BST
#=============================================================================================

def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)

#uji pencarian
key = 100

if search(root,key):
    print("Data Ditemukan")
else:
    print("Data Tidak Ditemukan")

#Penjelasan:
# 1. Kode ini menerapkan struktur Binary Search Tree (BST), di mana posisi data ditentukan oleh nilainya.
# 2. Aturan utama BST: Nilai yang lebih kecil dari 'Root' masuk ke kiri, sedangkan nilai yang lebih besar masuk ke kanan.
# 3. Fungsi 'insert' secara otomatis menempatkan data baru pada posisi yang tepat secara rekursif agar pohon tetap terurut.
# 4. Fungsi 'inorder' mengunjungi pohon dengan urutan: Kiri -> Root -> Kanan. Teknik ini selalu menghasilkan data yang terurut dari terkecil ke terbesar.
# 5. Fungsi 'search' melakukan pencarian efisien dengan cara mengabaikan separuh bagian pohon di setiap langkahnya (seperti cara kerja kamus).
# 6. Visualisasi Struktur dari data [50, 30, 70, 20, 40, 60, 80]:
# [ 50 ] (Root)
# /      \
# [ 30 ]   [ 70 ]
# /    \   /    \
# [ 20 ] [ 40 ] [ 60 ] [ 80 ]
# 7. Hasil Output Inorder: 20 30 40 50 60 70 80 (Data terurut sempurna).
# 8. Pada uji pencarian 'key = 100', sistem mengembalikan "Data Tidak Ditemukan" karena 100 tidak ada dalam struktur pohon tersebut.