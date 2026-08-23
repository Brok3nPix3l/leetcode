class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        targetScore = nums[0] + nums[1]
        maxOps = 1

        if len(nums) % 2 == 0:
            upperBound = len(nums)
        else:
            upperBound = len(nums) - 1
        for i in range(2, upperBound, 2):
            curScore = nums[i] + nums[i + 1]
            if curScore != targetScore:
                break
            maxOps += 1
        
        return maxOps