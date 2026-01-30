from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(1 , len(nums)):
            for j in range(i , len(nums)):
                if nums[j] == k - nums[i]:
                    count += 1
        return count 
    
solution = Solution()
nums = [1,2,3,4]
k = 5
k = solution.maxOperations(nums , k)
print(k)