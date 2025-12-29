class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        totalApples = sum(apple)
        k = 0
        res = 0
        for i in capacity:
            k += i
            res += 1
            if k >= totalApples:
                return res