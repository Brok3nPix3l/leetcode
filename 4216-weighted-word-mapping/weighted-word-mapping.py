class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        word_weights = [0] * len(words)
        for i, word in enumerate(words):
            for c in word:
                word_weights[i] += weights[ord(c) - ord('a')]
        print(word_weights)
        ans = [None] * len(words)
        for i, weight in enumerate(word_weights):
            ans[i] = chr(ord('z') - weight % 26)
        return "".join(ans)