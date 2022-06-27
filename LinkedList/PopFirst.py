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

    def popFirst(self):
        current = self.head
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            current.next = None
        self.length -= 1

    def printList(self):
        if self.head is None:
            print("Empty")
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
newLL.popFirst()

newLL.printList()
