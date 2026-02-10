from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
    def anotherSol(self, nums: List[int], k: int) -> int:
        available_zeros = k
        left = 0
        cur_window_len = 0
        max_window_len = 0

        for n in nums:
            if n == 1:
                cur_window_len += 1
            elif available_zeros > 0:
                cur_window_len += 1
                available_zeros -= 1
            else:
                if max_window_len < cur_window_len:
                    max_window_len = cur_window_len
                while nums[left] == 1:
                    left += 1
                    cur_window_len -= 1
                left += 1

        if max_window_len < cur_window_len:
            max_window_len = cur_window_len

        return max_window_len

                
solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(solution.longestOnes(nums,k))