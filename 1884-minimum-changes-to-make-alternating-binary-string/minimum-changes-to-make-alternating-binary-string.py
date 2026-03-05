class Solution:
    def minOperations(self, s: str) -> int:
        z, o, cnt_z, cnt_o = 0, 1, 0, 0
        for ch in s:
            x = 0 if ch=='0' else 1
            cnt_z += x ^ z
            cnt_o += x ^ o
            z = 1-z
            o = 1-o
        return min(cnt_z, cnt_o)