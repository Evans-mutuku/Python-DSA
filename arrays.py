class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

LI = LinkedList()
LI.append(1)
LI.append(2)


# Arrays
numbers = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
print(numbers[5])