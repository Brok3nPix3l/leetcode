class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        c = Counter((num for num in nums if num % 2 == 0))
        if len(c) == 0:
            return -1
        return c.most_common(1)[0][0]