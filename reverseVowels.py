class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        vowels = set("aeiouAEIOU")
        pointer_left = 0
        pointer_right = len(s) - 1
        while pointer_left < pointer_right:
            if arr[pointer_left] in vowels:
                if arr[pointer_right] in vowels:
                    temp = arr[pointer_left]
                    arr[pointer_left] = arr[pointer_right]
                    arr[pointer_right] = temp
                    pointer_left += 1 
                    pointer_right -= 1
                else:
                    pointer_right -= 1
            else:
                pointer_left += 1
                    
        return ''.join(arr)
    
solution = Solution()
s = "ai"
k = solution.reverseVowels(s)
print(k)