class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        used = [0] * n

        avail = list(range(n))
        heapify(avail)
        busy = []
        heapify(busy)

        for start, end in meetings:
            while busy and busy[0] and busy[0][0] <= start:
                _,room = heappop(busy)
                heappush(avail,room)
            
            if avail:
                room = heappop(avail)
                heappush(busy,(end,room))
                used[room] +=1
            else:
                dur= end-start
                endTime,room = heappop(busy)
                heappush(busy,(endTime+dur,room))
                used[room]+=1
        maxRoom = 0
        maxCount = 0
        for i in range(n):
            if used[i] > maxCount:
                maxCount = used[i]
                maxRoom = i 
        return maxRoom