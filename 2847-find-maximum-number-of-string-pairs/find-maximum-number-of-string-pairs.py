class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        rev = set()

        for word in words:
            if word in rev:
                ans += 1
            else:
                rev.add(word[::-1])

        return ans