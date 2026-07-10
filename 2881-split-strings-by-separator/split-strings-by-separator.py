class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return list(filter(lambda x: bool(x), (s for word in words for s in word.split(separator))))