class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        evens = [num for num in nums if num % 2 == 0]
        return reduce(lambda a, b: a | b, evens, 0)