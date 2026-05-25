#Factorial of number
# def factorial(n):
#     if n == 0:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))

# Fibonacci seriese
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
    
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

# Fibonacci list
def fibonacci_list(n):
    if n == 0:
        return [0]
    
    if n == 1:
        return [0, 1]
    series = fibonacci_list(n-1)
    series.append(series[-1] + series[-2])
    return series

print(fibonacci_list(5))
