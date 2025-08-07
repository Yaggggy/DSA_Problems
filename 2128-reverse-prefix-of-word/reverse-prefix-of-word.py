class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        n = len(word)
        ans = []

        i = 0
        
        while i < n :
            if word[i] == ch :
                ans.append((word[i::-1]))
                ans.append(word[i+1:])
                
                return ''.join(ans)
            else:
                i += 1
        
        return word
        