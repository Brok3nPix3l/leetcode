class Solution:
    def minOperations(self, s: str) -> int:
        """
        0 if it's sorted
        1 if either:
            - the smallest element is at position 0
            - the largest element is at position n - 1
        -1 if n == 2 and it's not sorted
        else 2
        """
        s_s = ''.join(sorted(s))
        if s_s == s:
            return 0
        
        if s[0] == s_s[0] or s[-1] == s_s[-1]:
            return 1
        
        if len(s) == 2:
            return -1
        
        if s_s[0] not in s[:-1] and s_s[-1] not in s[1:]:
            return 3
            
        return 2