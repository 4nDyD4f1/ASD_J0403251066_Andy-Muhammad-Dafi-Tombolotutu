class Node:
    def __init__(self, data):
        self.data = data    #menyimpan data pada node
        self.left = None   #child kiri
        self.right = None  #child kanan

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

#Membuat node root
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menyampaikan isi node
print('Inorder Traversal:')
inorder(root)