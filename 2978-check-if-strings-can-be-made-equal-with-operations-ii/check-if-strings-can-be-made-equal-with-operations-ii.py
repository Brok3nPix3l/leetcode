class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return (Counter(c for c in s1[::2]) == Counter(c for c in s2[::2])
            and Counter(c for c in s1[1::2]) == Counter(c for c in s2[1::2]))