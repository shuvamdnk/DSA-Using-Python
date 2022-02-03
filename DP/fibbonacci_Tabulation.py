# Tabulation (Buttom-up)
def fib(n):
    f = [0] * (n+1)
    f[1] = 1

    print(f[0] ,end=" ")

    print(f[1] ,end=" ")

    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
        print(f[i],end=" ")

    return f[i]    

if __name__ == '__main__':
    n = 10
    fibo = fib(n)
    print()
    print(f"Fibonecci of {n} is {fibo}")