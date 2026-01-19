from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                checkleft = (i == 0) or flowerbed[i - 1] == 0
                checkright = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

                if checkleft and checkright:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n


solution = Solution()
flowerbed = [1, 0, 0, 0, 1, 0, 0, 0, 0]
n = 3
k = solution.canPlaceFlowers(flowerbed, n)
print(k)
