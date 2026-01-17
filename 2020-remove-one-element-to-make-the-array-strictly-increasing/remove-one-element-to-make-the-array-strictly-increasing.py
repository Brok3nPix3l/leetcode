class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        for i in range(len(nums)-1):
            # print(i)
            if not (nums[i] < nums[i+1]):
                if removed:
                    return False
                # try removing nums[i+1]
                if len(nums) < i+3 or nums[i] < nums[i+2]:
                    # print(f'removed {i+1}')
                    i += 1
                    removed = True
                # try removing nums[i]
                elif i == 0 or nums[i-1] < nums[i+1]:
                    # print(f'removed {i}')
                    removed = True
                else:
                    return False
        
        return True