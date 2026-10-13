import numpy as np

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # if n is even, there are an equal number of positive and negative numbers
        # if n is odd, the middle number is positive

        k = len(nums) // 2
        nums = np.partition([n ** 2 for n in nums], k)

        return int(sum(num for num in nums[k:]) - sum(num for num in nums[:k]))