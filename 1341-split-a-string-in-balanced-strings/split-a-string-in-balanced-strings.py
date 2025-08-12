class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, r_l = 0, 0
        
        for c in s:
            if c == 'L':
                r_l -= 1
            elif c == 'R':
                r_l += 1
            if r_l == 0:
                count += 1

        return count