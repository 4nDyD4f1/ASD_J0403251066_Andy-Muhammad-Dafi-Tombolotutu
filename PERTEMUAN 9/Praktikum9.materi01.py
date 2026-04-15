class Node:
    def __init__(self, data):
        self.data = data    #
        self.right = None
        self.left = None

root = Node("A")

print('Data pada root:' ,root.data)
print('Child kiri root:' ,root.left)
print('Child kanan root:' ,root.right)