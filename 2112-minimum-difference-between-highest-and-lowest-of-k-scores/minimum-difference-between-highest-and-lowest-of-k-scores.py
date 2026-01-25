import math

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        min_diff = math.inf
        for r in range(len(nums)):
            if r - l + 1 == k:
                min_diff = min(min_diff, nums[r] - nums[l])
                l += 1
        
        return min_diff