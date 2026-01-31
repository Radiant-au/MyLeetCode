from typing import List


class Solution:
    def fixedSizeSlidingWindow(self, nums: List[int], k: int) -> int:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]        # add right
            window_sum -= nums[i - k]    # remove left
            max_sum = max(max_sum, window_sum)

        return max_sum
    
    def variableSizeSlidingWindow(self, s: str) -> int:
        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans
    
nums = [2,1,5,1,3,2]
k = 3
s = "abcabdcbb"
solution = Solution()
print(solution.variableSizeSlidingWindow(s))  # Output: 9