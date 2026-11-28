class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        free = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                free[f] += freq[j]
            free[f] -= 1

        items.sort(key=lambda x: x[1])
        m = items[0][1]
        ans = 0

        for f, p in items:
            if p > 2 * m:
                break

            k = min(free[f], budget // p)
            ans += 2 * k
            budget -= k * p

            if k < free[f]:
                break

        return ans + budget // m