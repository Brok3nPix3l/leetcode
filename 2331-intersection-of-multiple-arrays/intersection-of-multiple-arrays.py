class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        unique = [set(l) for l in nums]
        intersection = unique[0]
        for s in unique[1:]:
            intersection &= s
        return sorted(list(intersection))