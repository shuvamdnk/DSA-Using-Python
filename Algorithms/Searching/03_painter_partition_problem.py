class Solution:
    def isValid(self, arr, totalPainters, maxTime):
        painter = 1
        time = 0
        
        for i in arr:
            if i > maxTime:
                return False
                
            if time + i <= maxTime:
                time += i
            else:
                painter += 1
                time = i
                
        if painter > totalPainters:
            return False
        else:
            return True
        
    def minTime (self, arr, k):
        # code here
            
        start = max(arr)
        end = sum(arr)
        ans  = -1
        while start <= end:
            mid = (start + end) // 2
            print(f"start = {start}, end = {end}, mid = {mid}, ans = {ans}", end= " ")
            
            if self.isValid(arr, k ,mid):
                ans = mid
                end = mid - 1
                print("Valid")
            else:
                start = mid + 1
                print("InValid")
        
        return ans
    
    
sol = Solution()
print(sol.minTime([5,10,30,20,15], 3))

