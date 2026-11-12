class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        should_be_increasing = 1
        longest = 0

        def compare_to_previous_index(i: int) -> int:
            """
            returns:
              - -1 if the value at index i is less than the value at index i - 1
              - 1 if the value at index i is greater than the value at index i - 1
              - 0 if the value at index i is the same as the value at index i - 1
            """

            if nums[r] == nums[r - 1]:
                return 0

            return 1 if nums[r] > nums[r - 1] else -1
        
        for r in range(1, n):
            if r == l - 1:
                continue
            
            comparison = compare_to_previous_index(r)
            if comparison == should_be_increasing:
                continue
            
            longest = max(longest, r - l)
            # print(f'l={l} r={r} longest={longest}')
            l = r if comparison == 0 else r - 1
            should_be_increasing = -1 * should_be_increasing
        
        return max(longest, n - l)