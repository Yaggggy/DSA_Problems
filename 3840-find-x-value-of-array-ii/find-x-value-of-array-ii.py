from typing import List

class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1, nums)

    def _build(self, node: int, lo: int, hi: int, nums: List[int]):
        if lo == hi:
            p = nums[lo] % self.k
            count = [0] * self.k
            count[p] = 1
            self.tree[node] = (p, count)
        else:
            mid = (lo + hi) // 2
            self._build(node * 2, lo, mid, nums)
            self._build(node * 2 + 1, mid + 1, hi, nums)
            self.tree[node] = self._merge(self.tree[node * 2],
                                         self.tree[node * 2 + 1])

    def _merge(self, left: tuple, right: tuple) -> tuple:
        prod_L, count_L = left
        prod_R, count_R = right
        prod = (prod_L * prod_R) % self.k

        count = count_L.copy()
        for r in range(self.k):
            count[(prod_L * r) % self.k] += count_R[r]

        return (prod, count)

    def _update(self, node: int, lo: int, hi: int, idx: int, val: int):
        if lo == hi:
            p = val % self.k
            count = [0] * self.k
            count[p] = 1
            self.tree[node] = (p, count)
        else:
            mid = (lo + hi) // 2
            if idx <= mid:
                self._update(node * 2, lo, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, hi, idx, val)
            self.tree[node] = self._merge(self.tree[node * 2],
                                         self.tree[node * 2 + 1])

    def update(self, idx: int, val: int):
        self._update(1, 0, self.n - 1, idx, val)

    def _query(self, node: int, lo: int, hi: int, L: int, R: int) -> tuple:
        if R < lo or hi < L:
            return (1 % self.k, [0] * self.k)
        if L <= lo and hi <= R:
            return self.tree[node]
        mid = (lo + hi) // 2
        left = self._query(node * 2, lo, mid, L, R)
        right = self._query(node * 2 + 1, mid + 1, hi, L, R)
        return self._merge(left, right)

    def query_suffix(self, start: int) -> List[int]:
        return self._query(1, 0, self.n - 1, start, self.n - 1)[1]


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:
        st = SegTree(nums, k)
        ans = []
        for idx, val, start, x in queries:
            st.update(idx, val)
            count_array = st.query_suffix(start)
            ans.append(count_array[x])
        return ans