class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for n, num in enumerate(nums[1:]):
            # print(f'n={n} num={num} sums={sums}')
            cur_sum = num + nums[n]
            if cur_sum in sums:
                return True
            sums.add(cur_sum)
        return False