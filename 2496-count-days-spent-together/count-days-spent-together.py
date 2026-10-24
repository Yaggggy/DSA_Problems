class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a1 = self.convert(arriveAlice)
        a2 = self.convert(leaveAlice)
        b1 = self.convert(arriveBob)
        b2 = self.convert(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)

    def convert(self, date: str) -> int:
        length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = int(date[3:])
        months = int(date[0:2])

        total = days
        for i in range(months - 1):
            total += length[i]

        return total