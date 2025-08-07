class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ans = [''] * n
        
        for i in range(n) :
            ans[i] = s[indices.index(i)]

        return ''.join(ans)        