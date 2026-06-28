class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        curMax = 1
        sortedArr = sorted(arr)
        for i, num in enumerate(sortedArr):
            sortedArr[i] = min(curMax, num)
            curMax = sortedArr[i] + 1
        return sortedArr[-1]