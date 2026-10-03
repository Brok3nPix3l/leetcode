from collections import Counter

class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)

        most_common_vowel_freq = 0
        for v in self.vowels:
            most_common_vowel_freq = max(most_common_vowel_freq, c[v])
            del c[v]

        mce = c.most_common(1)
        if len(mce) == 0:
            most_common_consonant_freq = 0
        else:
            most_common_consonant_freq = c.most_common(1)[0][1]

        return most_common_vowel_freq + most_common_consonant_freq