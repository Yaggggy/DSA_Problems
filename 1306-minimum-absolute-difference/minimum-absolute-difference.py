class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        sub = float('inf')

        for i in range(1,len(arr)):
            check = arr[i] - arr[i-1]
            if check < sub :
                sub = check 
                ans = [[arr[i-1],arr[i]]]
            elif check == sub :
                ans.append([arr[i-1],arr[i]])
        return ans 