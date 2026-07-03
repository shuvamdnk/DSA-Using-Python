def maxCoinsInfiniteSwitches(lane1: list[int], lane2: list[int]) -> int:
    n = len(lane1)
    
    # Stores the best coin total ending at the current position
    current_max = 0
    # Stores the overall maximum collection found across the entire array
    global_max = float('-inf')
    
    for i in range(n):
        # Step 1: Since you can switch anytime, always target the lane with more coins
        best_coin_here = max(lane1[i], lane2[i])
        
        # Step 2: Decide whether to extend the current trip or start a brand new one
        current_max = max(best_coin_here, current_max + best_coin_here)
        
        # Step 3: Keep track of the highest peak reached
        global_max = max(global_max, current_max)
        
    return int(global_max)

# Run Test Cases
tests = [
    ([1, -5, 3, -2], [-2, 4, -1, 5], 13),
    ([-8, -10, 5, 6], [-5, -9, 2, -1], 11),
    ([-3, -4, -2], [-5, -1, -6], -1),
    ([10, 20, 30, 40], [1, 2, 3, 4], 100)
]

for idx, (l1, l2, expected) in enumerate(tests, 1):
    result = maxCoinsInfiniteSwitches(l1, l2)
    print(f"Test {idx}: {'PASSED' if result == expected else 'FAILED'} (Got: {result}, Expected: {expected})")