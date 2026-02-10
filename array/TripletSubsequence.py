from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else: 
                return True
        return False
    
solution = Solution()
nums = [9,6,5,0,8,6]
k = solution.increasingTriplet(nums)
print(k)
                
                