class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0 

        for i in range(n-1):
            for j in range(i+1,n):
                if sorted(words[i]) == sorted(words[j]) :
                    count += 1 
        
        return count 
        