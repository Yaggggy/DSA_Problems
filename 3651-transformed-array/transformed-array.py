class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] == 0 :
                ans.append(0)
            elif nums[i] > 0 :
                right = (i + nums[i]) % n
                ans.append(nums[right])
            else :
                left = i - (abs(nums[i])%n)
                ans.append(nums[left])
        return ans  