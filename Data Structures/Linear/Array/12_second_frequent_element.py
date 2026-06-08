from collections import Counter, defaultdict

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = Counter(arr)

print(count)
print(10 in count.keys())
print(sorted(count.items()))

# maxfreq = max(count.values())

# print(maxfreq)

# print(len(count))

# def_dict = defaultdict(list)

# for item, value in count.items():
#     def_dict[value].append(item)

# print(def_dict)

# print(len(def_dict))

# second_freq = def_dict[1]


# from collections import Counter

# def second_most_frequent(arr):
#     if not arr:
#         return -1
    
#     # Step 1: Count frequencies of each element
#     freq_map = Counter(arr)
#     print(freq_map)
#     # Step 2: Group elements by their frequency
#     # Key = frequency, Value = list of numbers with that frequency
#     grouped_by_freq = {}
#     for num, count in freq_map.items():
#         if count not in grouped_by_freq:
#             grouped_by_freq[count] = []
#         grouped_by_freq[count].append(num)

#     print(grouped_by_freq)
        
#     # Step 3: Get all unique frequencies sorted in descending order
#     unique_counts = sorted(grouped_by_freq.keys(), reverse=True)
#     print(unique_counts)
#     # Step 4: Check if a second most frequent element exists
#     if len(unique_counts) < 2:
#         return -1
    
#     # Get the frequency of the second most frequent element(s)
#     second_highest_freq = unique_counts[1]
#     candidates = grouped_by_freq[second_highest_freq]
    
#     # Step 5: Return the maximum number if there's a tie
#     return max(candidates)

# # --- Test Cases ---
# print(second_most_frequent([1, 1, 1, 2, 2, 3, 3]))        # Output: 2  (Freq of 1 is 3, Freq of 2 is 2)
# # print(second_most_frequent([1, 1, 1, 2, 2, 3, 3]))     # Output: 3  (Tie for second freq: 2 and 3. Max is 3)
# # print(second_most_frequent([1, 1, 1, 1]))              # Output: -1 (No second most frequent element)
# # print(second_most_frequent([4, 4, 2, 2, 3, 3, 3, 3]))  # Output: 4  (Tie for second freq: 4 and 2. Max is 4)