class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersect = set(nums1) & set(nums2)
        if len(intersect) > 0:
            return min(intersect)
        mn1 = min(nums1)
        mn2 = min(nums2)
        return int(str(min(mn1, mn2)) + str(max(mn1, mn2)))