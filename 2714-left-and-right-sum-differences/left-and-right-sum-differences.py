class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = 0, sum(nums)
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            rightSum -= num
            ans[i] = abs(leftSum - rightSum)
            leftSum += num
        return ans