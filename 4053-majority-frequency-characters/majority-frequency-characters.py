from collections import Counter
from collections import defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq_groups = Counter(s)
        char_by_freq = defaultdict(str)
        for char, freq in freq_groups.items():
            char_by_freq[freq] += char
        
        freq_group_freqs = Counter(freq_groups.values())
        
        largest_group_size = max(sorted((size, k) for k, size in freq_group_freqs.items()))
        
        return char_by_freq[largest_group_size[1]]