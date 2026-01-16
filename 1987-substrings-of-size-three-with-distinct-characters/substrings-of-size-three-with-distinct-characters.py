class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            if self.is_good(s[i:i+3]):
                count += 1
        
        return count

    def is_good(self, s: str) -> bool:
        cur_seq = set()
        for c in s:
            if c in cur_seq:
                return False
            cur_seq.add(c)
        
        return True