class Node:
    def __init__(self, val = None, next1 = None):
        self.val = val
        self.next = next1

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or self.size == 0 or index < 0:
            return -1

        if index == 0:
            return self.head.val
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
        else:
            new_node = Node(val, self.head)
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            new_node = Node(val)
            current.next = new_node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(val, current.next)
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or self.size == 0 or index < 0:
            return

        if self.size == 1:
            self.head = None
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
