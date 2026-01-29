ctoi = lambda c: ord(c) - ord('a')
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = [[float('inf')]*26 for _ in range(26)]
        for u,v,w in zip(original, changed, cost):
            adj[ctoi(u)][ctoi(v)] = min(adj[ctoi(u)][ctoi(v)],w)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if adj[i][k] != float('inf') and adj[k][j] != float('inf'):
                        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        
        res = 0
        for a,b in zip(source,target):
            if a == b: continue
            v = adj[ctoi(a)][ctoi(b)]
            if v == float('inf'): return -1
            res += v
        return res