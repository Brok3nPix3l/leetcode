from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        longest = 0
        co = Counter()
        l = 0
        for r, ch in enumerate(s):
            co[ch] += 1
            while co[ch] > 2:
                co[s[l]] -= 1
                l += 1
            curLen = r - l + 1
            if r - l + 1 > longest:
                longest = curLen
        return longest