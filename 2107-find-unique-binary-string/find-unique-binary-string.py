class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # nums_set = set(nums)
        # print(nums_set)
        for i in range(2 ** len(nums)):
            candidate = bin(i)[2:].zfill(len(nums))
            # print(candidate)
            if candidate not in nums:
                return candidate