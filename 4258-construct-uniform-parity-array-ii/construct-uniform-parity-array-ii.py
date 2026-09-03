class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallest = min(nums1)

        if smallest % 2 == 1:
            return True
        
        return all(num % 2 == 0 for num in nums1)