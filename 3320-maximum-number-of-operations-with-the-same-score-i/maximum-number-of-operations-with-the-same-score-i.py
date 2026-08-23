class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        targetScore = nums[0] + nums[1]
        maxOps = 1

        for i in range(2, len(nums), 2):
            if i + 1 > len(nums) - 1:
                break
            curScore = nums[i] + nums[i + 1]
            if curScore != targetScore:
                break
            maxOps += 1
        
        return maxOps