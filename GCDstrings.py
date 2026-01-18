class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        
        def IsDivisor(str):
            if l1 % len(str) and l2 % len(str):
                return False
            f1,f2 = l1 // len(str), l2 // len(str)
            return str * f1 == str1 and str * f2 == str2

        for l in range(min(l1,l2) , 0 , -1):
            if IsDivisor(str1[:l]):
                return str1[:l]
           
        return ""
    
    
str1 = "ABC"
str2 = "ABCDABCD"
solution = Solution()
k = solution.gcdOfStrings(str1, str2)
print(k)
        
    
        