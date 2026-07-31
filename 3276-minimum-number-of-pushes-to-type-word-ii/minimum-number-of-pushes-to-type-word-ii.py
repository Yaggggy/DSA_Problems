class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        ans = 0

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        frequency = sorted(freq.values(), reverse=True)

        for i, f in enumerate(frequency):
            pushes = (i // 8) + 1
            ans += pushes * f

        return ans