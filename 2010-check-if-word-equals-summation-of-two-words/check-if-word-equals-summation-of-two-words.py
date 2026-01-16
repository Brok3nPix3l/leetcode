class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.num_val(firstWord) + self.num_val(secondWord) == self.num_val(targetWord)

    def num_val(self, word: str) -> int:
        val = int("".join(str(ord(c) - ord('a')) for c in word))
        # print(f'word={word} val={val}')
        return val