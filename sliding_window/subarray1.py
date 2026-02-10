from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_len = 0
        zero_count = 0
        left = 0 
        
        for right in range(len(nums)):
            zero_count += (nums[right] == 0)
            
            while zero_count > 1:
                zero_count -= (nums[left] == 0)
                left += 1
            
            max_len = max(max_len , right - left)
            
        return max_len
    
solution = Solution()
nums = [0,1,1,1,0,1,1,0,1]
print(solution.longestSubarray(nums))