class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans = [], []
        k = 0
        for x in nums:
            if x == -1:
                k += 1
                ans.append(seen[-k] if k <= len(seen) else -1)
            else:
                seen.append(x)
                k = 0
        return ans