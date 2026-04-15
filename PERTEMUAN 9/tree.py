class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

print(root.data)