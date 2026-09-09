class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        ans = n - 999

        if n >= 1000000:
            ans += n - 999999

        if n >= 1000000000:
            ans += n - 999999999

        if n >= 1000000000000:
            ans += n - 999999999999

        if n >= 1000000000000000:
            ans += n - 999999999999999

        return ans