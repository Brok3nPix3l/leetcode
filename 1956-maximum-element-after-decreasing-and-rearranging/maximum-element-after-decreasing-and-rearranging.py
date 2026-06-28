class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curMax = 1
        for num in arr:
            if num >= curMax:
                curMax += 1
        return curMax - 1