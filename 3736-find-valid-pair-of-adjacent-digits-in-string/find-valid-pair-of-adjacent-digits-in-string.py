from collections import Counter
import functools

class Solution:
    def findValidPair(self, s: str) -> str:
        self.c = Counter(s)

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                continue
            
            if self.appearsCorrectNumberOfTimes(s[i]) and self.appearsCorrectNumberOfTimes(s[i + 1]):
                return s[i] + s[i + 1]
        
        return ""

    # @cache
    def appearsCorrectNumberOfTimes(self, d: chr) -> bool:
        num = int(d)

        return self.c[d] == num