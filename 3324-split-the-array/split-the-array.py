class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # rephrasing the question; are the following statements true:
        # - all elements appear exactly one or two times
        # - an number of elements appear exactly once (this is guaranteed if the above is true)
        f = {}
        for num in nums:
            numFreq = f.get(num, 0) + 1
            if numFreq == 3:
                return False
            f[num] = numFreq
        
        return True