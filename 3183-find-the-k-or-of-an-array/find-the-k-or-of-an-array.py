class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        setBitCount = [0] * 32
        for num in nums:
            curBit = 0
            while num > 0:
                setBitCount[curBit] += num & 1
                num >>= 1
                curBit += 1
        # print(setBitCount)
        ans = 0
        for b, s in enumerate(setBitCount):
            if s >= k:
                ans += 2 ** b
        return ans