class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = [0] * k 
        ans[0] = happiness[0]
        for i in range(k):
            if happiness[i] - i > 0 :
                ans[i] = happiness[i]-i 
        return sum(ans)