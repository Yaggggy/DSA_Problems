class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        White = 0
        n = len(blocks)

       
        for j in range(k):
            if blocks[j] == 'W':
                White += 1
        ans = White

      
        for j in range(k, n):
            if blocks[j] == 'W':
                White += 1 
            if blocks[j - k] == 'W':
                White -= 1  
            ans = min(ans, White)

        return ans