class Solution:
    def romanToInt(self, s: str) -> int:
        rule = {'I':1, 'V':5 , 'X':10 , 'L' : 50 , 'C': 100 , 'D': 500 , 'M': 1000}
        n = len(s)
        ans = 0 
        for i in range(n-1):
            if rule[s[i]] < rule[s[i+1]]:
                ans -= rule[s[i]]
            else:
                ans += rule[s[i]]
        return ans + rule[s[n-1]]