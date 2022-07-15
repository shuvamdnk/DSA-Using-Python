class Queue:
    def __init__(self,size):
        self.queue = []
        self.size= size

    def insert(self,ele):
        if(len(self.queue) < self.size):
            self.queue.append(ele)
        else:
            print('Queue Overflow')    

    def remove(self):
        if(len(self.queue) > 0):
            print(f'{self.queue.pop(0)} removed from queue')
        else:
            print('Queue Underflow')

    def display(self):
        if(len(self.queue) > 0):
            for i in range(len(self.queue)):
                if(i == (len(self.queue)-1)):
                    print(self.queue[i])
                else:    
                    print(self.queue[i], end=" <- ")
        else:
            print('Queue Underflow')      


queue = Queue(5)
queue.display()                
queue.insert(12)
queue.insert(25)
queue.insert(20)
queue.insert(10)
queue.display()
queue.remove()
queue.display()    

queue.remove()
queue.display()   

queue.remove()
queue.display()   

queue.remove()
queue.display()   

queue.remove()
queue.display()   