class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = None
        for i in range(len(nums)):
            pair_sum = nums[i] + nums[-i - 1]
            if not max_pair_sum or pair_sum > max_pair_sum:
                max_pair_sum = pair_sum
        
        return max_pair_sum