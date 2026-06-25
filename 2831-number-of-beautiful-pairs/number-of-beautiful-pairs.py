import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        return sum(1 if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1 else 0 for i in range(len(nums)) for j in range(i + 1, len(nums)))