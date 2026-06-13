class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join([chr(122 - weight % 26) for weight in [sum(weights[ord(c) - 97] for c in word) for word in words]])