# def numbers():
#     print("Start")
#     yield 1

#     print("Middle")
#     yield 2

#     print("End")
#     yield 3

# g = numbers()

# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))

# for i in g:
#     print(i)


# def echo():
#     value = yield
#     print(value)

# e = echo()
# next(e)
# e.send("Hello")


# r = range(5)

# print(iter(r))


# class Counter:
#     def __init__(self):
#         self.i = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i > 3:
#             raise StopIteration

#         value = self.i
#         self.i += 1
#         return value

# c = Counter()

# for x in c:
#     print(x)


# import copy

# a = [(1, 2), (3, 4)]

# b = copy.copy(a)
# c = copy.deepcopy(a)

# print(a[0] is b[0])  # True
# print(a[0] is c[0])  # Usually True



a = []
b = []

a.append(b)
b.append(a)

del a
del b