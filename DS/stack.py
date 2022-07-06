class Stack:
    def __init__(self,size) -> None:
        self.size = size
        self.stack = []

    def push(self):
        if len(self.stack) < self.size:
            ele = int(input("Enter the element > "))
            self.stack.append(ele)
            self.display()
        else:
            print("Stake Overflow")

    def pop(self):
        if len(self.stack) > 0:
            ele = self.stack.pop()
            print(f"{ele} Removed from stack")
        else:
            print('Stack Underflow')    

    def display(self):
        for i in self.stack:
            print(f"[{i}]",end=" ")


try:
    n = int(input("Enter the stack size > "))
    stack = Stack(n)

    while True:
        print('\n---------------------------')
        print('1) Push')
        print('2) Pop')
        print('3) Display')
        print('4) Exit')
        print('---------------------------')

        opt = int(input("Enter a option > "))
        if(opt == 1):
            stack.push()
        elif opt == 2:
            stack.pop()
        elif opt == 3:
            stack.display() 
        else:
            break    

except ValueError:
    print("Value Error")
except NameError:
    print('Name Error')  
except TypeError:
    print('Type Error')    
except Exception as e: 
    print(e)   

finally:
    print("Thank You")





                    