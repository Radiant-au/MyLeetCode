class Solution:
    def reverseWords(self, s: str):
        arr = s.split()
        rev = arr[::-1]
        return ' '.join(rev)
    
solution = Solution()
st = "The sky is blue"
k = solution.reverseWords(st)
print(k)
