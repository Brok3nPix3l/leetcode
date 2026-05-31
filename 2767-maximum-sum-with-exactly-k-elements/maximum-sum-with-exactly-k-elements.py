class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = max(nums)
        return int((((n + k - 1) * (n + k)) / 2) - (((n - 1) * n) / 2))