class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan nilai pada node
        self.right = None   # Menyiapkan pointer untuk anak sebelah kanan
        self.left = None    # Menyiapkan pointer untuk anak sebelah kiri

root = Node("A")

print('Data pada root:' ,root.data)
print('Child kiri root:' ,root.left)
print('Child kanan root:' ,root.right)

#penjelasan:
# 1. Class Node berfungsi sebagai cetak biru (blueprint) untuk setiap titik dalam pohon.
# 2. Metode __init__ menginisialisasi node baru dengan data tertentu ("A").
# 3. 'self.left' dan 'self.right' diatur ke 'None' karena saat node dibuat, 
#    ia belum memiliki hubungan atau cabang ke node lainnya.
# 4. 'root = Node("A")' membuat objek pertama yang bertindak sebagai akar dari struktur data ini.
# 5. Output print menunjukkan bahwa root memiliki data "A", namun anak kiri dan kanannya
#    masih kosong (None) karena belum ada node baru yang disambungkan.