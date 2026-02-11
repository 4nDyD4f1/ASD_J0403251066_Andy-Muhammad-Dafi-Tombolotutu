class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        #Contoh Tampilan #3: Jika list kosong
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        curr = self.head
        found = False
        
        #Penelusuran menggunakan logika do-while
        while True:
            if curr.data == key:
                found = True
                break
            curr = curr.next
            if curr == self.head:
                break
        
        if found:
            print(f"Elemen {key} ditemukan dalam Circular Linked List.")
        else:
            print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

#Program Utama
cll = CircularLinkedList()

print("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma atau spasi):")
user_input = input("Elemen: ").strip()

#Memproses input user
if user_input:
    #Mengganti koma menjadi spasi dan memisahkan angka
    elements = user_input.replace(',', ' ').split()
    for item in elements:
        cll.insert(int(item))

try:
    search_key = int(input("Masukkan elemen yang ingin dicari: "))
    cll.search(search_key)
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")