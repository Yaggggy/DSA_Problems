class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if (
                a and c and
                all(ch.isalnum() or ch == '_' for ch in c) and
                b in priority
            ):
                valid.append((priority[b], c))

        valid.sort()
        return [c for _, c in valid]

        