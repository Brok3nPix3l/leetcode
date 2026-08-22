class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitProduct = 1
        for c in str(n):
            d = int(c)
            digitSum += d
            digitProduct *= d
        combined = digitSum + digitProduct
        return n >= combined and n % combined == 0