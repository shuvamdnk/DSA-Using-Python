# Maximum sum subarray of size K
# arr = [2, 0, 5, -1, 3, 2]
# k = 2
# window_sum = sum(arr[:k])
# max_sum = window_sum
# for i in range(k, len(arr)):
#     window_sum += arr[i] - arr[i - k]
#     max_sum = max(max_sum, window_sum)

# print(max_sum)


# Longest substring without repeating characters
# st = 'sfwrssfffdsrqfeweffsfsbdew'

# st1 = ''
# st2 = ''

# for i in st:
#     if i in st1:
#         # 1. Update st2 before we alter st1
#         if len(st1) > len(st2):
#             st2 = st1
#         # 2. Slice st1 to keep everything AFTER the duplicate character
#         st1 = st1[st1.index(i) + 1:]
    
#     # 3. Always append the current character to st1
#     st1 += i

# # Final check for the last substring after the loop finishes
# if len(st1) > len(st2):
#     st2 = st1

# print(st2)  # Correctly outputs: dsrqfew


# seen_chars = set()
# start = 0
# max_len = 0
# longest_sub = ""

# for end in range(len(st)):
#     # If the character is already in the window, shrink the window from the left
#     while st[end] in seen_chars:
#         seen_chars.remove(st[start])
#         start += 1
    
#     # Add the current character to our window
#     seen_chars.add(st[end])
    
#     # Check if the current window is the longest we've seen
#     current_window_len = end - start + 1
#     if current_window_len > max_len:
#         max_len = current_window_len
#         longest_sub = st[start:end + 1]

# print("Maximum Length:", max_len)
# print("Longest Substring:", longest_sub)


# Longest subarray with sum K
arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
k = 3

start = 0
current_sum = 0
max_len = 0

for end in range(len(arr)):
    current_sum += arr[end]

    while current_sum > k and start <= end:
        current_sum -= arr[start]
        start += 1
    
    if current_sum == k:
        max_len = max(max_len, end-start +1)

print(max_len)