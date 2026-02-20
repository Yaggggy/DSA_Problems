class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        subs = []

        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                middle = s[start + 1:i]
                subs.append('1' + self.makeLargestSpecial(middle) + '0')
                start = i + 1

        subs.sort(reverse=True)
        return ''.join(subs)