class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        values = defaultdict(int)
        for i, (r, c) in enumerate(cells):
            values[(r, c)] = -i
        pq = []
        visited = set()
        for i in range(1, col + 1):
            pq.append((values[(1, i)], 1, i))
            visited.add((1, i))
        heapq.heapify(pq)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        res = float('inf')
        while pq:
            val, r, c = heapq.heappop(pq)
            res = min(res, -val)
            if r == row:
                return res
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newR > row or newC <= 0 or newC > col:
                    continue
                if (newR, newC) in visited:
                    continue
                visited.add((newR, newC))
                heapq.heappush(pq, (values[(newR, newC)], newR, newC))
        return res
                

        