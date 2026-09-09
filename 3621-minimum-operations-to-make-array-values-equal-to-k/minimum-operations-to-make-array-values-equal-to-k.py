class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set(nums)
        
        if min(s) < k:
            return -1
        
        if k in s:
            return len(s) - 1
        
        return len(s)