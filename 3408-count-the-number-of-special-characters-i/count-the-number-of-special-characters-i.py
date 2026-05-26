class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ctr = Counter(word)
        specialChars = 0
        for letter in string.ascii_lowercase:
            if ctr[letter] > 0 and ctr[letter.upper()] > 0:
                specialChars += 1
        return specialChars