class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        mean = sum(nums) // len(nums)
        # s = set(nums)
        target = max(1, mean + 1)
        
        while target in nums:
            target += 1
        
        return target