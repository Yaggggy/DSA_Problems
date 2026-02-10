class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        best = 0
        balance = tuple([set(), set()])
        while len(nums) > best:
            balance[0].clear(); balance[1].clear()
            for r, x in enumerate(reversed(nums), start=1):
                balance[x & 1].add(x)
                if len(balance[0]) == len(balance[1]):
                    best = max(best, r)
            nums.pop()
        return best