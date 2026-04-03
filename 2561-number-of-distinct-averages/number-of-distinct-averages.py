class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        avgs = set()
        while len(nums) > 0:
            avgs.add((nums.pop() + nums.pop(0)) / 2)
        return len(avgs)