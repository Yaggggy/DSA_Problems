class Solution:
    def checkString(self, s: str) -> bool:
        check = None 
        for i in s :
            if i == 'a' and not check :
                continue 
            elif i == 'a' and check == 'b':
                return False 
            else:
                check = 'b'
        return True         
