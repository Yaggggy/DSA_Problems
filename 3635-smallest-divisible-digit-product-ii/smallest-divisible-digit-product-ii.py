class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        d=Counter()
        t2=t
        for dig in [2,3,5,7]:
            while t2%dig==0:
                t2//=dig
                d[dig]+=1
        if t2 !=1:
            return "-1"
        n=len(num)+47
        ans=["0"]*n
        num1=num.zfill(n)
        MI=[num1,'1'*n]
        @cache
        def dp(i,c2,c3,c5,c7,mi_=0,lead_zero=True):
            if lead_zero:
                p=1
            mi=MI[mi_]
            if i == n:
                return c2==0 and c3==0 and c5==0 and c7==0
            cur_min=int(mi[i])
            for dig in range(max(0 if lead_zero else 1,cur_min), 10):
                ans[i]=str(dig)
                next_mi_ = mi_!=0 or dig != cur_min
                p=dig
                nc2=c2
                while nc2>0 and p>0 and p%2==0:
                    p//=2
                    nc2-=1
                nc3=c3
                while nc3>0 and  p>0 and  p%3==0:
                    p//=3
                    nc3-=1
                nc5=c5
                while nc5>0 and p>0 and  p%5==0:
                    p//=5
                    nc5-=1
                nc7=c7
                while nc7>0 and p>0 and  p%7==0:
                    p//=7
                    nc7-=1
                if dp(i + 1, nc2, nc3, nc5, nc7, next_mi_, dig==0):
                    return True
            return False
        dp(0,d[2],d[3],d[5],d[7])
        dp.cache_clear()
        ans2=[]
        for x in ans:
            if x!='0':
                ans2.append(x)
        return ''.join(ans2)
