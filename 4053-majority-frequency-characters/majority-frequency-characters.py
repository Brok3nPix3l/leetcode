from collections import Counter
from collections import defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        """
        determine frequency of each char in s
        determine frequency of frequencies of chars in s
        
        return the most frequent frequency; largest frequency if tied
        """

        freq_by_char = Counter(s)
        group_by_freq = defaultdict(str)
        for char, freq in freq_by_char.items():
            group_by_freq[freq] += char
        
        freq_group_freqs = Counter(freq_by_char.values())
        
        _, largest_group_size = max((size, k) for k, size in freq_group_freqs.items())
        
        return group_by_freq[largest_group_size]