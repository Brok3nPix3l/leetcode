class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for i, d in enumerate(number):
            if d == digit:
                substring_with_digit_removed = number[0:i] + number[i+1:]
                substring_int = int(substring_with_digit_removed)
                max_num = max(max_num, substring_int)
        return str(max_num)