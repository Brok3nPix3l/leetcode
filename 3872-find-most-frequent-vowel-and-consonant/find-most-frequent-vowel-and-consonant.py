from collections import Counter

class Solution:
    vowels = 'aeiou'

    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        most_common = counter.most_common()
        
        max_vowel_freq     = next((freq for ch, freq in most_common if ch in self.vowels), 0)
        max_consonant_freq = next((freq for ch, freq in most_common if ch not in self.vowels), 0)

        return max_vowel_freq + max_consonant_freq