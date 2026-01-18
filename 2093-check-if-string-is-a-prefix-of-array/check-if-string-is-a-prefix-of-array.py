class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        wi = 0
        for c in s:
            if wi >= len(words) or words[wi][i] != c:
                return False
            i += 1
            if i >= len(words[wi]):
                wi += 1
                i = 0
        
        return i == 0