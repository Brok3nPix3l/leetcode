class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            res[i] = nums[(i + n) % len(nums)]
        
        return res