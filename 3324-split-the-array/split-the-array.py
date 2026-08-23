from collections import defaultdict

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # rephrasing the question; are the following statements true:
        # - all elements appear exactly one or two times
        # - an number of elements appear exactly once (this is guaranteed if the above is true)
        f = defaultdict(int)
        for num in nums:
            f[num] += 1
            if f[num] == 3:
                return False
        
        return True