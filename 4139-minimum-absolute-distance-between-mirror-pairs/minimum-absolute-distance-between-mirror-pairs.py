class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        min = -1
        d = {}
        for i, num in enumerate(nums):
            if str(num) in d:
                cur = i - d[str(num)]
                if min == -1 or cur < min:
                    min = cur
            d[str(num)[::-1].lstrip('0')] = i
        return min