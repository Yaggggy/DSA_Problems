class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total
                if total < target:
                    left+=1
                elif total > target:
                    right-=1
                else:
                    break

        return closest_sum

