class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        arr = [s[0]]

        for ch in s[1:]:
            arr.append('#')
            arr.append(ch)

        l = r = 0
        p = [0] * len(arr)

        for i in range(len(arr)):

            if i <= r:
                p[i] = min(p[l + r - i], r - i)

            while (
                i - p[i] - 1 >= 0
                and i + p[i] + 1 < len(arr)
                and arr[i - p[i] - 1] == arr[i + p[i] + 1]
            ):
                p[i] += 1

            if i + p[i] > r:
                r = i + p[i]
                l = i - p[i]

        dp = [0] * (n + 1)

        for i in range(k, n + 1):
            dp[i] = dp[i - 1]

            center = i - k + i - 1

            if p[center] >= k - 1:
                dp[i] = max(dp[i], dp[i - k] + 1)

            if i >= k + 1:
                center = i - k - 1 + i - 1

                if p[center] >= k:
                    dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]