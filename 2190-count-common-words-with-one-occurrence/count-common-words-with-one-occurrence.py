class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        ans = 0
        for word, freq in c1.items():
            if freq == 1 and c2[word] == 1:
                ans += 1
        return ans