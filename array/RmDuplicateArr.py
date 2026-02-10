from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
            else:
                continue
                
        return k

# Example usage:
nums = [1, 1, 2, 2, 3]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Length of array after removing duplicates: {k}")