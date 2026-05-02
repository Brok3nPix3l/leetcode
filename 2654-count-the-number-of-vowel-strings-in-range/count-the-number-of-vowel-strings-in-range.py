class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(1 if self.isVowelString(word) else 0 for word in words[left:right + 1])
    
    def isVowelString(self, word: str) -> bool:
        return self.isVowel(word[0]) and self.isVowel(word[-1])
    
    def isVowel(self, c: chr) -> bool:
        return c.lower() in ['a', 'e', 'i', 'o', 'u']