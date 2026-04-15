class Node:
    def __init__(self, data):
        self.data = data    #menyimpan data pada node
        self.left = None   #child kiri
        self.right = None  #child kanan

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

#Membuat node root
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menyampaikan isi node
print('Postorder Traversal:')
postorder(root)