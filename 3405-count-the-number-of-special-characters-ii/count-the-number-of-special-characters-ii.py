class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = [0 for _ in string.ascii_lowercase]
        for c in word:
            if c == c.lower():
                if seen[ord(c.lower()) - ord('a')] in [0, 1]:
                    seen[ord(c.lower()) - ord('a')] = 1
                else:
                    seen[ord(c.lower()) - ord('a')] = 3
            else:
                if seen[ord(c.lower()) - ord('a')] in [1, 2]:
                    seen[ord(c.lower()) - ord('a')] = 2
                else:
                    seen[ord(c.lower()) - ord('a')] = 3
        return sum(1 if v == 2 else 0 for v in seen)