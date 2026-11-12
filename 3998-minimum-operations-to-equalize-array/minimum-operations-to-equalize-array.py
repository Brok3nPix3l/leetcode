class Solution:
    def minOperations(self, nums: List[int]) -> int:
        first = nums[0]
        return 0 if all(num == first for num in nums[1:]) else 1