class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        min = max = nums[0]
        for num in nums[1:]:
            if num > max:
                if min == max:
                    max = num
                else:
                    return max
            elif num < min:
                if min == max:
                    min = num
                else:
                    return min
            else:
                return num
        # should not be reached
        exit()