class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        
        for i, row in enumerate(mat):
            shift = k if i % 2 == 0 else -k
            for j in range(n):
                if row[j] != row[(j + shift) % n]:
                    return False
        return True