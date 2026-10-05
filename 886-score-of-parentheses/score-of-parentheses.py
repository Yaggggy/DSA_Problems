class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, b, p= 0, 0, 0
        for c in s:
            open=c=='('
            b+=(open<<1)-1
            score+=(-(not open) & (p<<b))
            p=open
        return score