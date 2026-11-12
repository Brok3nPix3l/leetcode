class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if all(num == nums[0] for num in nums) else 1