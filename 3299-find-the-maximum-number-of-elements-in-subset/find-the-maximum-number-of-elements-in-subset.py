from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_size_subset = {}
        for num in sorted(set(nums), reverse=True):
            # num can be the largest number in the subset (x^k) or, if there are at least 2 instances of it, one of the smaller numbers (x^(k/2j)). so try both and decide which is bigger? maybe store both all of the way through and return whichever is bigger at the end?
            # print(num)
            if num == 1:
                if c[1] % 2 == 0:
                    max_size_subset[1] = c[1] - 1
                else:
                    max_size_subset[1] = c[1]
            elif c[num] >= 2 and num ** 2 in max_size_subset:
                    max_size_subset[num] = max_size_subset[num ** 2] + 2
            else:
                max_size_subset[num] = 1
            # print(max_size_subset)
        return max(max_size_subset.values())