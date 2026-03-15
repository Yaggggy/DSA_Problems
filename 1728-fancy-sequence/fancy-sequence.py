MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.raw = []
        self.mult = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv = pow(self.mult, MOD-2, MOD)
        base = (val - self.add) * inv % MOD
        self.raw.append(base)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mult = self.mult * m % MOD
        self.add = self.add * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.raw):
            return -1
        return (self.raw[idx] * self.mult + self.add) % MOD