# arr = [1, 2, 2, 3, 4, 4 , 4, 5]

# count = dict()

# for i in arr:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(count)


def myPow(x: float, n: int) -> float:
    power = 1
    for i in range(abs(n)):
        print("print",x)
        if n > 0:
            power *= x
        else:
            power *= 1/x
            print(power)
    return power
    
print(myPow(2.00000,-2))