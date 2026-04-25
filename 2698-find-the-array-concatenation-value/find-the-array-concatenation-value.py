class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        concat_val = 0
        while l <= r:
            if l == r:
                # print('only one val left in nums')
                new_val = nums[l]
            else:
                new_val = int(f'{nums[l]}{nums[r]}')
            # print(f'new_val={new_val}')
            concat_val += new_val
            # print(f'concat_val={concat_val}')
            l += 1
            r -= 1
        return concat_val