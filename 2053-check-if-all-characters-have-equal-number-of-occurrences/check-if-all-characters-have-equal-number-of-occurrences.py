class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq_dict = {}
        for c in s:
            if c not in freq_dict:
                freq_dict[c] = 0
            freq_dict[c] += 1
        
        for freq in freq_dict.values():
            if freq != freq_dict[s[0]]:
                return False
        
        return True