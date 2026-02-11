class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        shorter = c1 if len(c1) <= len(c2) else c2
        ans = 0
        for word in shorter:
            if c1[word] == 1 and c2[word] == 1:
                ans += 1
        return ans