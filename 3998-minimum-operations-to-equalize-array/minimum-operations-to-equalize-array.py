class Solution:
    def minOperations(self, nums: List[int]) -> int:
        it = iter(nums)
        first = next(it)
        return 0 if all(num == first for num in it) else 1