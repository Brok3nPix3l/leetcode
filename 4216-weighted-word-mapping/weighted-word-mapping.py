class Solution:
    def __init__(self):
        self.a_ord = ord('a')
        self.z_ord = ord('z')

    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join([chr(self.z_ord - weight % 26) for weight in [sum(weights[ord(c) - self.a_ord] for c in word) for word in words]])