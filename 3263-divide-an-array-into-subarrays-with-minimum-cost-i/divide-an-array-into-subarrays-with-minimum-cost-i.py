import heapq

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return sum(heapq.nsmallest(2, nums[1:])) + nums[0]