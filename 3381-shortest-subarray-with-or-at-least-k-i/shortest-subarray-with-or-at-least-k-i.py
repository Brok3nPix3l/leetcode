class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        for size in range(1, len(nums) + 1):
            for i in range(len(nums) - (size - 1)):
                # print(nums[i:i + size])
                if isSpecial(nums[i:i + size], k):
                    return size
        return -1

def isSpecial(nums: List[int], k: int) -> bool:
    bitwiseOr = 0
    for num in nums:
        bitwiseOr |= num
    return bitwiseOr >= k