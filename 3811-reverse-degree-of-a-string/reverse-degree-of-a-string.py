class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(reverse_degree(c) * (i + 1) for i, c in enumerate(s))

def reverse_degree(c: chr) -> int:
    return(26 - (ord(c) - ord('a')))