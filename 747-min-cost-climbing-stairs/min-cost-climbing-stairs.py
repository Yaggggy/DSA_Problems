class Solution:
    def minCostClimbingStairs(self, arr: List[int]) -> int:
        arr.append(0)
        for i in range(len(arr)-3,-1,-1):
            arr[i] = min(arr[i+1]+arr[i],arr[i]+arr[i+2])
        return min(arr[0],arr[1])
        

        