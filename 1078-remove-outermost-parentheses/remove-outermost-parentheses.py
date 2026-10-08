class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        start = opens = closes = 0
        pieces = []
        for end, char in enumerate(s):
            if char == '(':
                opens += 1
            else:
                closes += 1
            if opens == closes:
                pieces.append(s[start + 1:end])
                start = end + 1
        return ''.join(pieces)