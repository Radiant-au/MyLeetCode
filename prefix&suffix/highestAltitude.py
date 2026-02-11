from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
            n = len(gain)
            prefix = [0] * (n + 1)
            prefix[0] = 0
            for i in range(n):
                prefix[i + 1] = prefix[i] + gain[i]
                
            return max(prefix)
        
solution = Solution()
gain = [-5,1,5,0,-7]
print(solution.largestAltitude(gain))