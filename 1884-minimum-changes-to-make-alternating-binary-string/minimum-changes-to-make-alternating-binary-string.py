class Solution:
    def minOperations(self, s: str) -> int:
        ops = [0, 0]
        for i, d in enumerate(s):
            if int(d) == i % 2:
                ops[1] += 1
            else:
                ops[0] += 1
        return min(ops)