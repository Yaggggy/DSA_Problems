class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        arr = []
        for i in range(left,right+1):
            arr.append(bin(i)[2:])
        ans = 0 
        for (i) in arr :
            i = str(i)
            count = i.count('1')
            if count in [2, 3, 5, 7, 11, 13, 17 , 19] :
                ans += 1 
        return ans 