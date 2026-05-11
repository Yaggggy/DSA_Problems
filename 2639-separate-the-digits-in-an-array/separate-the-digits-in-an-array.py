class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            s = str(i)
            for x in s:
                output.append(int(x))
        return output