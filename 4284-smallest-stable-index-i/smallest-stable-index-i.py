class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        largestPrefix = generateLargestPrefixArray(nums)
        smallestSuffix = generateSmallestSuffixArray(nums)

        for i in range(len(nums)):
            if largestPrefix[i] - smallestSuffix[i] <= k:
                return i
        
        return -1

def generateLargestPrefixArray(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [nums[0]] * n

    for i in range(1, n):
        ans[i] = max(ans[i - 1], nums[i])
    
    return ans

def generateSmallestSuffixArray(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [nums[-1]] * n

    for i in range(n - 2, -1, -1):
        ans[i] = min(ans[i + 1], nums[i])
    
    return ans