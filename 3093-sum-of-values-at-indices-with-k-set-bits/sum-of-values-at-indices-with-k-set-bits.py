class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num if i.bit_count() == k else 0 for i, num in enumerate(nums))