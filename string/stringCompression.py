from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0 
        write = 0 
        n = len(chars)
        while read < n:
            char = chars[read]
            count = 0
             
            while read < n and chars[read]  == char:
                 read += 1
                 count += 1
                 
            chars[write] = char
            write += 1
            
            if count > 1:
                for i in str(count):
                    chars[write] = i 
                    write += 1
                    
        return write
    
solution = Solution()
chars = ["a","a","b","b","c","c","c"]
k = solution.compress(chars)
print(k)
    