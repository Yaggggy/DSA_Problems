class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        i , j = 0 , 0 
        ans = []
        while i < n and j < m :
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1 
            j += 1 

        if i < n :
            ans.append(word1[i:])
        elif j < m :
            ans.append(word2[j:])
        
        return ''.join(ans)

            