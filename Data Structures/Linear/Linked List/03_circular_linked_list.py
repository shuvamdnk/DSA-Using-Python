class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insertHead(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
    
    def print_list(self):
        if self.head == None:
            return
        temp = self.head

        print(temp.data, end=" => ")

        while temp.next != self.head:
            print(temp.next.data, end=" => ")
            temp = temp.next
        
        print(temp.next.data)
    
    def insertTail(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node

    def pop_head(self):
        if self.head == None:
            return
        if self.head.next == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    def pop_tail(self):
        if self.head == None:
            return
        if self.head.next == self.head:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            self.tail = temp
            self.tail.next = self.head


cll = CircularLinkedList()

cll.insertHead(1)
cll.insertHead(2)
cll.insertHead(3)

cll.insertTail(20)
cll.pop_head()
cll.pop_tail()
cll.print_list()