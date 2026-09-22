class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            if i >= k:
                if nums[i - k] >= nums[i]:
                    continue
            if i + k < n:
                if nums[i + k] >= nums[i]:
                    continue
            
            ans += nums[i]
        
        return ans