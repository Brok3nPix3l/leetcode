from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        i = 0
        ops = 0

        while i < len(nums) and c.most_common(1)[0][1] > 1:
            for _ in range(3):
                if i >= len(nums):
                    continue
                c[nums[i]] -= 1
                i += 1
            
            ops += 1
        
        return ops