class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if i.isalnum():
                arr.append(i.lower())
        print(arr)
        l = 0 
        r = len(arr) - 1 

        while l < r :
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1 
        return True