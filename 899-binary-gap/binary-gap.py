class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        l = None
        for r, d in enumerate(bin(n)[2:]):
            if d == "0":
                continue
            if l != None:
                max_gap = max(max_gap, r-l)
            l = r
        return max_gap