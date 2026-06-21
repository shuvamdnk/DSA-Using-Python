class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # prefix sum
        ans = [1 for _ in range(len(nums))]
        suffix = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
    
        for i in range(len(nums) - 2, -1, -1):
            suffix = suffix * nums[i+1] 
            ans[i] = ans[i] * suffix
        
        return ans


obj = Solution()

print(obj.productExceptSelf([1,2,3,4]))