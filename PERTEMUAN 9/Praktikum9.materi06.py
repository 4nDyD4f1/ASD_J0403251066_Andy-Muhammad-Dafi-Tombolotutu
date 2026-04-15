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
root = Node("Direktur")

#Membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#Membuat child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.left = Node("Staff3")
root.right.right = Node("Staff4")

#Menyampaikan isi node
print('Postorder Traversal:')
postorder(root)