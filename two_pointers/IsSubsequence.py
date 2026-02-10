class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0:
            return True
        p1 = 0
        count = len(s) 
        for i in range(len(t)):
            if t[i] == s[p1]:
                p1 += 1
                if (p1 == count):
                    return True
            
        return False
    
solution = Solution() 
s = ""  
t = "ahbgdc"
k = solution.isSubsequence(s,t)
print(k)