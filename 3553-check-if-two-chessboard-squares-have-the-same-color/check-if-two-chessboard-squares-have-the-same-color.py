class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1, n1 = ord(coordinate1[0]), ord(coordinate1[1])
        c2, n2 = ord(coordinate2[0]), ord(coordinate2[1])

        return not ((abs(c1 - c2) & 1 == 0) ^ (abs(n1 - n2) & 1 == 0))