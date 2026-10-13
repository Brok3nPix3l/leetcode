class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # if n is even, there are an equal number of positive and negative numbers
        # if n is odd, the middle number is positive

        n = len(nums)
        nums = [n ** 2 for n in nums]
        nums.sort()
        i = 0
        j = n - 1

        ans = 0
        while i < j:
            ans += nums[j] - nums[i]
            i += 1
            j -= 1
        
        if i == j:
            ans += nums[i]
        
        return ans