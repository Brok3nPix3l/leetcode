class Solution:
    def minOperations(self, s: str) -> int:
        arr = [int(d) for d in s]
        ops = [0, 0]
        for i, d in enumerate(arr):
            if d == i % 2:
                ops[1] += 1
            else:
                ops[0] += 1
        return min(ops)