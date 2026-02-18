#========================================
#Nama: Andy Muhammad Dafi Tombolotutu
#NIM: J0403251066
#========================================


#========================================
#Implementasi Dasar: Node pada LinkedList
#========================================

class Node:
    def __init__(self,data):
        self.data = data #Menyimpan nilai/data
        self.next = None #Pointer ke note berikutnya

# 1) Membuat mode satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mehubungkan Node : A->B->C-> None
nodeA.next = nodeB
nodeB.next = nodeC


#3) Menentukan node pertama (head)
head = nodeA


#4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)     #Menampilkan data pada node saat ini
    current = current.next  #Pindah ke node berikutnya


#========================================
#Implementasi Dasar : Linked List + Insert Awal
#========================================

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_awal(self,data):
        #1) Buat node baru
        nodeBaru = Node(data)

        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3) head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self):
        data_terhapus = self.head.data
        self.head = self.head.next
        print("Node yang dihapus adalah:", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList() #instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
