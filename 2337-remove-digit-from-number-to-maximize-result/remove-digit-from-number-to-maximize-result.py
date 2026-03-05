class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for i, d in enumerate(number):
            if d == digit:
                max_num = max(max_num, int(number[0:i] + number[i+1:]))
        return str(max_num)