class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        minn = min(n,m)
        ans = []
        for i in range(minn):
            ans.append(word1[i])
            ans.append(word2[i])
        if n == minn :
            ans.append(word2[i+1:m])
        elif m == minn:
            ans.append(word1[i+1:n])

        return ''.join(ans)

            