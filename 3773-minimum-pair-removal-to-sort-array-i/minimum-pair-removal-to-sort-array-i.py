class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while sorted(nums) != nums:
            s, i = minPair(nums)
            nums.pop(i)
            nums[i] = s
            ops += 1
        
        return ops

def minPair(nums: List[int]) -> Tuple[int, int]:
    m = float('inf')
    mi = -1
    for i in range(len(nums) - 1):
        cur = nums[i] + nums[i + 1]
        if cur < m:
            m = cur
            mi = i
    
    return (m, mi)