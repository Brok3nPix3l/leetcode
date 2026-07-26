class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for size in range(1, len(nums) + 1):
            # print('size', size)
            for i in range(len(nums) - size + 1):
                # print('i', i)
                subarray_count = len(set(nums[i:i + size]))
                # print('subarray', nums[i:i + size])
                ans += subarray_count ** 2
        return ans