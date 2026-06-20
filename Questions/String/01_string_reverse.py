# reverse a string

st = "Hello"

print(st[::-1])
print("".join(reversed(st)))

# recusrion
def reverse_str(str):
    if len(str) <= 1:
        return str
    return str[-1] + reverse_str(str[:-1])

print(reverse_str(st))