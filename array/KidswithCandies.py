from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result.append(True)
            else: 
                result.append(False)
        
        return result
    
solution = Solution()
candies = [12,1,12]
extraCandies = 10
k = solution.kidsWithCandies(candies , extraCandies)
print(k)