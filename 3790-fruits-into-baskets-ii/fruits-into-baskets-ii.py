class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for fruit in fruits:
            for basket in baskets:
                if basket >= fruit:
                    count += 1
                    baskets.remove(basket)
                    break

        return len(fruits) - count
        