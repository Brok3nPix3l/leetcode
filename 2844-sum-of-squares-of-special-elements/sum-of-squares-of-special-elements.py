import math

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                ans += nums[i - 1] ** 2
                other = n // i
                if i != other:
                    ans += nums[other - 1] ** 2
        return ans