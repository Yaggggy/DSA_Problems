class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt = 0
        lst = []
        for i in nums:
            if i == target:lst.append(1)
            else:lst.append(-1)
        prefix = [0]
        running_total = 0
        for score in lst:
            running_total += score 
            prefix.append(running_total)
        n = len(prefix)
        for i in range(n):
            for j in range(i+1,n):
                if prefix[j] > prefix[i]:cnt += 1
        return cnt