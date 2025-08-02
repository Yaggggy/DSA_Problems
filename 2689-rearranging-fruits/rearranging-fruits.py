class Solution:
    def minCost(self, basket1, basket2):
        count = Counter()
        global_min = float('inf')

     
        for x in basket1:
            count[x] += 1
            global_min = min(global_min, x)
        for x in basket2:
            count[x] -= 1
            global_min = min(global_min, x)

        total = 0

        for v in count.values():
            if v % 2 != 0:
                return -1 
         
        im = []
        for num, v in count.items():
            im.extend([num] * (abs(v) // 2))

        im.sort()

        half = len(im) // 2
        double_min = 2 * global_min
        ans = sum(min(im[i], double_min) for i in range(half))

        return ans 