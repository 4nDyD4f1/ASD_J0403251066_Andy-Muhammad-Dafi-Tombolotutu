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