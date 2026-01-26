class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                abs_diff = abs(nums[i] - nums[j])
                if abs_diff == k:
                    count += 1
                elif abs_diff > abs_diff:
                    break
        
        return count