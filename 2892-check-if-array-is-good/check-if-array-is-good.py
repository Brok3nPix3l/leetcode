from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        expected = Counter(n for n in range(1, len(nums)))
        expected[len(nums) - 1] += 1
        # print(f'expected={expected}')
        actual = Counter(nums)
        # print(f'actual={actual}')
        return actual == expected