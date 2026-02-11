class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next  #Pindahkan head ke node berikutnya
            temp = None            #Hapus referensi lama
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Node dengan nilai {key} tidak ditemukan.")
            return

        #Lepaskan node dari linked list
        prev.next = temp.next
        temp = None

    #Fungsi pembantu untuk mencetak list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")