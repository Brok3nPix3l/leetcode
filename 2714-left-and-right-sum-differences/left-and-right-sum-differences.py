class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre_sum = [nums[0]]
        for num in nums[1:]:
            pre_sum.append(pre_sum[-1] + num)
        suf_sum = [nums[-1]]
        for num in nums[-2::-1]:
            suf_sum.insert(0, suf_sum[0] + num)
        return [abs(pre - suf) for pre, suf in zip(pre_sum, suf_sum)]