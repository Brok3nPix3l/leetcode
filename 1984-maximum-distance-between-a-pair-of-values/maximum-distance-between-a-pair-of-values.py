import bisect

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        for each number in nums1:
        - binary search for the last number in nums2[idx1:] that is >=
        - update max_dist based on distance between indices
        return max_dist
        """
        
        max_dist = 0
        for i, n1 in enumerate(nums1):
            # print(f'i={i} n1={n1}')
            j = bisect.bisect_right(nums2, -n1, lo=i, key=lambda x: -x) - 1
            if j < i:
                continue
            n2 = nums2[j]
            # print(f'j={j} n2={n2}')
            max_dist = max(max_dist, j - i)
            # print(f'max_dist={max_dist}')
        return max_dist