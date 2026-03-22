class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for i, ni in enumerate(nums):
            for j, ji in enumerate(nums[i+1:]):
                if ji - ni != diff:
                    continue
                for k, ki in enumerate(nums[j+1:]):
                    if ki - ji != diff:
                        continue
                    ans += 1
        return ans