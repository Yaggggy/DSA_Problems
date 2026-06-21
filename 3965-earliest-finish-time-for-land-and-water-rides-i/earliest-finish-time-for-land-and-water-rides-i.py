class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime )):
                s = landStartTime[i] + landDuration[i]
                m = max(s,waterStartTime[j]) + waterDuration[j]
                s1 = waterStartTime[j] + waterDuration[j]
                m1 = max(s1,landStartTime[i]) + landDuration[i]
                ans = min(ans,m,m1)
        return ans 