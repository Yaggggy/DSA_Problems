class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lessThanEqual = 0
        onlyLess = 0
        for i in nums:
            if i <= target:
                lessThanEqual += 1
            if i < target:
                onlyLess += 1
        return list(range(onlyLess, lessThanEqual))