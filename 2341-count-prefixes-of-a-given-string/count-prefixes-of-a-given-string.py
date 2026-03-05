class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum((1 if s.startswith(word) else 0) for word in words)