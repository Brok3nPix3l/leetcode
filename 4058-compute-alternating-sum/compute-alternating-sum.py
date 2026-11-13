class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        alt_sum = 0

        for i, num in enumerate(nums):
            if i & 1 == 0:
                alt_sum += num
            else:
                alt_sum -= num

        return alt_sum