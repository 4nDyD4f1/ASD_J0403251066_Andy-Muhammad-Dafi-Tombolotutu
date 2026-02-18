class Node:
    def __init__(self,data):
        self.data = data #Menyimpan nilai/data
        self.next = None #Pointer ke note berikutnya

class QueueLL:
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None  #node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        #Menambahkan data di belakang (rear)
        nodeBaru = Node(data)

        #jika queue kosong, front dan rear menunjukkan kode yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong: 
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru

    def tampilkan(self):

        current = self.front
        print("Front ->", end="")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")

# Intantiasi objek class QueueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()