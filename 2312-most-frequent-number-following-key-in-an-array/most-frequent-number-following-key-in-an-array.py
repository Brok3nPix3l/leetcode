class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = Counter()
        for i, num in enumerate(nums[:-1]):
            if num != key:
                continue
            c[nums[i+1]] += 1
        return c.most_common(1)[0][0]