class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], 
                    changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        
        # Build string-to-ID mapping
        string_to_id = {}
        lens = set()
        
        for s in original + changed:
            if s not in string_to_id:
                string_to_id[s] = len(string_to_id)
                lens.add(len(s))
        
        # Initialize distance matrix
        sz = len(string_to_id)
        D = [[INF] * sz for _ in range(sz)]
        
        for i in range(sz):
            D[i][i] = 0
        
        # Build graph with minimum cost edges
        for o, c, w in zip(original, changed, cost):
            u = string_to_id[o]
            v = string_to_id[c]
            D[u][v] = min(D[u][v], w)
        
        # Floyd-Warshall: all-pairs shortest paths
        for k in range(sz):
            for i in range(sz):
                if D[i][k] < INF:
                    for j in range(sz):
                        if D[k][j] < INF:
                            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        
        # DP: dp[i] = min cost to convert source[0:i] to target[0:i]
        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] >= INF:
                continue
            
            # No transformation needed
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            # Try substring transformations
            for length in lens:
                j = i + length
                if j > n:
                    continue
                
                s_sub = source[i:j]
                t_sub = target[i:j]
                
                if s_sub in string_to_id and t_sub in string_to_id:
                    u = string_to_id[s_sub]
                    v = string_to_id[t_sub]
                    if D[u][v] < INF:
                        dp[j] = min(dp[j], dp[i] + D[u][v])
        
        return dp[n] if dp[n] < INF else -1