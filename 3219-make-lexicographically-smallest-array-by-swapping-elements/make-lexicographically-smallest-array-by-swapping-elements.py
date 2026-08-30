class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        pairs = [(nums[i], i) for i in range(n)]
        pairs.sort()

        l = 0

        while l < n:
            r = l + 1

            while r < n and pairs[r][0] - pairs[r - 1][0] <= limit:
                r += 1

            group = []

            for i in range(l, r):
                group.append(pairs[i][1])

            group.sort()

            for i in range(len(group)):
                nums[group[i]] = pairs[l + i][0]

            l = r

        return nums