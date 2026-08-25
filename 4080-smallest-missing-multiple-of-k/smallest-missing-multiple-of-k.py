class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashSet = set(nums)
        i = 1 
        while True:
            if i * k not in hashSet:
                return i * k
            else:
                i += 1