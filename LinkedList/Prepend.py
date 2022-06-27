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

    def pop(self):
        if self.head is None:
            return None

        current = self.head
        previous = self.head

        while current.next is not None:
            previous = current
            current = current.next
        self.tail = previous
        self.tail.next = None

    def prepend(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

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
newLL.append(10)
newLL.append(20)
newLL.prepend(33)
newLL.pop()
newLL.printList()
