class Solution:
    reverseDegreeDict = {chr(code): (26 - (code - ord('a'))) for code in range(ord('a'), ord('z') + 1)}

    def reverseDegree(self, s: str) -> int:
        return sum(self.reverseDegreeDict[c] * (i + 1) for i, c in enumerate(s))