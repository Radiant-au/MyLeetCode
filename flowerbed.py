from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 1
        count = 0
        for i in range(0 , len(flowerbed) , k):
            if flowerbed[i]:
                k += 2
            else:
                count += 1
                k += 1
        
        return count == n
    
solution = Solution()
flowerbed = [1,0,0,0,1]
n = 1
k = solution.canPlaceFlowers(flowerbed , n)
print(k)