class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        answer = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                answer.append(i)
        return answer