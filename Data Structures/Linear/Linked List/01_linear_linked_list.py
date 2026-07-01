class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def push_front(self, data):
        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def push_back(self, data):
        node = Node(data)
        if self.tail == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        # if self.head == None:
        #     self.head = node
        # else:
        #     temp = self.head
        #     while temp.next:
        #         temp = temp.next
        #     # print(temp.next)
        #     temp.next = node
    
    def pop_front(self):
        if self.head == None:
            return
        self.head = self.head.next

    def pop_back(self):
        if self.head == None:
            return
        
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next

        temp.next = None
        self.tail = temp
        
    

ll = LinkedList()

ll.push_front(1)
ll.push_front(2)
ll.push_front(24)
ll.push_back(50)
ll.push_back(54)
ll.pop_front()
ll.pop_back()
ll.push_back(102)
ll.print_list()