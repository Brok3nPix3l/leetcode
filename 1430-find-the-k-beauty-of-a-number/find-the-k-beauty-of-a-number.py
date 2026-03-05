class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        return sum((1 if int(num / 10 ** i % 10 ** k) != 0 and num % int(num / 10 ** i % 10 ** k) == 0 else 0) for i in range(len(str(num)) + 1 - k))