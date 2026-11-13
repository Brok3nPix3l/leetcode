class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing = []
        
        for i in range(min(nums), max(nums) + 1):
            if i not in nums:
                missing.append(i)
        
        return missing