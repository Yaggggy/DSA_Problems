class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h = len(hBars)
        v = len(vBars)
        hBars.sort()
        vBars.sort()

        def find_continuous_chunk(nums) -> list:
            if not nums:
                print("warning: empty inputs")
                return []
            counts = 1
            res = 0
            n = len(nums)
            for i in range(n-1):
                if nums[i] == nums[i+1] - 1:
                    counts += 1
                    res = max(res, counts)
                else:
                    counts = 1
            return max(res, counts)
        
        hcounts = find_continuous_chunk(hBars)
        vcounts = find_continuous_chunk(vBars)
        return (min(vcounts, hcounts)+1) ** 2