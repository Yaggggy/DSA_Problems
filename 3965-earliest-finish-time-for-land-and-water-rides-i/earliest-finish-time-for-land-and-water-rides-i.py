class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solving (start1, start2, duration1, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
            finish2 = inf
            for j in range(len(start2)):
                finish2 = min(finish2, max(finish1, start2[j]) + duration2[j])
            return finish2
        
        landwater = solving(landStartTime, waterStartTime, landDuration, waterDuration)
        waterland = solving(waterStartTime, landStartTime, waterDuration, landDuration)

        return min(landwater,waterland)