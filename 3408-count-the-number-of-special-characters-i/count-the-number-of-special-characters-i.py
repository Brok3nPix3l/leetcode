class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = [False] * 58
        for letter in word:
            seen[ord(letter) - ord('A')] = True
        specialChars = 0
        for letter in string.ascii_lowercase:
            if seen[ord(letter) - ord('A')] and seen[ord(letter.upper()) - ord('A')]:
                specialChars += 1
        return specialChars