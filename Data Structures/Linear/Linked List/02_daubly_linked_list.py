class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
    
    def push_back(self, data):
        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
    
    def pop_front(self):
        if self.head == None:
            return
        temp = self.head
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
        del temp

    def pop_back(self):
        if self.head == None:
            return
        temp = self.tail
        if self.tail.pre is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None

        del temp


    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <==> ")
            temp = temp.next

        print(temp)


dll = DoublyLinkedList()

dll.push_front(1)
dll.push_front(2)
dll.push_front(3)

dll.push_back(6)
dll.push_back(10)

dll.pop_front()
dll.pop_back()

dll.pop_front()
dll.pop_back()
dll.print_list()