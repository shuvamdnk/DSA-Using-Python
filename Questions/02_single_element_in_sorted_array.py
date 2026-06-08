nums = [3,3,7,7,10,11,11]
start = 0
end = len(nums) - 1

while start <= end:
    mid = (start + end) // 2
    
    if nums[mid] != nums[mid + 1] != nums[mid - 1]:
        print(nums[mid])
        
    if len(nums[start:mid]) % 2 == 1:
        if nums[mid] == nums[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if nums[mid] == nums[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1
   
    
