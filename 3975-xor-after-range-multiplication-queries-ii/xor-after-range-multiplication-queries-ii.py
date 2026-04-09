class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        n = len(nums)
        limit = int(n ** 0.5) + 1

        small_k = defaultdict(list)
        for q in queries:            
            if q[2] >= limit:
                for i in range(q[0], q[1] + 1, q[2]):
                    nums[i] = (nums[i] * q[3]) % MOD
            else:                
                small_k[q[2]].append(q)
                
        for k, query_list in small_k.items():
            diff = [1] * n
            for q in query_list:
                diff[q[0]] = (diff[q[0]] * q[3]) % MOD
                steps = (q[1] - q[0]) // k
                nxt = q[0] + (steps + 1) * k
                if nxt < n:
                    diff[nxt] = (diff[nxt] * pow(q[3], -1, MOD)) % MOD
                    
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                nums[i] = (nums[i] * diff[i]) % MOD
                
        return reduce(operator.xor,nums)