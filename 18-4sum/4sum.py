class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target: continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target: break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target: continue
                
                k, l = j + 1, n - 1
                while k < l:
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k+1]: k += 1
                        while k < l and nums[l] == nums[l-1]: l -= 1
                        k += 1
                        l -= 1
                    elif curr_sum < target:
                        k += 1
                    else:
                        l -= 1
        return res