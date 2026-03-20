class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        pairs = 0
        rem = 0
        for n in c:
            pairs += c[n] // 2
            rem += c[n] % 2
        return [pairs, rem]