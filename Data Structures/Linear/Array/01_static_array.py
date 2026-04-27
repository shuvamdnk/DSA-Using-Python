# An array is a contiguous block of memory storing elements of the same type. Elements are accessed
# in O(1) via index because the address of element i is simply: base_address + i × element_size.
import ctypes

static_array = []
# length 
print(len(static_array))

# memory address in binary
print(id(static_array))

# memory address in hex
print(hex(id(static_array)))

static_array.append(23)
static_array.append(45)

print(static_array)

print(id(static_array[0]))
print(id(static_array[1]))

# So here the index return the address of 23 and 45 no the address of the list index

import array

# 1. Create an array of 'i' (signed integers)
# These are typically 4 bytes each.
numbers = array.array('i', [100, 200, 300, 400])

# 2. Get the memory info
# buffer_info() returns (address, length)
address, length = numbers.buffer_info()

print(f"The array starts at memory address: {(address)}")
print(f"Number of elements: {length}")
print("-" * 40)

# 3. Calculate where each element lives in RAM
# Since each 'i' is 4 bytes, we add 4 to the address for each index.
item_size = numbers.itemsize # This will be 4

for i in range(length):
    element_address = address + (i * item_size)
    print(f"Index {i} (Value {numbers[i]}) is physically at: {(element_address)}")

