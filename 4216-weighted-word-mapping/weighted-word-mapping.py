class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        word_weights = [sum(weights[ord(c) - ord('a')] for c in word) for word in words]
        return "".join([chr(ord('z') - weight % 26) for weight in word_weights])