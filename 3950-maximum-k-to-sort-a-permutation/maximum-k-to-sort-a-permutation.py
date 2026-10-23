class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # AND of all unsorted elements
        s_nums = sorted(nums)
        ans = None
        is_sorted = True
        
        for i in range(len(nums)):
            if nums[i] != s_nums[i]:
                is_sorted = False
                if ans is None:
                    ans = nums[i]
                else:
                    ans &= nums[i]
        
        return 0 if is_sorted else ans