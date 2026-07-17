class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        ans = []

        i = 0 
        j = 0 

        while i < n and j < m :
            ans.append(word1[i])
            ans.append(word2[j])

            i += 1 
            j += 1 

        while i < n :
            ans.append(word1[i])
            i += 1 
        
        while j < m :
            ans.append(word2[j])
            j += 1 
            
        return "".join(ans)