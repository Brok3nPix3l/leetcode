class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min, max = float('inf'), 0
        for num in nums:
            if num < min:
                min = num
            if num > max:
                max = num
        return (max - min) * k