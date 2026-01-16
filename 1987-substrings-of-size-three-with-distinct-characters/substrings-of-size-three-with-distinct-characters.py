class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        char_count = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in char_count:
                char_count[s[r]] = 0
            char_count[s[r]] += 1
            if r - l == 2:
                if self.is_good(char_count):
                    count += 1
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
            # print(char_count)
        
        return count

    def is_good(self, char_count: dict[chr, int]) -> bool:
        for c in char_count:
            if char_count[c] > 1:
                return False
        
        return True