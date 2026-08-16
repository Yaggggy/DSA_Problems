class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count_mod = [0, 0, 0]
        for stone in stones:
            count_mod[stone % 3] += 1
        if count_mod[0] % 2 == 0:
            return count_mod[1] > 0 and count_mod[2] > 0
        return abs(count_mod[1] - count_mod[2]) > 2 or count_mod[0] % 2 == 0