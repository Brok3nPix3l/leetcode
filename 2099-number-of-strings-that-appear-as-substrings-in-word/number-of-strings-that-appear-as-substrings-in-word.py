class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum((1 if pattern in word else 0) for pattern in patterns)