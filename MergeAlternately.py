class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        output=''
        i = 0 
        while(i<length): 
            output += word1[i]
            output += word2[i]
            i+=1
            
        if i < len(word1):
            output+=word1[i:len(word1)]
        elif i < len(word2):
            output+=word2[i:len(word2)]
            
        return output


solution = Solution()
k = solution.mergeAlternately("abcd","pq")
print(f"Length of array after merged: {k}")
            
        
