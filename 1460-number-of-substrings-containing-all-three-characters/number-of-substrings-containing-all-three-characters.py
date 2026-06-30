class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res=0
        a=b=c=-1
        for i,ch in enumerate(s):
            if ch=='a':
                a=i
            if ch=='b':
                b=i
            if ch=='c':
                c=i
            res+=min(a,b,c)+1
        return res                
                

        