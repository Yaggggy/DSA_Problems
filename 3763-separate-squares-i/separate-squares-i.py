class Solution:
    def separateSquares(self, squares: List[List[int]], margin = 1e-5) -> float:
        bot = top = totalArea = 0
        for _, y, l in squares:
            totalArea += l * l
            top = max(top, y + l)
        halfArea = totalArea / 2
        while top - bot > margin:
            m = (top + bot) / 2
            botArea = sum(max(0, min(m - y, l)) * l for _, y, l in squares)
            if botArea >= halfArea:
                top = m
            else:
                bot = m
        return top