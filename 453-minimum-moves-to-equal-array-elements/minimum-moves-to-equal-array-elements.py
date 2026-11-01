class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num = min(nums)

        diff = [num - min_num for num in nums]

        return sum(diff)