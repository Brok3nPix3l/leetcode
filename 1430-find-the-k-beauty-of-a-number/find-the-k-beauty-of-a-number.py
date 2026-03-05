class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        for i in range(len(str(num)) + 1 - k):
            cur = int(num / 10 ** i % 10 ** k)
            if cur == 0:
                continue
            if num % cur == 0:
                ans += 1
        return ans