# built-in functions
# num = 16

# print(int(bin(num),2))
# print(int(oct(num),0))
# print(hex(num))


# Custom Logic
import string

def any_base_to_decimal(value:str, base):
    digits = string.digits + string.ascii_uppercase
    power = len(str(value)) - 1
    decimal = 0
    for ch in value.upper():
        digit = digits.index(ch)
        decimal += digit * (base ** power)
        power -= 1
    return decimal

print(any_base_to_decimal("A1F",16))
    



