# leetcode 46
class Solution:

    def getPermutation(self, nums, idx, ansArr):
        if idx == len(nums)-1:
            ansArr.append(nums[:])
            return
           
        for i in range(idx,len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.getPermutation(nums, idx + 1, ansArr)
            nums[i], nums[idx] = nums[idx], nums[i]


    def permute(self, nums):
        ansArr = []
        self.getPermutation(nums, 0, ansArr)
        return ansArr
    
sl = Solution()
print(sl.permute([1,2,3]))