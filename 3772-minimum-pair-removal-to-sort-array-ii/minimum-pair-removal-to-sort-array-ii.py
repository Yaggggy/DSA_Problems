class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        prev = [i-1 for i in range(len(nums))]
        next = [i+1 for i in range(len(nums))]
        prev.append(len(nums) - 1)
        next[-1] = -1
        next.append(0)
        q = []
        bad = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                bad += 1
            heappush(q, (nums[i-1] + nums[i], i))
        ans = 0
        while bad:
            # print(ans, bad, nums, q)
            sum, r = heappop(q)
            l = prev[r]
            if l == -1 or nums[l] + nums[r] != sum:
                continue
            next[l] = next[r]
            prev[next[r]] = l
            if nums[l] > nums[r]:
                bad -= 1
            ll = prev[l]
            rr = next[r]
            if ll != -1:
                bad += (nums[ll] > sum) - (nums[ll] > nums[l])
                heappush(q, (nums[ll] + sum, l))
            if rr != -1:
                bad += (sum > nums[rr]) - (nums[r] > nums[rr])
                heappush(q, (nums[rr] + sum, rr))
            nums[l] = sum
            nums[r] = inf
            ans += 1
        return ans
            