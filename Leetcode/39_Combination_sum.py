class Solution:
    def getCombinations(self, arr, i, combination, ans, target):
        # print(combination)
        if target == 0:
            ans.append(combination.copy())
            return
        
        if i == len(arr) or target < 0:
            return
        
        

        # include single
        combination.append(arr[i])
        self.getCombinations(arr, i, combination, ans, target - arr[i])

        # Backtrack
        combination.pop()

        # Exclusion
        self.getCombinations(arr, i+1, combination, ans, target)




    def combinationSum(self, arr: list[int], target: int) -> list[list[int]]:
        
        ans = []
        combination = []

        self.getCombinations(arr, 0, combination, ans, target)

        return ans
    


obj = Solution()

print(obj.combinationSum([2,3,6,7], 7))