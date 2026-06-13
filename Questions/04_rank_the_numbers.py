def rank_elements_inplace(nums):
    if not nums:
        return []
        
    # 1. Pair each number with its original index: [(9, 0), (2, 1), (4, 2)...]
    # Then sort by the numbers in descending order
    indexed_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
    
    ranks = [0] * len(nums)
    current_rank = 1
    # print(indexed_nums)  # Debug: Show the sorted indexed numbers
    # 2. Assign rank 1 to the largest element
    ranks[indexed_nums[0][0]] = current_rank
    # print(ranks)
    # 3. Loop through the rest, increasing the rank ONLY if the number changes
    for i in range(1, len(indexed_nums)):
        # If this number is smaller than the previous one, bump the rank
        # print(f"Comparing {indexed_nums[i][1]} with {indexed_nums[i-1][1]}")
        if indexed_nums[i][1] < indexed_nums[i-1][1]:
            current_rank += 1
            
        # Put the rank back into the element's original position
        original_idx = indexed_nums[i][0]
        ranks[original_idx] = current_rank
        
    return ranks

print(rank_elements_inplace([9, 2, 4, 3, 10, 10]))  # Output: [2, 5, 3, 4, 1, 1]