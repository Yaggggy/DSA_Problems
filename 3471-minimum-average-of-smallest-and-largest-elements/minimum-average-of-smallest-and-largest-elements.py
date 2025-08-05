class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []

        for i in range(len(nums)//2):
            a = max(nums)
            b = min(nums)
            nums.remove(a)
            nums.remove(b)
            averages.append((a+b)/2)

        return min(averages)

        