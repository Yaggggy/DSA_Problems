class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        ord_a = ord("a")
        s = [ord(c) - ord_a for c in s]
        t = [ord(c) - ord_a for c in target]

        cnt = [0] * 26
        for x in s:
            cnt[x] += 1
        
        i = 0
        while i < n and cnt[t[i]] > 0:
            cnt[t[i]] -= 1
            i += 1
        if i == n:
            i -= 1
            cnt[t[i]] += 1
        
        mx = max(i for i in range(26) if cnt[i] > 0)
        while i >= 0:
            if mx > t[i]:
                first = t[i] + 1
                while cnt[first] == 0:
                    first += 1

                ans = [target[: i], chr(first + ord_a)]
                cnt[first] -= 1

                for x in range(26):
                    if cnt[x] == 0:
                        continue
                    ans.append(cnt[x] * chr(x + ord_a))
                
                return "".join(ans)
            
            i -= 1
            if i >= 0:
                cnt[t[i]] += 1
                mx = max(mx, t[i])
        
        return ""