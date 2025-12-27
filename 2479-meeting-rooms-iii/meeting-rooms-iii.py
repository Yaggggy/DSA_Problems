class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        count = [0] * n 
        freeRoom = list(range(n))
        heapq.heapify(freeRoom)
        used = []
        for start, end in meetings:
            while used and used[0] and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(freeRoom, room)
            dur = end - start
            if freeRoom:
                room = heapq.heappop(freeRoom)
                begin = start
            else:
                
                delay, room = heapq.heappop(used)
                begin = delay
            count[room] += 1
            heapq.heappush(used, (begin + dur, room))
        maxCount = max(count)
        for i in range(n):
            if count[i] == maxCount:
                return i
