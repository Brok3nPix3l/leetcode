from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if len(Counter(nums)) == 1 else 1