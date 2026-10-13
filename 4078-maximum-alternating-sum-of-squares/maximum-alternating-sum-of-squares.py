from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        values = sorted((x * x for x in nums), reverse=True)
        half = (len(values) + 1) // 2

        return sum(values[:half]) - sum(values[half:])