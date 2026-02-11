class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            return "kosong"
        
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " -> ".join(elements) + " -> null"

def merge_lists(list1, list2):
    #Jika list 1 kosong, maka hasilnya adalah list 2
    if not list1.head:
        return list2
    #Jika list 2 kosong, maka hasilnya adalah list 1
    if not list2.head:
        return list1

    #Cari node terakhir di list 1
    temp = list1.head
    while temp.next:
        temp = temp.next
    
    #Sambungkan node terakhir list 1 ke head list 2
    temp.next = list2.head
    return list1

#Program Utama
ll1 = LinkedList()
ll2 = LinkedList()

#Input List 1
in1 = input("Masukkan elemen untuk Linked List 1: ").strip().replace(',', ' ')
if in1:
    for val in in1.split():
        ll1.insert(int(val))

#Input List 2
in2 = input("Masukkan elemen untuk Linked List 2: ").strip().replace(',', ' ')
if in2:
    for val in in2.split():
        ll2.insert(int(val))

#Tampilan sebelum digabung
print(f"Linked List 1: {ll1.display()}")
print(f"Linked List 2: {ll2.display()}")

#Gabungkan
merged_list = merge_lists(ll1, ll2)

#Tampilan sesudah digabung
print(f"Linked List setelah digabungkan: {merged_list.display()}")