class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        p1 = str(num1).zfill(4)
        p2 = str(num2).zfill(4)
        p3 = str(num3).zfill(4)

        return int("".join(min(p1[i], p2[i], p3[i]) for i in range(4)))