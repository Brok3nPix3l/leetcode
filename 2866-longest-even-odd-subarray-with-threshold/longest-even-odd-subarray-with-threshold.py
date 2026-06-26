class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = 0
        longest = 0
        for r, num in enumerate(nums):
            if l == r and (nums[l] > threshold or nums[l] % 2 != 0):
                l += 1
            elif nums[r] > threshold or r - l > 0 and nums[r] % 2 == nums[r-1] % 2:
                longest = max(longest, r - l)
                if nums[r] <= threshold and nums[r] % 2 == 0:
                    l = r
                else:
                    l = r + 1
            # print('l', l, 'r', r)
        return max(longest, r - l + 1)