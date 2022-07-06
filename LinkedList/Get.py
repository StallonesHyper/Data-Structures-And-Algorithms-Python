

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            print("None")
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            print(current.value)

    def printList(self):
        if self.head is None:
            print("Empty LinkedList")
        current = self.head
        while current is not None:
            print(current.value, end="->")
            if current.next is None:
                print(end="None")
            current = current.next


newLL = LinkedList()
newLL.append(100)
newLL.append(200)
newLL.append(300) 
newLL.append(400)
newLL.get(2)
newLL.printList()
