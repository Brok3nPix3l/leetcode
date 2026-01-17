class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq_dict = {}
        for word in words:
            for c in word:
                if c not in freq_dict:
                    freq_dict[c] = 0
                freq_dict[c] += 1
        
        for f in freq_dict.values():
            if f % len(words) != 0:
                return False
        
        return True