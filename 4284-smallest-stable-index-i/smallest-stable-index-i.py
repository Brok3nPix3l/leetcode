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
    largest = nums[0]

    for i in range(1, n):
        largest = max(largest, nums[i])
        ans[i] = largest
    
    return ans

def generateSmallestSuffixArray(nums: list[int]) -> list[int]:
    n = len(nums)

    ans = [nums[-1]] * n
    smallest = nums[-1]

    for i in range(n - 2, -1, -1):
        smallest = min(smallest, nums[i])
        ans[i] = smallest
    
    return ans