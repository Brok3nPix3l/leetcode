class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return str(max((int(number[0:i] + number[i+1:]) if d == digit else 0) for i, d in enumerate(number)))