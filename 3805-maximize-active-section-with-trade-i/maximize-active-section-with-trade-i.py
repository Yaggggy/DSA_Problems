class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        prev = tail = 0
        total = s.count("1")
        ans = 0
        hasmidones = False
        for ch in s:
            if ch == "1":
                if tail and hasmidones:
                    prev = tail
                    tail = 0
                elif prev:
                    hasmidones = True
            else:
                if hasmidones:
                    tail += 1
                else:
                    prev += 1

            if prev and tail:
                ans = max(ans, prev + tail)
        
        
        return ans + total
                