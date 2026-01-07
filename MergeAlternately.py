class Solution:
    def MyMergeAlternately(self, word1: str, word2: str) -> str:
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
    
    def BestMergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return "".join(result)


solution = Solution()
k = solution.BestMergeAlternately("abcd","pq")
print(f"Length of array after merged: {k}")
            
        
