class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = {letter: False for letter in string.ascii_lowercase + string.ascii_uppercase}
        for letter in word:
            seen[letter] = True
        specialChars = 0
        for letter in string.ascii_lowercase:
            if seen[letter] and seen[letter.upper()]:
                specialChars += 1
        return specialChars