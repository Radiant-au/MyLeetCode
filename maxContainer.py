from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        max_water = 0
        max_height = 0
        while left < right: 
            row = right - left
            if height[left] < height[right]:
                max_height = height[left]
                left += 1
                water = row * max_height
            else:
                max_height = height[right]
                water = row * max_height
                right -= 1
            
            if water > max_water:
                    max_water = water
        return max_water
    
solution = Solution()
height = [0,2]
k = solution.maxArea(height)
print(k)      