class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_distance = None
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[j] != nums[k]:
                        continue
                    
                    cur_distance = abs(i - j) + abs(j - k) + abs(k - i)
                    if not min_distance:
                        min_distance = cur_distance
                    else:
                        min_distance = min(min_distance, cur_distance)
        
        return -1 if min_distance == None else min_distance