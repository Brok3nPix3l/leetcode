class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersect = set(nums1) & set(nums2)
        if intersect:
            return min(intersect)
        a, b = sorted((min(nums1), min(nums2)))
        return int(f'{a}{b}')