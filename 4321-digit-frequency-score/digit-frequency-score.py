class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        dic = {}

        for i in s :
            if i not in dic :
                dic[i] = 1 
            else:
                dic[i] += 1 
        
        ans = 0 
        for (key,value) in dic.items() :
            ans += (int(key)*int(value))
        return ans         