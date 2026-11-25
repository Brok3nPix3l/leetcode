class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_distance = float('inf')
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[j] != nums[k]:
                        continue
                    
                    cur_distance = abs(i - j) + abs(j - k) + abs(k - i)
                    min_distance = min(min_distance, cur_distance)
        
        return -1 if min_distance == float('inf') else min_distance