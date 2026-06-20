from functools import reduce
# args
def add(*nums):
    return reduce(lambda s, x: s + x, nums)

print(add(1,2,3,4,5,6,7))