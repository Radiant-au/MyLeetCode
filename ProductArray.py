from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        for i in range(len(nums)):
            nums[i] = prefix 
            prefix *= nums[i]
        
        return result
    
solution = Solution()
arr = [1 ,2 ,3, 4]
k = solution.productExceptSelf(arr)
print(k)
            