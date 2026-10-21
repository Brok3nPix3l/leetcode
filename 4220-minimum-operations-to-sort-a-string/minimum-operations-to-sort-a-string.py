class Solution:
    def minOperations(self, s: str) -> int:
        """
        0 if it's sorted
        1 if either:
            - the smallest element is at position 0
            - the largest element is at position n - 1
        -1 if n == 2 and it's not sorted
        3 if both:
            - the smallest element is only present at the last index
            - the largest element is only present at the first index
        else 2
        """
        s_s = ''.join(sorted(s))
        if s_s == s:
            return 0
        
        if s[0] == s_s[0] or s[-1] == s_s[-1]:
            return 1
        
        if len(s) == 2:
            return -1
        
        if s[-1] == s_s[0] and s[0] == s_s[-1] and s.count(s_s[0]) == 1 and s.count(s_s[-1]) == 1:
            return 3

        return 2