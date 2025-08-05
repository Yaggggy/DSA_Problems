class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        check = {'a','e','i','o','u'}
        count = 0 

        for i in range(left,right+1):
            if words[i][0] in check and words[i][-1] in check :
                count += 1 
            else:
                continue 
        
        return count