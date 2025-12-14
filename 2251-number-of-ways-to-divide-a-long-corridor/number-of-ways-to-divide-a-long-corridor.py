class Solution:
    def numberOfWays(self, s: str) -> int:
        if (q:=s.count('S'))==0 or q%2: return 0
        return prod(len(m[1])+1 for m in finditer(r'(?<=S)P*S(P*)S',s))%(10**9+7)