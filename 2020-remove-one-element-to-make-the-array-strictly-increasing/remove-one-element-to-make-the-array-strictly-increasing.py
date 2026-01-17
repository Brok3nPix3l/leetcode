class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if self.is_strictly_increasing(nums[0:i] + nums[i+1:]):
                return True
        
        return False
    
    def is_strictly_increasing(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            if not (nums[i] < nums[i+1]):
                return False
        
        return True