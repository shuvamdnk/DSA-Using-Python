# A dynamic array starts with a fixed capacity. When full, it allocates a new, larger buffer (typically 2×),
# copies all elements, and frees the old buffer. This gives O(1) amortised append.

class DynamicArray:
    def __init__(self):
        self.capasity = 2
        self.data = [None] * self.capasity
        self.size = 0
        
    def __repr__(self):
        return str(self.data[:self.size])

    def __len__(self):
        return self.size
    
    def __getitem__(self, key):
        if key < 0 or key >= self.size:
            raise IndexError("Array index out of range")
        return self.data[key]

    def append(self, value):
        if self.size == self.capasity:
            self.resize(2 * self.capasity)

        self.data[self.size] = value
        self.size += 1

    def resize(self, capasity):
        new_cap = [None] * capasity
        for i in range(self.size):
            new_cap[i] = self.data[i]
        self.data = new_cap
        self.capasity = capasity    

dynamic_arr = DynamicArray()

dynamic_arr.append(12)
dynamic_arr.append(34)
dynamic_arr.append(72)
dynamic_arr.append(22)
dynamic_arr.append(25)
dynamic_arr.append(90)
print(f"Dynamic Array Length = {len(dynamic_arr)}")

print(dynamic_arr)