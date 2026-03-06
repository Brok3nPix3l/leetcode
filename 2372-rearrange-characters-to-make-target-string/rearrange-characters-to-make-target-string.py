class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counter = Counter(s)
        target_counter = Counter(target)
        return min(int(s_counter[char] / target_counter[char]) for char in set(target))