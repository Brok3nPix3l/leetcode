class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        
        for size in range(l, r + 1):
            for i in range(len(nums) - size + 1):
                cur_sum = sum(nums[i:i + size])
                if cur_sum <= 0:
                    continue
                min_sum = min(min_sum, cur_sum)
        
        if min_sum == float('inf'):
            return -1
        
        return min_sum