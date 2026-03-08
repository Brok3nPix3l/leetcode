class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        for _ in range(int(log2(len(nums)))):
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
        return nums[0]