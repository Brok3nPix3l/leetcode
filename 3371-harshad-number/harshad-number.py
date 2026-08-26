class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumOfDigits = sum(int(c) for c in str(x))
        return sumOfDigits if x % sumOfDigits == 0 else -1