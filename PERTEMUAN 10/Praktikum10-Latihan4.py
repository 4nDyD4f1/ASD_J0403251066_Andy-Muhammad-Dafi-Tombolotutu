# ========================================================== 
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang 
# ========================================================== 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def right_rotate(y):
    """
    Melakukan rotasi kanan pada node y.
    Struktur awal: y adalah root, x adalah anak kiri y.
    """
    print(f"--- Melakukan Rotasi Kanan pada node {y.key} ---")
    x = y.left
    T2 = x.right

    # Proses Rotasi
    x.right = y
    y.left = T2

    # Return root baru (x)
    return x

def print_tree(root, level=0, prefix="Root: "):
    """Fungsi pembantu untuk menampilkan struktur pohon."""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")



# 1. Membangun Kondisi "Sebelum Rotasi Kanan"
# Struktur: 30 -> 20 -> 10 (Left-Left Case)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Kondisi SEBELUM Rotasi Kanan:")
print_tree(root)
print("\n")

# 2. Menjalankan Fungsi Rotasi
root = right_rotate(root)

# 3. Menampilkan Hasil "Sesudah Rotasi Kanan"
print("\nKondisi SESUDAH Rotasi Kanan:")
print_tree(root)

#Penjelasan:
# 1. Kode ini mendemonstrasikan teknik 'Right Rotation', kebalikan dari rotasi kiri, yang digunakan untuk menangani pohon yang miring ke kiri (Left-Skewed).
# 2. Kondisi ini sering disebut 'Left-Left Case', di mana Root memiliki anak kiri, dan anak kiri tersebut memiliki cucu di sisi kiri lagi (30 -> 20 -> 10).
# 3. Fungsi 'right_rotate' bekerja dengan cara menurunkan Root lama (30) menjadi anak kanan, dan mengangkat anak kirinya (20) menjadi Root yang baru.
# 4. Jika Node kiri (x) memiliki anak kanan (T2), anak tersebut akan dipindahkan menjadi anak kiri dari Root yang lama (y) agar urutan nilai BST tetap valid.
# 5. Sebelum rotasi, pohon berbentuk garis lurus ke kiri dengan kedalaman 3 tingkat, yang membuat pencarian menjadi lambat.
# 6. Sesudah rotasi, pohon menjadi seimbang (Balanced) sehingga jarak tempuh pencarian data menjadi lebih pendek.
# 7. Visualisasi Perubahan Struktur:
# [Sebelum Rotasi]           [Sesudah Rotasi]
# 30 (Root)                  20 (Root)
# /                          /    \
# 20                        10      30
# /
# 10
# 8. Hasil Akhir: Struktur pohon berubah dari hirarki vertikal (30-20-10) menjadi bentuk piramida yang seimbang dengan 20 sebagai pusatnya.