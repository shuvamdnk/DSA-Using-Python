# Print First N Fibonacci Numbers
# 0,1,1,2,3,5,8,13,...

# Loop
n = 10
a = 0
b = 1
while n >= 0:
    print(a, end= " ")
    c = a + b
    a = b
    b = c
    n -= 1


# Recursion 
# Find nth fibonacci number
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))


# Recursion with sequence
# def fibonacci_sequence(n, arr:list, a=0, b= 1):
#     if n == 0:
#         return
    
#     arr.append(a)

#     fibonacci_sequence(n-1, arr, b, a+b)

# arr = []
# fibonacci_sequence(6,arr)
# print(arr)



    





