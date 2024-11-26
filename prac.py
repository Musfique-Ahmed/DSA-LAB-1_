class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_beginning(self, data):
        new_mode = Node(data)
        new_mode.next = self.head
        self.head = new_mode

    def display(self):
        current = self.head
        if not current:
            print("This list is empty")
            return
        while current:
            print(current.data, end= "->")
            current = current.next
        print("None")

sll = SinglyLinkedList()
sll.add_to_beginning(5)
sll.add_to_beginning(15)
sll.add_to_beginning(-5)
sll.display()