class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        longest_log = max(n, m)
        # if longest_log <= k:
        #     return 0
        
        # longest_log - k = a + b
        # a + b > 0
        # a <= k
        # b <= k
        # minimize a * b

        # theory: maximizing the length of one log and minimizing the length of the other log will always give the smallest a * b
        # set a to k
        # set b to longest_log - k
        return k * max(longest_log - k, 0)