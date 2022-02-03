# Fibbonecci Number Problem
#Memoization(Top Down)  Technique

def fib(n,lookup):
    # print(lookup[n])
    if n <= 1:
        lookup[n] = n

    if lookup[n] == None:
        lookup[n] = fib(n-1,lookup) + fib(n-2,lookup)  

    return lookup[n]
      
if __name__ == '__main__':
    n = 34
    lookup = [None] * 101
    fibo = fib(n,lookup)
    # print(lookup)
    print(fibo)


