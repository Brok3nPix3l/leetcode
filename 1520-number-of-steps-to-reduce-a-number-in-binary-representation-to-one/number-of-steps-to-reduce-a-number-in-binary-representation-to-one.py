class Solution:
    def numSteps(self, s: str) -> int:
        i = int(s, 2)
        steps = 0
        while i != 1:
            if i & 1 == 0:
                i >>= 1
            else:
                i += 1
            steps += 1
        return steps