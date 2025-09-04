class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dis1 = abs(z-x)
        dis2 = abs(z-y)

        if dis1 < dis2 :
            return 1 
        elif dis1 > dis2 :
            return 2 
        else:
            return 0