class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        """
        sliding window
        
        accumulate the valid substrings one window at a time

        for a given window spanning s[l..r], there are r - l + 1 unique valid substrings that have not already been accounted for

        e.g.
        10101
        ^       0 - 0 + 1 = 1 [1]           1 total
        ^^      1 - 0 + 1 = 2 [0, 10]       3 total
        ^ ^     2 - 0 + 1 = 3 [1, 01, 101]  6 total
         ^ ^    3 - 1 + 1 = 3 [0, 10, 010]  9 total
          ^ ^   4 - 2 + 1 = 3 [1, 01, 101]  12 total
        """

        substringCount = 0
        
        bitsInWindow = [0] * 2
        l = 0
        for r, c in enumerate(s):
            bitsInWindow[int(s[r])] += 1
            while all(count > k for count in bitsInWindow):
                bitsInWindow[int(s[l])] -= 1
                l += 1

            substringCount += r - l + 1
        
        return substringCount