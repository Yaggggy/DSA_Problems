class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0]*(n+1)
        dp[0] = 1

        pref = [0]*(n+1)
        pref[0] = dp[0]

        min_dp = deque()
        max_dp = deque()

        l = 0
        for r in range(n):
            while max_dp and nums[max_dp[-1]]<=nums[r]:
                max_dp.pop()
            max_dp.append(r)

            while min_dp and nums[min_dp[-1]] > nums[r]:
                min_dp.pop()
            min_dp.append(r)

            while nums[max_dp[0]] - nums[min_dp[0]] > k:
                if max_dp[0] == l:
                    max_dp.popleft()
                if min_dp[0] == l:
                    min_dp.popleft()
                l+=1 
            if l == 0:
                total = pref[r]
            else:
                total = (pref[r] - pref[l - 1]) % MOD
            dp[r+1] = total
            pref[r+1] = (pref[r] + dp[r+1])%MOD
        return dp[n]%MOD