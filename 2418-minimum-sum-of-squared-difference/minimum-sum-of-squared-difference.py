class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        remaining = k - sum(
            max(0, d - threshold) for d in diff
        )

        result = 0

        for d in diff:
            d = min(d, threshold)

            if d == threshold and remaining > 0:
                d -= 1
                remaining -= 1

            result += d * d

        return result