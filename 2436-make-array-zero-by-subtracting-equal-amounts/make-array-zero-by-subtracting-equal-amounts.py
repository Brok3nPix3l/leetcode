class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        largest = nums[-1]
        removed = 0
        cur = 0
        iterations = 0
        while largest - removed > 0:
            iterations += 1
            while nums[cur] - removed <= 0:
                cur += 1
            removed += nums[cur] - removed
        return iterations