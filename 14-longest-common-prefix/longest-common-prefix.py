class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest = float('inf')
        for i in strs :
            if len(i) < smallest :
                smallest = len(i)
        
        i = 0 
        while i < smallest :
            for s in strs :
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1 
        
        return strs[0][:i]
        