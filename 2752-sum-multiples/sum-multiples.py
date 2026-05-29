class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            for d in [3, 5, 7]:
                if num % d == 0:
                    ans += num
                    break
        return ans