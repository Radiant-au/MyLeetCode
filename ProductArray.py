from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            arr[i] = prefix 
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1 , -1 , -1):
            arr[i] *= postfix
            postfix *= nums[i]
            
        return arr
        
solution = Solution()
arr = [1 ,2 ,3, 4]
k = solution.productExceptSelf(arr)
print(k)
            