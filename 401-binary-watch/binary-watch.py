class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        return [f'{q>>6}:{q&63:02d}' for q in range(1024) 
            if q.bit_count()==n and q>>6<12 and q&63<60]