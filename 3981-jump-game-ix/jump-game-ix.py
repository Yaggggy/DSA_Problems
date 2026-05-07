class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        
        suffix = [inf]
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(min(suffix[-1], nums[i]))
        
        suffix = (suffix[::-1])

        heap = []
        ans = [0] * len(nums)
        mx = 0
        for i in range(len(nums)):
            heapq.heappush(heap, (i))
            mx = max(mx, nums[i])
            while heap and mx <= suffix[i + 1]:
                ans[heapq.heappop(heap)] = mx
        
        return (ans)