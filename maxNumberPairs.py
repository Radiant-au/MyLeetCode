from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        right = len(nums) - 1
        left = 0
        nums.sort()
        while left < right:
            if k == nums[left] + nums[right]:
                left += 1
                right -= 1
                count += 1
            elif k < nums[left] + nums[right]:
                right -= 1
            else:
                left += 1
                 
        return count 
    
    def anotherSolution(self , nums : List[int] , k : int) -> int:
        count = Counter()
        ops = 0

        for x in nums:
            need = k - x
            if count[need] > 0:
                ops += 1
                count[need] -= 1
            else:
                count[x] += 1

        return ops
    
    def anotherCounterSolution(self , nums : List[int] , k : int) -> int:
        c = Counter(nums)
        output = 0
        seen = set()

        for x in c:
            if x not in seen and (k - x) in c:
                if x == (k - x):
                    output += c[x] // 2
                else:
                    output += min(c[x], c[k - x])
                seen.add(x)
                seen.add(k - x)

        return output
    
solution = Solution()
nums = [3,1,3,4,3]
k = 6
k = solution.anotherCounterSolution(nums , k)
print(k)