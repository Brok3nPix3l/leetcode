import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        return sum(1 if self.is_beautiful_pair(int(str(nums[i])[0]), int(str(nums[j])[-1])) else 0 for i in range(len(nums)) for j in range(i + 1, len(nums)))
    
    def is_beautiful_pair(self, x: int, y: int) -> bool:
        return math.gcd(x, y) == 1