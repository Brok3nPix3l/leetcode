from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0
        
        for val, freq in c.items():
            if freq % k == 0:
                ans += val * freq
        
        return ans