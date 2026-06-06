class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = 0, sum(nums) - nums[0]
        ans = [abs(leftSum - rightSum)]
        for i, num in enumerate(nums[:-1]):
            leftSum += num
            rightSum -= nums[i+1]
            ans.append(abs(leftSum - rightSum))
        return ans