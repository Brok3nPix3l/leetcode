class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        sums = set()
        l = 0
        r = len(nums) - 1
        while l < r:
            # store the sum instead of the average
            # since we're always taking the average of 2 numbers
            sums.add(nums[r] + nums[l])
            l += 1
            r -= 1
        return len(sums)