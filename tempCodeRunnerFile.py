
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(0 , len(flowerbed) , 2):
            if flowerbed[i]:
                continue
            else:
                count += 1
                
        return count == n
    
solution = Solution()
flowerbed = [0,0,1,0,0]
n = 2