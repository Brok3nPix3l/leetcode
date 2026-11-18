class Solution:
    def minChanges(self, s: str) -> int:
        # we can just treat all substrings as length 2
        # it doesn't matter if we create a valid substring of length 4, because that can also be expressed as two valid sbustrings of length 2
        
        # iterate over every 2 characters of the string and, if they don't match, increment changes required by 1

        changes_needed = 0
        
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes_needed += 1
        
        return changes_needed